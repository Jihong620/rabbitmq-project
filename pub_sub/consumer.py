# Consumer(Pub/Sub)
import pika

# 處理訊息
def callback(ch, method, properties, body):
    print(f" [x] Received '{body.decode()}'")

# 連接到 RabbitMQ 伺服器
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# 宣告一個 exchange，類型為 'fanout'
channel.exchange_declare(exchange='logs', exchange_type='fanout')

# 創建一個臨時佇列（獨立且隨機生成）
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

# 將佇列綁定到交換器
channel.queue_bind(exchange='logs', queue=queue_name)

# 設定回調函數並開始消費訊息
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()