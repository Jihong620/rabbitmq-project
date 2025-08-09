# Consumer(Topic)
import pika
import sys

# 定義回調函數處理接收到的訊息
def callback(ch, method, properties, body):
    print(f" [x] {method.routing_key}:{body.decode()}")

# 連接到 RabbitMQ 伺服器
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# 宣告一個主題交換器
channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

# 創建一個臨時 queue
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

# 從命令列參數獲取匹配的 routing keys
binding_keys = sys.argv[1:] if len(sys.argv) > 1 else ['#.info']
for binding_key in binding_keys:
    channel.queue_bind(exchange='topic_logs', queue=queue_name, routing_key=binding_key)

# 處理訊息
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for logs. To exit press CTRL+C')
channel.start_consuming()