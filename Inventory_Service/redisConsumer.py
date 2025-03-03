from redis_om import get_redis_connection
import time
from model.product import Product, redis
from config.redisConfig import redis
from dotenv import load_dotenv
import os


load_dotenv()
key = os.getenv("REDIS_CONSUMER_KEY")
group = os.getenv("REDIS_CONSUMER_GROUP")

def processMessage(results):
    if results != []:
        for result in results:
            message = result[1][0][1]
            product = Product.get(message["product_id"])
            processPayment(product,message)

def processPayment(product: Product, message):
    if product:
        print(f"Product Details : {product}")
        product.quantity = product.quantity - int(message['quantity'])
        product.save()
        redis.xadd("payment_received", dict(message), "*")
    else:
        # Produce Message for Refund
        redis.xadd("refund_order", dict(message), '*')


try:
    redis.xgroup_create(key, group)
except:
    print('Group Already Exists!')

while True:
    try:
        results = redis.xreadgroup(group, key, {key: '>'}, None)
        processMessage(results)

    except Exception as ex:
        print(str(ex))
    time.sleep(1)
