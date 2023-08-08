import json

FILENAME = 'data/operations.json'
NUMBER_LAST_OPERATIONS = 5

def load_data():
    with open(FILENAME, 'r', encoding='UTF-8') as file:
        return json.load(file)

def last_five_operations():
    operations = load_data()
    all_times = []
    for operation in operations:
        if 'state' in operation and operation['state'] == 'EXECUTED':
            all_times.append(operation['date'])
        else:
            operations.remove(operation)
    all_times.sort(reverse=True)
    last_five_times = all_times[:NUMBER_LAST_OPERATIONS]
    result = {}
    for operation in operations:
        if operation['date'] in last_five_times:
            result [last_five_times.index(operation['date'])] = operation
    return result

def creat_message(operation):
    result = f'''{operation['date'][:10]} {operation['description']}
{creat_from(operation)} -> {creat_to(operation)}
{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}
'''
    return result

def creat_from(operation):
    if 'from' not in operation:
        return ''
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
    if 'to' not in operation:
        return ''
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

    return result

