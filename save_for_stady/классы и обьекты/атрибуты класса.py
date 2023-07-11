class Comment:
    total_comments = 0  # - атрибут класса

    def __init__(self, text):  # - функция создает новый экземпляр класса
        self.text = text  # - атрибут экземпляра класса
        self.votes_qty = 0
        Comment.total_comments += 1


first_comment = Comment("First comment")  # - экземпляр класса
print(Comment.total_comments)

second_comment = Comment("Second comment")  # - экземпляр класса
print(Comment.total_comments)

# атрибут класса так же наследуется экземплярами класса
print(first_comment.total_comments)
# на уровне экземпляра изменить значение нельзя
first_comment.total_comments = 10
print(first_comment.total_comments)
print(Comment.total_comments)
# на прямую изменяем значение атрибута класса(через класс)
Comment.total_comments = 10
print(Comment.total_comments)
print(first_comment.total_comments)
