# Producer(Pub/Sub)
import pika
import sys

# 連接到 RabbitMQ 伺服器
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# 宣告一個 exchange，類型為 'fanout'
channel.exchange_declare(exchange='logs', exchange_type='fanout')

# 從命令列參數獲取訊息，若無則使用預設訊息
message = ' '.join(sys.argv[1:]) or "info: Hello RabbitMQ!"
channel.basic_publish(exchange='logs', routing_key='', body=message)
print(f" [x] Sent '{message}'")

# 關閉連線
connection.close()