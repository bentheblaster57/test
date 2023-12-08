import pytest
from app.account import *

@pytest.fixture
def empty_account():
    return account(0)

@pytest.fixture
def account():
    return account(20)