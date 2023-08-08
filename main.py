from utils.utils import load_data, last_five_operations, creat_message, NUMBER_LAST_OPERATIONS

def main():
    last_operations = last_five_operations()
    for item in range(NUMBER_LAST_OPERATIONS):
        print(creat_message(last_operations[item]))

main()
