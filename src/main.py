# src/main.py
import asyncio
import os
import sys

# Assuming the grpc_client.py is in src/client and the generated files are in src/generated
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'client')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'generated')))

from grpc_client import create_grpc_channel, get_user_client
from users_pb2 import UserRequestModel
from google.protobuf.wrappers_pb2 import Int32Value

async def main():
    # Create a gRPC channel
    channel = await create_grpc_channel('localhost:5000')

    # Create a user client
    client = get_user_client(channel)

    # Create a request model
    request = UserRequestModel(
        email="example@example.com",
        firstName="John",
        lastName="Doe",
        age=Int32Value(value=25),
        isDiscount=True,
        userType=1  # Assume 1 corresponds to some valid UserType
    )

    try:
        # Make a CreateUser call
        response = await client.CreateUser(request)
        print("CreateUser Response:", response)
    finally:
        # Properly close the channel
        await channel.close()

if __name__ == "__main__":
    asyncio.run(main())
