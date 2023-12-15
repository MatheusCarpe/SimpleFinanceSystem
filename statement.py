def do_statement(bank):
    while True:
        statement_option = int(input('''
        [ 1 ] General Statement
        [ 2 ] Withdrawal Statement
        [ 3 ] Deposit Statement
        [ 4 ] Quit
        '''))

        if statement_option == 1:
            for general_statement in bank.bank_statements['General Statement']:
                print(general_statement)
        if statement_option == 2:
            for withdrawal_statement in bank.bank_statements['Withdrawal Statement']:
                print(withdrawal_statement)
        if statement_option == 3:
            for deposit_statement in bank.bank_statements['Deposit Statement']:
                print(deposit_statement)
        if statement_option == 4:
            break