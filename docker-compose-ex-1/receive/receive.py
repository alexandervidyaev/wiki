#!/usr/bin/env python
import pika

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

def main():
    credentials = pika.PlainCredentials('admin', 'P@ssw0rd')
    parameters = pika.ConnectionParameters('192.168.1.6', 5672, '/', credentials)
    connection = pika.BlockingConnection(parameters)

    channel = connection.channel()

    channel.queue_declare(queue='queue1')

    channel.basic_consume(
        queue='queue1', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

main()