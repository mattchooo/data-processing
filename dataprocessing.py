database_dict = {}
temporary_dict = {}
transaction_progress = False

def begin_transaction():
    global transaction_progress
    if not transaction_progress:
        transaction_progress = True
        print('\nTransaction has begun.')
    else:
        print('\nTransaction already in progress.')

def put(key, value):
    try:
        value = int(value)
        temporary_dict[key] = value
        print('\n')
        print(key, 'with value', value, 'has been initialized in the transaction.')
    except ValueError:
        print('\nInvalid value. Please enter a valid integer.')

def get(key):
    global database_dict

    if key in database_dict:
        return database_dict[key]
    else:
        return -1

def commit():
    global database_dict
    global temporary_dict
    global transaction_progress

    if transaction_progress:
        database_dict.update(temporary_dict)
        temporary_dict.clear()
        transaction_progress = False
        print('\nTransaction has been committed.')
    else:
        print('\nCannot commit. There is no ongoing transaction.')

def rollback():
    global temporary_dict
    global transaction_progress
    
    if transaction_progress:
        temporary_dict.clear()
        transaction_progress = False
        print('\nTransaction has rollbacked.')
    else:
        print('\nCannot rollback. There is no ongoing transaction.')


def main():
    print('\nWelcome to the transaction database!')
    operation = 0
    while operation != 6:
        print('-----------------------------------\n1: Begin Transaction\n2: Insert/Put New Value\n3: Get Value\n4: Commit Transaction\n5: Rollback\n6: Exit\n')
        try:
            operation = int(input('What would you like to do? '))
        except ValueError:
            print('\nInvalid command.')
            continue

        if operation == 1:
            begin_transaction()
        elif operation == 2:
            global transaction_progress
            if not transaction_progress:
                print('\nCannot insert. There is no ongoing transaction.')
            else:
                key = str(input('What is the name of the key you would like to insert? '))
                value = (input('What is its value? '))
                put(key, value)
        elif operation == 3:
            key = str(input('What is the name of the key you would like to search? '))
            value = get(key)
            if value == -1:
                print('\nThe key does not exist in the database.')
            else:
                print("\nKey's Value:", value)
        elif operation == 4:
            commit()
        elif operation == 5:
            rollback()
        elif operation == 6:
            print('\nThanks for using the database. Have a nice day!')
        else:
            print('\nInvalid command.')

main()