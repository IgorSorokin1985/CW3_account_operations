import json
import datetime

FILENAME = 'data/operations.json'
NUMBER_LAST_OPERATIONS = 5

def load_data(filename):
    '''
    Load data from FILENAME
    :return: list with operations
    '''
    with open(filename, 'r', encoding='UTF-8') as file:
        return json.load(file)

def last_five_operations(operations):
    '''
    Finding last five operations in all list of operations.
    First find inly executed operations.
    Then creating list with all datatimes of operations.
    And finaly, find operations with last five datatimes.
    :return: dictionary with five last operations
    '''
    executed_operations = is_executed(operations)
    all_times = []
    for operation in executed_operations:
        all_times.append(operation['date'])
    all_times.sort(reverse=True)
    last_five_times = all_times[:NUMBER_LAST_OPERATIONS]
    result = {}
    for operation in executed_operations:
        if operation['date'] in last_five_times:
            result [last_five_times.index(operation['date'])] = operation
    return result

def is_executed(operations):
    '''
    Checking operations on having param EXECUTED
    :param operations: list with all operations
    :return: list with only executed operations
    '''
    result = []
    for operation in operations:
        if 'state' in operation and operation['state'] == 'EXECUTED':
            result.append(operation)
    return result

def creat_message(operation):
    '''
    Creating message about operation
    :param operation: operation
    :return: text message
    '''
    result = f'''{datetime_operation(operation['date'])} {operation['description']}
{creat_from(operation)} -> {creat_to(operation)}
{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}
'''
    return result

def creat_from(operation):
    '''
    Transforming operatino['from'] in view "Maestro 7810 84** **** 5568"
    :param operation: operation
    :return: text like "Maestro 7810 84** **** 5568"
    '''
    if 'from' not in operation:
        return 'Cash'
    card_list = operation['from'].split()
    result = ''
    number_account = ''
    for item in card_list:
        if item.isalpha():
            result += item + ' '
        else:
            number_account += item
    result += number_account[:4] + ' ' + number_account[4:6] + '** **** ' + number_account[-4:]
    return result

def creat_to(operation):
    '''
    Transforming operatino['to'] in view "Счет **2869"
    :param operation: operation
    :return: text like "Счет **2869"
    '''
    if 'to' not in operation:
        return 'Cash'
    card_list = operation['to'].split()
    result = ''
    number_account = ''
    for item in card_list:
        if item.isalpha():
            result += item + ' '
        else:
            number_account += item
    result += '**' + number_account[-4:]
    return result

def datetime_operation(date):
    '''
    Creat data format YYYY-MM-DD from income data
    :param date: data
    :return: text
    '''
    data_mod = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f')
    return data_mod.date()
