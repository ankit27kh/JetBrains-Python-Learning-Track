import random
import sqlite3


class Banking:
    conn = sqlite3.connect('card.s3db')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS card ('
                'id INTEGER PRIMARY KEY,'
                'number TEXT,'
                'pin TEXT,'
                'balance INTEGER DEFAULT 0);')
    conn.commit()

    def __init__(self):
        self.IIN = 400000
        self.account_num = 000000000
        self.checksum = 0
        self.pin = '0000'
        self.card_num = str(self.IIN) + str(self.account_num) + str(self.checksum)
        self.balance = 0
        self.card_numbers = self.numbers()
        self.menu()

    def numbers(self):
        self.cur.execute("SELECT number FROM card")
        card_numbers = self.cur.fetchall()
        card_numbers = [i[0] for i in card_numbers]
        return card_numbers

    def menu(self):
        print('1. Create an account')
        print('2. Log into account')
        print('0. Exit')
        n = int(input())
        if n == 1:
            print()
            self.create_account()
        elif n == 2:
            print()
            self.log_account()
        elif n == 0:
            print()
            self.exit()
        else:
            print('Incorrect input')
            self.menu()

    def create_account(self):
        while True:
            self.account_num = str(random.randint(0, 10 ** 9 - 1))
            self.account_num = (9 - len(self.account_num)) * '0' + self.account_num
            self.card_num = str(self.IIN) + str(self.account_num) + str(self.checksum)
            self.checksum = self.make_checksum(self.card_num)
            self.card_num = str(self.IIN) + str(self.account_num) + str(self.checksum)
            self.card_numbers = self.numbers()
            if self.card_num not in self.card_numbers:
                break
            else:
                continue
        self.pin = str(random.randint(0, 10 ** 4 - 1))
        self.pin = (4 - len(self.pin)) * '0' + self.pin
        print('Your card number has been created')
        print('Your card number:')
        print(self.card_num)
        print('Your card PIN:')
        print(self.pin)
        print()
        self.cur.execute(f"INSERT INTO card (number, pin) VALUES ({self.card_num}, {self.pin})")
        self.conn.commit()
        self.menu()

    def make_checksum(self, number):
        number = number[:-1]
        number = [int(i) for i in number]
        number = [number[i - 1] if i % 2 == 0 else number[i - 1] * 2 for i in range(1, 16)]
        number = [number[i - 1] if number[i - 1] < 10 else number[i - 1] - 9 for i in range(1, 16)]
        count = sum(number)
        if count % 10 == 0:
            self.checksum = '0'
        else:
            self.checksum = str(10 - count % 10)
        return self.checksum

    def log_account(self):
        print('Enter your card number:')
        num = input()
        print('Enter your PIN:')
        pin = input()
        self.card_numbers = self.numbers()
        if num in self.card_numbers:
            self.cur.execute(f"SELECT pin FROM card WHERE number = {num}")
            pin_check = self.cur.fetchone()[0]
            pin_check = (4 - len(pin_check)) * '0' + pin_check
            if pin_check == pin:
                print('You have successfully logged in!')
                self.account_details(num)
            else:
                print('Wrong card number or PIN!')
                self.menu()
        else:
            print('Wrong card number or PIN!')
            self.menu()

    def account_details(self, card_number):
        print()
        print('1. Balance')
        print('2. Add income')
        print('3. Do transfer')
        print('4. Close account')
        print('5. Log out')
        print('0. Exit')
        n = int(input())
        if n == 1:
            self.cur.execute(f"SELECT balance FROM card WHERE number = {card_number}")
            balance = self.cur.fetchone()[0]
            print(f'Balance: {balance}')
            print()
            self.account_details(card_number)
        elif n == 2:
            print()
            print('Enter income:')
            income = int(input())
            self.cur.execute(f"SELECT balance FROM card WHERE number = {card_number}")
            balance = self.cur.fetchone()[0]
            self.cur.execute(f"UPDATE card SET balance = ({balance + income}) WHERE number = {card_number}")
            self.conn.commit()
            print('Income was added!')
            print()
            self.account_details(card_number)
        elif n == 3:
            print()
            print('Transfer')
            print('Enter card number:')
            card_transfer = input()
            self.transfer(card_transfer, card_number)
        elif n == 4:
            print()
            self.cur.execute(f"DELETE FROM card WHERE number = {self.card_num}")
            self.conn.commit()
            print('The account has been closed!')
            print()
            self.menu()
        elif n == 5:
            print()
            print('You have successfully logged out!')
            print()
            self.menu()
        elif n == 0:
            print()
            self.exit()

    def transfer(self, number, original):
        checksum = self.make_checksum(number)
        self.card_numbers = self.numbers()
        if checksum != number[-1]:
            print('Probably you made a mistake in the card number. Please try again!')
            self.account_details(original)
        elif number == original:
            print("You can't transfer money to the same account!")
            self.account_details(original)
        elif number not in self.card_numbers:
            print('Such a card does not exist.')
            self.account_details(original)
        else:
            print('Enter how much money you want to transfer:')
            money = float(input())
            self.cur.execute(f"SELECT balance FROM card WHERE number = {original}")
            balance = self.cur.fetchone()[0]
            if money > balance:
                print('Not enough money!')
                self.account_details(original)
            else:
                self.cur.execute(f"UPDATE card SET balance = ({balance - money}) WHERE number = {original}")
                self.cur.execute(f"SELECT balance FROM card WHERE number = {number}")
                balance = self.cur.fetchone()[0]
                self.cur.execute(f"UPDATE card SET balance = ({balance + money}) WHERE number = {number}")
                self.conn.commit()
                print('Success!')
                self.account_details(original)

    def exit(self):
        print('Bye!')
        pass


my_bank = Banking()
