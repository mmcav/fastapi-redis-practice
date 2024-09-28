#from main import redis, Product
from main import Product
from redis_om import get_redis_connection
import time

key = "order_completed"
group = "inventory-group"

redis_external = get_redis_connection(
    host="localhost",
    port=14705,
    password="LVAJPGcqZynn9yDm92ZXPFu0pKNPjjDs",
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