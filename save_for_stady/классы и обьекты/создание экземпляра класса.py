# __init__ - функция конструктор для создания экземпляров
# классы - это шаблоны для обьектов, на основании шаблонов создаются
# экземпляры, экземпляры могут иметь собственные атрибуты,экземпляры
# наследуют атрибуты классов
# создание класса:
class Car:
    def move(self):
        print("Car is moving")

    def stop(self):
        print("Car stopped")


my_car = Car()

print(type(my_car))
print(isinstance(my_car, Car))

my_car.move()
my_car.stop()
# создание класса с методом __init__


class Comment:
    def __init__(self, text):
        self.text = text
        self.votes_qty = 0

    def upvote(self, qty):
        self.votes_qty += qty


first_comment = Comment("Frist comment")
print(first_comment.__dict__)
print(first_comment.text)
print(first_comment.votes_qty)

first_comment.upvote(5)
print(first_comment.votes_qty)

first_comment.upvote(10)
print(first_comment.votes_qty)


print(type(first_comment))
print(dir(first_comment))
##################################################


class Comment:
    def __init__(self, text, initial_votes_qty=0):
        self.text = text
        self.votes_qty = initial_votes_qty

    def upvote(self, qty):
        self.votes_qty += qty

    def reset_votes_qty(self):
        self.votes_qty = 0


second_comment = Comment("My comment")

print(second_comment.votes_qty)

second_comment.upvote(10)
second_comment.upvote(20)

print(second_comment.votes_qty)

second_comment.reset_votes_qty()
print(second_comment.votes_qty)
# задача


class Image:
    def __init__(self, resolution, title, extension):
        self.resolution = resolution
        self.title = title
        self.extension = extension

    def resize(self, new_resolution):
        self.resolution = new_resolution

    def __str__(self):
        return f"{self.title}.{self.extension}"


first_img = Image('1920x1080', "My dog", 'jpg')

first_img.resize('4000x3000')
print(first_img.resolution)

second_img = Image('8000x5000', "My cat", 'png')
print(second_img)
