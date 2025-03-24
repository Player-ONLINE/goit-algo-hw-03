import re

def normalize_phone(phone_number):
    phone_number = re.sub(r'[^0-9+]', '', phone_number)

    if phone_number.startswith('+'):
        if phone_number[1:3] != '38':
            return phone_number
        else:
            return phone_number
    else:
        if phone_number.startswith('380'):
            return '+' + phone_number[1:]
        else:
            return '+38' + phone_number

print(normalize_phone("    +38(050)123-32-34"))
print(normalize_phone("     0503451234"))
print(normalize_phone("(050)8889900"))
print(normalize_phone("38050-111-22-22"))
print(normalize_phone("38050 111 22 11   "))
print(normalize_phone("12345"))
