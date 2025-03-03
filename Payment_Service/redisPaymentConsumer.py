from config.redisConfig import redis
from dotenv import load_dotenv
import os
import time

from model.order import Order
from model.orderStatus import OrderStatus

load_dotenv()

key = os.getenv("REDIS_CONSUMER_PAY_REC_KEY")
group = os.getenv("REDIS_CONSUMER_GROUP")

def processPaymentConfirmationMessage(message):
    if message != []:
        record = message[0][1][0][1]
        order = Order.get(record["pk"])
        order.status = OrderStatus.PAID.name
        print(f"Save Order Record : {order}")
        order.save()
        

try:
    redis.xgroup_create(key, group)
except:
    print("Redis Group Exists")

while True:
    try:
        message = redis.xreadgroup(group, key, {key: '>'}, None)
        processPaymentConfirmationMessage(message)
    except Exception as err:
        print(f"Error While Reading {key} Redis Stream : {err}")
    time.sleep(1)
