def nums(a, b):
    a = a + b
    c = a + b
    return (c)


sum = nums('abc', '123')
print(sum)

sum1 = nums('123', 'abc')
print(sum1)

##########################################


def get_posts_info(name, posts_qty):
    info = f"{name} wrote {posts_qty} posts"
    return info


info = get_posts_info('Bogdan', 25)
print(info)

###################################


def favorite_book(title):
    result = f"One of my favorite books is {title}"
    return result


print(favorite_book('Alise in Wonderlands'))
