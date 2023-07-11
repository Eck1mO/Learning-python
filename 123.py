import random

while True:
    try:
        num_one = str(
            input("Please enter you're date of birthday (dd,mm,yy): "))
    except ValueError as e:
        print(e)
        print("You must enter (dd.mm.yy)")
        continue
    if num_one != '08.08.74':
        print("Wrong")
        break
    if num_one == '08.08.74':
        print("Okey, Let's go!")
        random_num = random.randint(1, 2)
        while True:
            num = int(input("Guess the number from 1 to 49: "))
            if num != random_num:
                print("Try again...")
                continue
            print("Congratulations!", random_num)

            print("Отгадайте загадку: \nЯ ползаю без ног,\nЯ лазаю без рук,\nВезде проникаю,\nВезде проникнуть могу.")

            answer3 = input("\nEnter you're answer (c большой буквы): ")

            if answer3 == 'Тень':
                print("Congratulations!!! Go to the next step")
            else:
                print("Wrong =(")
                answer8 = input(
                    "Do you want to continue, or try again? (yes/no): ")
                if answer8 == 'no':
                    continue

    answer4 = input("Укажите квадратный корень числа 49: ")
    if answer4 == 2401:
        print("Congratulations!!! Go to the next step")
    else:
        print("Wrong =(")
        break
    print("Поздравляю, вы прошли все испытания, теперь можете открывать подарок!!!")
    answer8 = input("Do you want to continue, or try again? (yes/no): ")
    if answer8 == 'no':
        break
