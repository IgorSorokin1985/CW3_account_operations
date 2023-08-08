from utils.utils import load_data, last_five_operations, is_executed, creat_message, creat_from, creat_to

TEST_FILENAME = 'tests/test_operations.json'

TEST_OPERATION = {
    "id": 594226727,
    "state": "EXECUTED",
    "date": "2018-09-12T21:27:25.241689",
    "operationAmount": {
      "amount": "67314.70",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Visa Platinum 1246377376343588",
    "to": "Счет 14211924144426031657"
  }

TEST_OPERATION_2 = {
    "id": 594226727,
    "state": "EXECUTED",
    "date": "2018-09-12T21:27:25.241689",
    "operationAmount": {
      "amount": "67314.70",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации"
  }

TEST_OPERATIONS = [
  {
    "id": 594226727,
    "state": "EXECUTED",
    "date": "2018-09-12T21:27:25.241689",
    "operationAmount": {
      "amount": "67314.70",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Visa Platinum 1246377376343588",
    "to": "Счет 14211924144426031657"
  }]

def test_load_data():
    assert load_data(TEST_FILENAME) == TEST_OPERATIONS

def test_last_five_operations():
    assert last_five_operations(TEST_OPERATIONS) == {0: TEST_OPERATION}

def test_is_executed():
    assert is_executed (TEST_OPERATIONS) == TEST_OPERATIONS

def test_creat_message():
    assert creat_message(TEST_OPERATION) == '''2018-09-12 Перевод организации
Visa Platinum 1246 37** **** 3588 -> Счет **1657
67314.70 руб.
'''

def test_creat_from():
    assert creat_from(TEST_OPERATION) == 'Visa Platinum 1246 37** **** 3588'
    assert creat_from(TEST_OPERATION_2) == 'Cash'

def test_creat_to():
    assert creat_to(TEST_OPERATION) == 'Счет **1657'
    assert creat_to(TEST_OPERATION_2) == 'Cash'
