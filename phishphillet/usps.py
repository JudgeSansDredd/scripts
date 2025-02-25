"""Fill the usps scammer's database with nonsense"""
import random
import string
import threading
from time import time

import luhn
import requests
from faker import Faker

############################################################
# WARNING: This script reaches out to a scammer's website. #
# Don't run it unless you know what you're doing           #
############################################################

fake = Faker('en-US')
email_domains = [
    'gmail.com',
    'yahoo.com',
    'msn.com',
    'hotmail.com'
]

def get_email():
    """Returns a fake email with one of the listed domains"""
    return fake.email().split('@')[0] + '@' + random.choice(email_domains)

def get_password():
    """Creates a fake password"""
    return fake.sentence(nb_words=3).replace(' ', '').lower()

def get_credit_card_w_spaces():
    """Gets a cc number with each 4 digits space delimited"""
    cc_fifteen = ''.join([random.choice(string.digits) for _ in range(15)])
    cc_luhn = cc_fifteen + str(luhn.generate(cc_fifteen))
    chunk_size = 4
    cc_split = [cc_luhn[i:i+chunk_size] for i in range(0, len(cc_luhn), chunk_size)]
    return ' '.join(cc_split)

def get_random_id():
    """Creates a random string of 32 characters"""
    return ''.join(
        random.choice(string.ascii_lowercase + string.digits)
        for _ in range(32)
    )

def get_timestamp():
    """Get a ms timestamp"""
    return round(time() * 1_000)

def do_req_one(name, phone, email, address, city, state, zipcode):
    """
    Update your address
    """
    url = f'https://houtai.uaspsq.com/php/app/index/verify-info.php?t={get_timestamp()}'
    data = {
        'murmur': get_random_id(),
        'uid': '',
        'first_name': name,
        'phone': phone,
        'email': email,
        'address': address,
        'city': city,
        'zip': zipcode,
        'state': state
    }

    requests.post(url, data=data, allow_redirects=False, timeout=120)

def do_req_two(name, address, city, state, zipcode):
    """
    Enter your billing info
    """
    url = f'https://houtai.uaspsq.com/php/app/index/verify-card.php?t={get_timestamp()}'
    data = {
        'uid': '1973',
        'card': get_credit_card_w_spaces(),
        'name': name,
        'date': fake.credit_card_expire(),
        'cvv': ''.join([random.choice(string.digits) for _ in range(3)]),
        'state': state,
        'zip': zipcode,
        'city': city,
        'address1': address,
        'address2': ''
    }

    requests.post(url, data=data, allow_redirects=False, timeout=120)

def do_all_reqs():
    """Sequentially perform all requests"""
    email = get_email()
    name = fake.name()
    phone = fake.phone_number().replace('+', '').split('x')[0]
    address = fake.street_address()
    city = fake.city()
    zipcode = fake.zipcode()
    state = fake.state()

    do_req_one(name, phone, email, address, city, state, zipcode)
    do_req_two(name, address, city, state, zipcode)


def do_all_reqs_infinitely():
    """Infinite loop that calls do_all_reqs"""
    i = 0
    thread_name = threading.current_thread().name
    while True:
        i += 1
        print(f"{thread_name} beginning attack run {i}")
        try:
            do_all_reqs()
        except:
            print("Sad Trombone")

def start_threads(num):
    """Begin running threads specified by num"""
    threads = []
    for i in range(num):
        t = threading.Thread(
            target=do_all_reqs_infinitely,
            name=f"Thread_{i}"
        )
        t.daemon = True
        threads.append(t)
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


if __name__ == '__main__':
    # do_all_reqs()
    start_threads(50)
