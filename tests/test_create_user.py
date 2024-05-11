import pytest
from users_pb2 import UserRequestModel
from google.protobuf.wrappers_pb2 import Int32Value
from utils.randomizers.random_string import generate_random_string
from grpc import StatusCode, RpcError

@pytest.mark.asyncio
async def test_create_user_with_full_valid_data_should_be_created(grpc_test_client):
    # Arrange
    user_client = grpc_test_client

    request_model = UserRequestModel(
        email="john@example.com",
        firstName="John",
        lastName="Doe",
        age=Int32Value(value=30),
        isDiscount=True,
        userType=1
    )

    # Act
    response = await user_client.CreateUser(request_model)

    # Assert
    assert response is not None
    assert response.email == "john@example.com"
    assert response.firstName == "John"
    assert response.lastName == "Doe"
    assert response.age.value == 30
    assert response.isDiscount is True
    assert response.id > 0


@pytest.mark.asyncio
@pytest.mark.parametrize("chars_number, is_positive", [
    (3, True),
    (2, False),
    (100, True),
    (101, False)
])
async def test_create_user_last_name_validation(grpc_test_client, chars_number, is_positive):
    # Arrange
    user_client = grpc_test_client
    request_model = UserRequestModel(
        email="test@test.com",
        firstName="FirstName",
        lastName=generate_random_string(chars_number)
    )

    # Act and Assert
    if is_positive:
        # Expect no exception, and user creation should be successful.
        response = await user_client.CreateUser(request_model)
        assert response is not None  # Ensure some response logic if needed
    else:
        # Expect an exception due to invalid last name length.
        with pytest.raises(RpcError) as exc_info:
            await user_client.CreateUser(request_model)
        
        assert exc_info.value.code() == StatusCode.INVALID_ARGUMENT
        if chars_number == 101:
            expected_message = "Last name max length is 100"
        else:
            expected_message = "Last name min length is 3"
        
        assert expected_message in exc_info.value.details()