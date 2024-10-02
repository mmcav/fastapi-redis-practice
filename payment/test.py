from redis_om import get_redis_connection, HashModel
from redis.exceptions import ConnectionError, TimeoutError

import os
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'main.env'))

# Configuration
redis_host = os.getenv('REDIS_HOST')
redis_port = os.getenv('REDIS_PORT')
redis_password = os.getenv('REDIS_PW')

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
