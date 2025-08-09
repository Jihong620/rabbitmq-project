# Producer(Work Queue)
import pika
import sys

# 連接到 RabbitMQ 服務器
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# 宣告一個 queue
channel.queue_declare(queue='task_queue', durable=True)

# 發送訊息到 queue
message = ' '.join(sys.argv[1:]) or "Hello RabbitMQ!"
channel.basic_publish(
    exchange='',
    routing_key='task_queue', # 指定 queue 名稱
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=2,  # 設定消息持久化，避免關閉 Server 後資料遺失
    ))
print(f" [x] Sent '{message}'")

# 關閉連線
connection.close()
