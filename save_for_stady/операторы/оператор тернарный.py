# у тернарного оператора 3 операнда
my_number = 21.5

print("is int") if type(my_number) is int else print("is not int")
# различие между полноценной функцией
if type(my_number) is int:
    print("is int")
else:
    print("is not int")
#############################################
# send_img(img) if img.get['is_processed'] else process_and_send_img(img)
#############################################
# передача значения тернарного оператора в функцию

product_qty = 10

print("in stock" if product_qty > 0 else "out of stock")
#############################################
# передача значения тернарного оператора в переменную
temp = +24

weather = "hot" if temp > 18 else "cold"
print(weather)
#############################################
my_img = ('1920', '1080')

print(f"{my_img[0]}x{my_img[1]}") if len(
    my_img) == 2 else print("Incorrect image formatting")
###############################################
my_img = ('1920', '1080')

info = f"{my_img[0]}x{my_img[1]}" if len(
    my_img) == 2 else ("Incorrect image formatting")

print(info)
