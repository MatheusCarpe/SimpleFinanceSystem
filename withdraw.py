def do_withdraw(bank):
    if bank.withdrawal_count < bank.withdrawal_limits:
        while True:
            try:
                withdraw_input = input('Please enter the withdrawal amount (R$): ')
                withdraw_amount = int(withdraw_input)

                if 0 < withdraw_amount <= bank.limit and withdraw_amount <= bank.account_balance:
                    bank.account_balance -= withdraw_amount
                    bank.bank_statements['Withdrawal Statement'].append(
                        f'Data: {str(bank.data)} - Withdrawal: R$ {withdraw_amount:.2f}')
                    bank.bank_statements['General Statement'].append(
                        f'Data: {str(bank.data)} - Withdrawal: R$ {withdraw_amount:.2f}')
                    print('Withdrawal Successful!')
                    break  # Sair do loop se o saque for bem-sucedido
                elif withdraw_amount <= 0:
                    print("Withdrawal amount must be above R$ 0.")
                    break
                else:
                    print("Invalid withdrawal amount. Please check your balance and withdrawal limit.")
                    break
            except ValueError:
                print("Invalid input. Please enter a valid integer value.")
    else:
        print('You cannot make the withdrawal; you have exceeded the daily limit (3 withdrawals).')
