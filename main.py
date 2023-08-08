from utils.utils import load_data, last_five_operations, creat_message, NUMBER_LAST_OPERATIONS

def main():
    '''
    Main function. Get last five operations and print messages.
    :return: None
    '''
    last_operations = last_five_operations()
    for item in range(NUMBER_LAST_OPERATIONS):
        print(creat_message(last_operations[item]))

main()
