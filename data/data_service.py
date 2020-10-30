
def get_balance():
    """Повертає список клієнтів який отримує з файлу 'balance.txt'
    
    Returns:
        balance_list: список клієнтів"""
        with open (".\data\balance.txt") as balance_file:
            from_file = balance_file.readlines()    ]

    balance_list = []

    for line in from_file:
        line = line[:-2]
        line_list = line.split(';')
        balance_list.append(line_list)

    return balance_list


def show_balance(balance_dump):
    balance_code_from = input("З якого коду рядка балансу?\n")
    balance_code_to   = input("По який?\n")

    for balance in balance_dump:
        if balance_code_from < balance[1] < balance_code_to:
            print("Підрозділ балансу: {:18} Код рядка балансу: {:5} На початок 1кв: {:12} 2кв: {:12} 3кв: {:12} 4кв: {:12} На кінець року: {:15}".format( balance[0], balance[1], balance[2], balance[3], balance[4], balance[5], balance[5]))



balance_dump = get_balance()

show_balance(balance_dump)
