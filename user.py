class User:
    def __init__ (self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

# print on separate lines
    def display_info(self):
        print (f'First Name: {self.first_name}')
        print (f'Last Name: {self.last_name}')
        print (f'Email: {self.email}')
        print (f'Age: {self.age}')
        print (f'Rewards Member: {self.is_rewards_member}')
        print (f'Gold Card Points: {self.gold_card_points}')

    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points += 200
    
    def earn_points(self):
        self.gold_card_points += 10

    def spend_points(self,amount):
        self.gold_card_points -= amount

Nora=User('Nora','McCarthy','nzmccarthy16@gmail.com',23)

latte = 100
chair_latte = 110

Nora.enroll()
Nora.display_info()
Nora.earn_points()
Nora.display_info()
Nora.spend_points(latte)
Nora.display_info()