import random
i = 10
while i < 50:
    print(i)
    i += 10
# бесконеочный цикл
# while True:
#     print("Infinite loop")

# выход из цикла с помощью break
while True:
    answer = input("Enter yes or no: ")
    if answer == 'no':
        break
# использование continue в циклах

random_num = random.randint(1, 5)
while True:
    num = int(input("Guess the number from 1 to 5: "))
    if num != random_num:
        print("Try again...")
        continue
    print("Congratulations!", random_num)
    break
# задача
while True:
    num = int(input("Give my you'r numbers, "))
    num1 = int(input("Give my you'r numbers, "))
    delenie = num / num1
    res = int(delenie)
    print(delenie)
    answer = input("Continue: 'yes' or 'no': ")
    if answer == 'no':
        print("Ok, Let's go")
        break
    print('Gratz')
    continue
# решение Богдана + try, except
while True:
    try:
        num_one = float(input("Please enter number one: "))
        num_two = float(input("Please enter number two: "))
    except ValueError as e:
        print(e)
        print("You must enter numbers!")
        continue

    print(num_one / num_two)

    answer = input("Do you want to continue? (yes/no): ")
    if answer == 'no':
        break
