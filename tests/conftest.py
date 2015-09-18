import pytest
from killranswers.connections import cassandra

@pytest.fixture(scope="module", autouse=True)
def connect():
    cassandra()
