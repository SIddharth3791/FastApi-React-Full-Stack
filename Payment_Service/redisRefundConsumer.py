from config.redisConfig import redis
from dotenv import load_dotenv
import os
import time

from model.order import Order
from model.orderStatus import OrderStatus

load_dotenv()

key = os.getenv("REDIS_CONSUMER_REFUND_KEY")
group = os.getenv("REDIS_CONSUMER_GROUP")

def processRefund(message):
    if message:
        refundRecord  = message[0][1][0]
        order = Order.get(refundRecord["pk"])
        order['status'] = OrderStatus.REFUND.name
        order.save()
        

try:
    redis.xgroup_create(key, group)
except:
    print("Redis Group Exists")

while True:
    try:
        message = redis.xreadgroup(group, key, {key: '>'}, None)
        print(message)
    except Exception as err:
        print(f"Error While Reading {key} Redis Stream : {err}")
    time.sleep(1)