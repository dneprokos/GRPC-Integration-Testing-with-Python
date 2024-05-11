# Test Project: GRPC Integration Testing with Python
![MAIN](/images/GRPC_PYTHON_MAIN.png)

This is a test project written in Python designed to test integration with a GRPC service. The project utilizes the `grpcio` and `grpcio-tools` packages for communicating with the GRPC service. Test server available here: [GrpcServicePracticeOnNet](https://github.com/dneprokos/GrpcServicePracticeOnNet)

## Pre-conditions

Before running the tests, ensure the following pre-conditions are met:
- Pull the [GrpcServicePracticeOnNet](https://github.com/dneprokos/GrpcServicePracticeOnNet) GitHub project.
- Start the GRPC server according to the instructions provided in the project's README.


## How to Run Tests

To run the tests, follow these steps:
1. Install Python 3.8 or later if not already installed.
2. Install dependencies using pipenv: "pipenv install --dev"
3. Activate the virtual environment: "pipenv shell"
4. Run the tests using pytest: "pytest"

## How to Add New Tests

To add new tests, follow these guidelines:
- Write test functions using the pytest framework.
- Place the test files in the `tests` directory.
- Ensure the test functions have descriptive names and cover different scenarios.
- Run the tests locally to verify they pass before committing changes.

With these instructions, you can effectively set up, run, and extend the test suite for integration testing with the GRPC service.


