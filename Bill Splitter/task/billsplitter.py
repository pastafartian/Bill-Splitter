# write your code here
print("Enter the number of friends (including you): ")
numFriends = int(input())

friends = []
i = 0
while i < (2 * numFriends):
    if numFriends <= 0:
        print("No one is joining for the party")
        break
    else:
        print("Enter a friend's name (including yours): ")
        friends += input()
        friends += 0
        print(friends)
        i += 1

print(friends[:])
