def get_posts_info(**person):
    info = (
        f"{person['name']} wrote "
        f"{person['posts_qty']} posts,"
        f" his id is {person['id']}"
    )
    return info


info = get_posts_info(name='Bogdan', posts_qty=25, id=1351)
print(info)

############


def describe_pet(animal_type, pet_name):
    print(
        f"\nI have a {animal_type}."
        f"\nMy {animal_type}'s name is {pet_name.title()}.")
    return describe_pet


describe_pet(animal_type='cat', pet_name='Murzik')

##############
# значение по умолчанию


def describe_pet(pet_name, animal_type='cat'):
    print(
        f"\nI have a {animal_type}."
        f"\nMy {animal_type}'s name is {pet_name.title()}.")
    return describe_pet


describe_pet(pet_name='Murzik')  # or
describe_pet('harry', 'humster')  # or
describe_pet(animal_type='dog', pet_name='Vasilii')  # or
describe_pet('willie')  # or
