import grpc
import os
import sys

# Assuming the grpc_client.py is in src/client and the generated files are in src/generated
generated_files_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'generated'))
if generated_files_directory not in sys.path:
    sys.path.append(generated_files_directory)

from users_pb2_grpc import UserStub

async def create_grpc_channel(address='localhost:5000'):
    """Create and return a gRPC channel."""
    return grpc.aio.insecure_channel(address)

def get_user_client(channel):
    """Create and return a user service client."""
    return UserStub(channel)