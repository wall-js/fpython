import pika
import threading
import json
# import datetime
import time
import uuid

from pika.exceptions import ChannelClosed
from pika.exceptions import ConnectionClosed


class RabbitMQServer(object):
    _instance_lock = threading.Lock()
    dial = ""
    exchange = ""
    routing_key = ""
    receive_queue = ""
    connection = None
    channel = None

    def __init__(self, dial):
        self.dial = dial
        self.connection = pika.BlockingConnection(pika.URLParameters(self.dial))
        self.channel = self.connection.channel()

    def consumer_callback(self, ch, method, properties, body):
        pass
        # print(body)
        # print(properties)
        # ch.basic_ack(delivery_tag=method.delivery_tag)

    def start_consumer(self):
        while True:
            try:
                self.reconnect()
                self.channel.queue_declare(queue=self.receive_queue, durable=True, auto_delete=True)
                self.channel.basic_consume(
                    queue=self.receive_queue, on_message_callback=self.consumer_callback, auto_ack=False)
                self.channel.start_consuming()
            except ConnectionClosed:
                self.reconnect()
                time.sleep(2)
            except ChannelClosed:
                self.reconnect()
                time.sleep(2)
            except Exception as e:
                self.reconnect()
                time.sleep(2)
                print(e)

    @classmethod
    def run(cls, dial, receive_queue):
        cls._instance_lock.acquire()
        consumer = cls(dial)
        consumer.receive_queue = receive_queue
        consumer.start_consumer()
        cls._instance_lock.release()

    def exec(self, func):
        try:
            self.reconnect()
            return func()
        except ConnectionClosed:
            self.reconnect()
            time.sleep(2)
        except ChannelClosed:
            self.reconnect()
            time.sleep(2)
        except Exception as e:
            self.reconnect()
            time.sleep(2)
            print(e)

    def reconnect(self):
        try:
            if self.connection and not self.connection.is_closed:
                self.connection.close()
            self.connection = pika.BlockingConnection(pika.URLParameters(self.dial))
            self.channel = self.connection.channel()
            # self.channel.exchange_declare(exchange=self.exchange, exchange_type="direct")
            # self.channel.queue_bind(exchange=self.exchange, queue=queue_name, routing_key=self.recv_serverid)
        except Exception as e:
            print(e)

    def send(self, routing_key, data):
        """
        发送数据至签名队列
        :param data: 数据 string
        :param routing_key: 路由地址 string
        :return: 会话ID guid
        """
        guid = str(uuid.uuid1())
        message = {"guid": guid, "data": data}
        properties = pika.BasicProperties(delivery_mode=2)  # 消息持久化

        def func(obj):
            obj.channel.queue_declare(queue=routing_key, durable=True, auto_delete=True)
            obj.channel.basic_publish(exchange='', body=json.dumps(message), routing_key=routing_key,
                                      properties=properties)

        return self.exec(func(self))


def listen(dial, receive_queue, server=RabbitMQServer):
    t = threading.Thread(target=server.run, args=(dial, receive_queue,))
    t.setDaemon(True)
    t.start()

# send example:
# server = RabbitMQServer(dial)
# server.send(receive_queue, "666")
