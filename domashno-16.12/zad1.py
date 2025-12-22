class Wallet:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def add_money(self, amount):
        self.amount += amount

    def spend_money(self, amount):
        if amount <= self.amount:
            self.amount -= amount
        else:
            print("Error")

    def show_balance(self):
        print(f"Balance: {self.amount:.2f} {self.currency}")

wallet = Wallet(100, "BGN")

wallet.add_money(50)
wallet.show_balance()

wallet.spend_money(30)
wallet.show_balance()

wallet.spend_money(200) 