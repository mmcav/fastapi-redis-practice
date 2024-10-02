#from main import redis, Product
from main import Product
from redis_om import get_redis_connection
import time

import os
from dotenv import load_dotenv

key = "order_completed"
group = "inventory-group"

load_dotenv(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'consumer.env'))

redis_external = get_redis_connection(
    host=os.getenv('REDIS_HOST'),
    port=os.getenv('REDIS_PORT'),
    password=os.getenv('REDIS_PW'),
    decode_responses=True
)

try:
    redis_external.xgroup_create(key, group)
except Exception as e:
    print(str(e))

while True:
    try:
        results = redis_external.xreadgroup(group, key, {key: '>'}, None)
        print(results)
    except Exception as e:
        print(str(e))
    time.sleep(1)