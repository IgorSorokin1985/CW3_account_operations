from utils.utils import load_data, last_five_operations, creat_message

def main():
    last_operations = last_five_operations()
    for item in range(5):
        print(creat_message(last_operations[item]))

main()
