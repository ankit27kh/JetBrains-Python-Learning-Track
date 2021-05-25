class CoffeeMachine:
    machine_water = 0
    machine_milk = 0
    machine_beans = 0
    machine_cups = 0
    machine_money = 0
    state = ''

    def __init__(self, water, milk, beans, cups, money):
        self.machine_cups = cups
        self.machine_money = money
        self.machine_milk = milk
        self.machine_water = water
        self.machine_beans = beans
        self.state = 'action'
        self.exit = False
        self.make = True
        self.action(self.state)

    def action(self, state):
        if state == 'action':
            action = input('Write action (buy, fill, take, remaining, exit):\n')
            if action == 'fill':
                self.fill(self.machine_water, self.machine_milk, self.machine_beans, self.machine_cups)
            elif action == 'take':
                self.take(self.machine_money)
            elif action == 'buy':
                self.buy(self.machine_water, self.machine_milk, self.machine_beans, self.machine_cups, self.machine_money)
            elif action == 'remaining':
                self.give_status(self.machine_water, self.machine_milk, self.machine_beans, self.machine_cups, self.machine_money)
            elif action == 'exit':
                self.exit = True
        if self.exit:
            self.state = 'exit'

    def give_status(self, water, milk, beans, cups, money):
        print('The coffee machine has:')
        print(f'{water} of water')
        print(f'{milk} of milk')
        print(f'{beans} of coffee beans')
        print(f'{cups} of disposable cups')
        print(f'${money} of money')
        self.action(self.state)

    def take(self, money):
        print(f'I gave you ${money}')
        self.machine_money = 0
        self.action(self.state)

    def fill(self, water, milk, beans, cups):
        self.machine_water = water + int(input('Write how many ml of water you want to add:\n'))
        self.machine_milk = milk + int(input('Write how many ml of milk you want to add:\n'))
        self.machine_beans = beans + int(input('Write how many grams of coffee beans you want to add:\n'))
        self.machine_cups = cups + int(input('Write how many disposable cups you want to add:\n'))
        self.action(self.state)

    def buy(self, water, milk, beans, cups, money):
        print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        what = input()
        if what == '1':
            self.make_espresso(water, milk, beans, cups, money)
        elif what == '2':
            self.make_latte(water, milk, beans, cups, money)
        elif what == '3':
            self.make_cappuccino(water, milk, beans, cups, money)
        else:
            pass
        self.action(self.state)

    def make_espresso(self, water, milk, beans, cups, money):
        self.check_resources(water, milk, beans, cups, coffee='espresso')
        if self.make:
            self.machine_water = water - 250
            self.machine_beans = beans - 16
            self.machine_money = money + 4
            self.machine_cups = cups - 1
            print('I have enough resources, making you a coffee!')
        self.action(self.state)

    def make_latte(self, water, milk, beans, cups, money):
        self.check_resources(water, milk, beans, cups, coffee='latte')
        if self.make:
            self.machine_water = water - 350
            self.machine_beans = beans - 20
            self.machine_milk = milk - 75
            self.machine_money = money + 7
            self.machine_cups = cups - 1
            print('I have enough resources, making you a coffee!')
        self.action(self.state)

    def make_cappuccino(self, water, milk, beans, cups, money):
        self.check_resources(water, milk, beans, cups, coffee='cappuccino')
        if self.make:
            self.machine_water = water - 200
            self.machine_milk = milk - 100
            self.machine_beans = beans - 12
            self.machine_cups = cups - 1
            self.machine_money = money + 6
            print('I have enough resources, making you a coffee!')
        self.action(self.state)

    def check_resources(self, water, milk, beans, cups, coffee):
        self.make = True
        if coffee == 'espresso':
            if water < 250:
                print('Sorry, not enough water!')
                self.make = False
            if beans < 16:
                print('Sorry, not enough beans!')
                self.make = False
            if cups < 1:
                print('Sorry, not enough cups!')
                self.make = False
        if coffee == 'latte':
            if water < 350:
                print('Sorry, not enough water!')
                self.make = False
            if beans < 20:
                print('Sorry, not enough beans!')
                self.make = False
            if cups < 1:
                print('Sorry, not enough cups!')
                self.make = False
            if milk < 75:
                print('Sorry, not enough milk!')
                self.make = False
        if coffee == 'cappuccino':
            if water < 200:
                print('Sorry, not enough water!')
                self.make = False
            if beans < 12:
                print('Sorry, not enough beans!')
                self.make = False
            if cups < 1:
                print('Sorry, not enough cups!')
                self.make = False
            if milk < 100:
                print('Sorry, not enough milk!')
                self.make = False


my_coffee = CoffeeMachine(400, 540, 120, 9, 550)
