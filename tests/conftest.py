import sys
import os
import pytest
base_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
client_directory = os.path.join(base_directory, 'src', 'client')
generated_directory = os.path.join(base_directory, 'src', 'generated')

sys.path.append(client_directory)
sys.path.append(generated_directory)
from grpc_client import create_grpc_channel, get_user_client


@pytest.fixture(scope="function")
async def grpc_test_client():
    # Create the channel
    channel = await create_grpc_channel('localhost:5000') # I'm lazy, so I'm hardcoding the port for this example. It should be read from a config file
    
    # Create the client
    client = get_user_client(channel)

    # Provide the client to the test and ensure it is awaited properly
    try:
        yield client
    finally:
        # Close the channel after the test
        await channel.close()