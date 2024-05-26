import os
print("Secret auction - Enter you name and the value you want to bid. After that if there are other bidders pass the computer to someone who wants to bid next or finish the auction \n")

the_list = []
def clear_screen():
    if os.name =='nt':
        os.system('cls')
    else:
        os.system('clear')

def next_person():
    name = input("What is your name? \n")
    while True:
        try:
            amount = int(input("How much do you bid \n"))
            break
        except:
            print("Only numbers")
    
    current_person =  {"name": name, "amount": amount}
    the_list.append(current_person)

next_person()
more_people = 0
while more_people == 0:
    ask = input("Is there another person that wants to bid \n")
    if ask == "no":
        more_people = 1
    elif ask == "yes":
        clear_screen()
        next_person()
    else:
        print('\n Invalid choice, please answer yes or no \n')
# print(f"{the_list}")
highest = {"name":"","amount": 0}
for list_item in the_list:
    if list_item["amount"] > highest["amount"]:
        highest = list_item
clear_screen()
print(f"The highest bid was by {highest["name"]}, he/she won with an amount of {highest["amount"]}")