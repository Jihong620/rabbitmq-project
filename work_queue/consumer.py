# Consumer(Work Queue)
import pika
import time

def callback(ch, method, properties, body):
    print(f" [x] Received {body.decode()}")
    # 模擬處理時間
    time.sleep(body.count(b'.'))  
    print(" [x] Done")

    # 確認消息已被處理
    ch.basic_ack(delivery_tag=method.delivery_tag)

# 連接到 RabbitMQ 服務器
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# 宣告一個持久化的 queue
channel.queue_declare(queue='task(apply_queue', durable=True)

# 設定公平分發，限制每次只處理一條訊息
channel.basic_qos(prefetch_count=1)

# 開始處理訊息
channel.basic_consume(queue='task_queue', on_message_callback=callback)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()