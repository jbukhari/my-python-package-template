# Set up pytest fixtures 
# https://docs.pytest.org/en/8.2.x/explanation/fixtures.html#about-fixtures

import pytest

@pytest.fixture
def my_fixture():
    return 1