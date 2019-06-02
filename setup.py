from setuptools import setup, find_packages

setup(
    name='fpython',
    version='0.0.8',
    keywords=('utils', 'packages'),
    long_description=open("README.rst").read(),
    description='packages',
    license='BSD License',
    author='Wall-js',
    author_email='307606056@qq.com',
    url='https://github.com/Wall-js/fpython',
    platforms=["all"],
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    install_requires=[
        'pika',
    ]
)
