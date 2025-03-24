import random

def get_numbers_ticket(min, max, quantity):
    empty_list = list()

    if min < 1 or max > 1000:
        return empty_list
    elif quantity < 1 or quantity > (max - min + 1):
        return empty_list

    mnozuna_dla_unikalnuh_chisel = set()
    while len (mnozuna_dla_unikalnuh_chisel) < quantity:
        random_numbers = random.randint(min, max)
        mnozuna_dla_unikalnuh_chisel.add(random_numbers)

    return sorted(list(mnozuna_dla_unikalnuh_chisel))

print(get_numbers_ticket(1, 49, 6))