from redis_om import get_redis_connection, HashModel
from redis.exceptions import ConnectionError, TimeoutError

# Configuration
redis_host = 'localhost'
redis_port = 14705
redis_password = 'LVAJPGcqZynn9yDm92ZXPFu0pKNPjjDs'

try:
    # Create a Redis client
    redis_conn = get_redis_connection(
        host=redis_host,
        port=redis_port,
        password=redis_password
    )
    
    # Define a model
    class MyModel(HashModel):
        class Meta:
            database = redis_conn
        
        foo: str
    
    # Create or update a record
    item = MyModel(foo='bar')
    item.save()
    
    # Fetch the record
    retrieved_item = MyModel.get(item.pk)
    print(f'The value of "foo" is: {retrieved_item.foo}')

except ConnectionError:
    print("Could not connect to Redis. Please check your configuration.")
except TimeoutError:
    print("Connection to Redis timed out.")
