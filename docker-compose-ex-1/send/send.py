#!/usr/bin/env python
import pika

def main():
    credentials = pika.PlainCredentials('admin', 'P@ssw0rd')
    parameters = pika.ConnectionParameters('192.168.1.6', 5672, '/', credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    channel.queue_declare(queue='queue1')

    while True:
      channel.basic_publish(exchange='', routing_key='queue1', body='Hello World!')
      print(" [x] Sent 'Hello World!'")


    connection.close()

main()