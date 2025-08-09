# Producer(Simple)
import pika

# 建立到 RabbitMQ 的連線
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# 宣告一個 queue
channel.queue_declare(queue='hello')

# 發送訊息到 queue
message = 'Hello RabbitMQ!'
channel.basic_publish(exchange='',
                     routing_key='hello',
                     body=message)

print(f" [x] Sent '{message}'")

# 關閉連線
connection.close()
