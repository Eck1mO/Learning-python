class Comment:
    def __init__(self, text):
        self.text = text
        self.votes_qty = 0

    def upvote(self):
        self.votes_qty += 1
    # новый экземпляр класса для магического метода

    def __add__(self, other):  # добавляем магический метод в класс
        return (f"{self.text} {other.text}",
                self.votes_qty + other.votes_qty)
        # возврящяем кортеж из 2 элементов, можено вернуть хоть словарь вот так:
        # return {
        #     'text': f"{self.text} {other.text}",
        #     'total_votes_qty': self.votes_qty + other.votes_qty
        # }

    def __eq__(self, other):
        return self.text == other.text


first_comment = Comment("First comment,")
first_comment.upvote()

second_comment = Comment("Second comment")
second_comment.upvote()


print(first_comment + second_comment)

print(first_comment == second_comment)
