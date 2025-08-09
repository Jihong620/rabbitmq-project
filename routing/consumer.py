# Consumer(Routing)
import pika
import sys
# 處理訊息
def callback(ch, method, properties, body):
    print(f" [x] {method.routing_key}:{body.decode()}")

# 建立到 RabbitMQ 的連線
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# 宣告一個直接交換器
channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

# 創建一個 queue
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

# 從命令列參數獲取匹配的 routing keys
severities = sys.argv[1:] if len(sys.argv) > 1 else ['info']
for severity in severities:
    channel.queue_bind(exchange='direct_logs', queue=queue_name, routing_key=severity)

# 處理消息
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for logs. To exit press CTRL+C')
channel.start_consuming()