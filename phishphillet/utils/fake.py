import random
import string

from faker import Faker

fake = Faker('en-US')
email_domains = [
    'gmail.com',
    'yahoo.com',
    'msn.com',
    'hotmail.com'
]

def getEmail(user_name=None):
    random_domain = random.choice(email_domains)
    if user_name is not None:
        return user_name + '@' + random_domain
    else:
        return fake.email().split('@')[0] + '@' + random_domain

def getPassword():
    return fake.sentence(nb_words=3).replace(' ', '').lower()

def getRandId(num_characters):
    return ''.join(
        random.choice(string.ascii_lowercase + string.digits)
        for _ in range(num_characters)
    )

def getDOBAsWritten():
    dobRaw = fake.date_of_birth()
    dobMonth = str(dobRaw.month).rjust(2, '0')
    dobDay = str(dobRaw.day).rjust(2, '0')
    dobYear = str(dobRaw.year).rjust(4, '0')
    return f"{dobMonth}/{dobDay}/{dobYear}"
