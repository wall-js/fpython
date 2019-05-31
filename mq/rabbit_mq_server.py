import pika
import threading
import json
import datetime
import time

from pika.exceptions import ChannelClosed
from pika.exceptions import ConnectionClosed


class RabbitMQServer(object):
    _instance_lock = threading.Lock()
    dial = ""
    exchange = ""
    routing_key = ""
    recv_queue = ""
    send_queue = ""
    connection = None
    channel = None

    def consumer_callback(self):
        pass

    def reconnect(self):
        try:
            if self.connection and not self.connection.is_closed:
                self.connection.close()
            self.connection = pika.BlockingConnection(pika.URLParameters(self.dial))
            self.channel = self.connection.channel()
            # self.channel.exchange_declare(exchange=self.exchange, exchange_type="direct")
            self.channel.queue_declare(queue=self.recv_queue, durable=True)
            # self.channel.queue_bind(exchange=self.exchange, queue=queue_name, routing_key=self.recv_serverid)
        except Exception as e:
            print(e)
