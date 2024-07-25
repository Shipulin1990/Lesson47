from threading import Thread, Lock


class BankAccount:

    def __init__(self, account, amount):
        self.account = account
        self.amount = amount

    def deposit(self, amount):
        self.amount += amount
        print(f'Deposited {amount}, new balance is {self.amount}')
        return

    def withdraw(self, amount):
        self.amount -= amount
        print(f'Withdrew {amount}, new balance is {self.amount}')
        return


bank_account_num = BankAccount(1, 1000)

lock = Lock()


def deposit_task(account, amount):
    with lock:
        for _ in range(5):
            account.deposit(amount)


def withdraw_task(account, amount):
    with lock:
        for _ in range(5):
            account.withdraw(amount)


deposit_thread = Thread(target=deposit_task, args=(bank_account_num, 100))
withdraw_thread = Thread(target=withdraw_task, args=(bank_account_num, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()
