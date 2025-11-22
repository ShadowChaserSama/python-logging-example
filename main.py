import logging
import json

logging.basicConfig(
    filename="bank.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

bank_data = {
    'balance': 0
}
with open('bank.json','r',encoding='utf-8') as f:
    bank_data = json.load(f)

class Bank():
    def __init__(self,name,default_balance=500):
        self.name = name
        self.default_balance = default_balance
    
    def save(self):
        with open("bank.json",'w',encoding='utf-8') as f:
            json.dump(bank_data,f,ensure_ascii=False,indent=4)
    
    def deposit(self,amount):
        try:
            if 1 == 1: # test ucun 1 == 1
                print('Deposit process successfuly!')
                bank_data['balance'] += amount
                logging.info(f"Deposit: {amount} AZN")
                self.save()
            else:
                print('You do not have enough money!')
        except Exception as e:
            print('Something went wrong!',e)

    def withdraw(self,amount):
        try:
            if amount < bank_data.get('balance'):
                print('Withdraw process successfuly!')
                bank_data['balance'] -= amount
                logging.info(f"Withdraw: {amount} AZN")
                self.save()
            else:
                print('You do not have enough money in your account!')
        except:
            print('Something went wrong!')

    def transfer(self,amount, from_acc, to_acc):
        try:
            if amount < bank_data.get('balance'):
                print('Transfer process successfuly!')
                bank_data['balance'] -= amount
                logging.info(f"Transfer: {amount} AZN from {from_acc} to {to_acc}")
                self.save()
            else:
                print('You do not have enough money in your account!')
        except:
            print('Something went wrong!')
    
    def show_logs(self):
        try:
            with open("bank.log", "r") as file:
                logs = file.read()
                print("---- LOG FILE CONTENT ----")
                print(logs)
                print("--------------------------")
        except FileNotFoundError:
            print("Log file not found!")



bank = Bank('RI BANK')

while True:
    print(f'''
    ***************************
           {bank.name} 
    ***************************
         BALANCE - {bank_data.get('balance',0)}          
    * 1 - Deposit             *
    *                         *
    * 2 - Withdraw            *
    *                         *
    * 3 - Transfer            *
    *                         *
    * 4 - Show logs           *
    *                         *
    * 0 - EXIT                *
    *                         *
    ***************************
    ''')

    try:
        choice = int(input())
        if choice == 1:
            amount = float(input('Enter a amount: '))
            bank.deposit(amount)
        elif choice == 2:
            amount = float(input('Enter a amount: '))
            bank.withdraw(amount)
        elif choice == 3:
            to_acc = input('Enter a card number: ')
            amount = float(input('Enter a amount: '))
            bank.transfer(amount,'You',to_acc)
        elif choice == 4:
            bank.show_logs()
        elif choice == 0:
            break
        else:
            print('Invalid choice!')
    except Exception as e:
        print('Something went wrong!',e)
