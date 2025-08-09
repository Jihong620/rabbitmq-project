# Producer(Topic)
import pika
import sys
print("Producer(Topic)")
# 連接到 RabbitMQ 伺服器
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# 宣告一個主題交換器
channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

# 從命令列參數獲取路由鍵和訊息
routing_key = sys.argv[1] if len(sys.argv) > 1 else 'anonymous.info'
message = ' '.join(sys.argv[2:]) or "Hello RabbitMQ!"
channel.basic_publish(exchange='topic_logs', routing_key=routing_key, body=message)
print(f" [x] Sent '{routing_key}:{message}'")

# 關閉連線
connection.close()