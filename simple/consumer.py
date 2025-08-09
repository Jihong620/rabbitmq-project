# Consumer(Simple)
import pika

# 處理接收的消息
def callback(ch, method, properties, body):
    print(f" [x] Received {body.decode()}")

# 建立到 RabbitMQ 的連線
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# 宣告一個 queue (與 send.py 中相同)
channel.queue_declare(queue='hello')

# 設定 consumer，使用 callback 處理接收到的消息
channel.basic_consume(queue='hello',
                      on_message_callback=callback,
                      auto_ack=True)

# 開始處理訊息
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
