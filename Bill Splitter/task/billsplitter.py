import random

# write your code here
print("Enter the number of friends joining (including you):")
num_friends = int(input())

friends = {}
if num_friends <= 0:
    print('No one is joining for the party')
else:
    print("Enter the name of every friend (including you), each on a new line:")
    for _ in range(num_friends):
        friends[input()] = 0
    bill_total = float(input('Enter the total bill value:\n'))
    lucky = input('Do you want to use the "Who is lucky?" feature? Type Yes or No\n')
    if lucky == 'Yes':
        winner = random.choice(list(friends))
        print(f"{winner} is the lucky one!")
        share = round(bill_total / (len(friends) - 1), 2)
        for name in friends:
            if name != winner:
                friends[name] = share
    else:
        print('No one is going to be lucky')
        share = round(bill_total / len(friends), 2)
        for name in friends:
            friends[name] = share
    print(friends)
    
