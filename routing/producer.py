# Producer(Routing)
import pika
import sys

# 建立到 RabbitMQ 的連線
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# 宣告一個直接交換器
channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

# 從命令列參數獲取路由鍵和訊息
severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
message = ' '.join(sys.argv[2:]) or "Hello RabbitMQ!"
channel.basic_publish(exchange='direct_logs', routing_key=severity, body=message)
print(f" [x] Sent '{severity}:{message}'")

# 關閉連線
connection.close()