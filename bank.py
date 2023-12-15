import datetime

class Bank:
    def __init__(self):
        self.menu = '''
        [ D ] Deposit
        [ W ] Withdraw
        [ S ] Statement
        [ C ] Check Balance
        [ Q ] Quit
        '''

        self.data = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        self.account_balance = 0
        self.limit = float(500)
        self.bank_statements = {
            "Deposit Statement": [],
            "Withdrawal Statement": [],
            "General Statement": []
        }
        self.withdrawal_count = 0
        self.withdrawal_limits = 3

    def deposit(self):
        from deposit import do_deposit
        do_deposit(self)

    def withdraw(self):
        from withdraw import do_withdraw
        do_withdraw(self)

    def statement(self):
        from statement import do_statement
        do_statement(self)

    def balance(self):
        from balance import do_balance
        do_balance(self)

    def run(self):
        while True:
            option = input(self.menu)

            if option.upper() == 'D':
                self.deposit()

            elif option.upper() == 'W':
                self.withdraw()

            elif option.upper() == 'S':
                self.statement()

            elif option.upper() == 'C':
                self.balance()

            elif option.upper() == 'Q':
                break

            else:
                print('Invalid operation, please enter a valid option.')

        print('Come back anytime and rely on our services!')

if(__name__ == '__main__'):
    banking = Bank()
    banking.run()