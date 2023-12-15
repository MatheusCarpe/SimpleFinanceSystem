def do_deposit(bank):
    while True:
        try:
            deposit_input = input("Please enter the amount you wish to deposit: R$ ")
            deposit_amount = float(deposit_input.replace(',','.'))

            if deposit_amount > 0:
                bank.account_balance += deposit_amount
                bank.bank_statements['Deposit Statement'].append(
                    f'Data: {str(bank.data)} - Deposit: R$ {deposit_amount:.2f}')
                bank.bank_statements['General Statement'].append(f'Data: {str(bank.data)} - Deposit: R$ {deposit_amount:.2f}')
                print('Deposit successful!')
                break
            else:
                print("Deposit must be above R$ 0.")
        except ValueError:
            print("Invalid input. Please enter a valid numeric value.")


