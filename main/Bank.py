user_1 = 25
user_2 = 25
def transaction(user_1, sum, user_2):
    if user_1 >= sum:
        user_1 = user_1 - sum
        user_2 = user_2 + sum
    return user_1, user_2



count = transaction(user_1, 10, user_2)
print(count)