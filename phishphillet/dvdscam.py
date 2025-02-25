import random
import string
import threading

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
    return fake.email().split('@')[0] + '@' + random.choice(email_domains)

def get_question_and_answer():
    questions = {
        'What is your mother\'s maiden name?': 'fname',
        'What is your father\'s middle name?': 'mname',
        'What is the name of yoru favorite pet?': 'name',
        'What is your favorite color?': 'color',
        'In what city were you born?': 'city',
        'What is your favorite teacher\'s name?': 'name',
        'What color was your first car?': 'color'
    }

    random_question = random.choice(list(questions.keys()))
    random_answer_type = questions[random_question]
    if random_answer_type == 'fname':
        random_answer = fake.name_female().split(' ')[1]
    elif random_answer_type == 'mname':
        random_answer = fake.name_male().split(' ')[0]
    elif random_answer_type == 'name':
        random_answer = fake.name().split(' ')[0]
    elif random_answer_type == 'color':
        random_answer = random.choice([
              'red'
            , 'orange'
            , 'yellow'
            , 'green'
            , 'blue'
            , 'purple'
            , 'gray'
            , 'black'
            , 'white'
        ])
    elif random_answer_type == 'city':
        random_answer = fake.city()
    else:
        random_answer = fake.word()

    return random_question, random_answer


def do_req_one():
    """
    Initial Sign In
    """
    url = 'https://uplink-cool.live/csslogon/login.php'
    headers = {
        'authority': 'uplink-cool.live',
        'method': 'POST',
        'path': '/csslogon/login.php',
        'scheme': 'https',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.5',
        'cache-control': 'no-cache',
        'content-length': '140',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://uplink-cool.live',
        'pragma': 'no-cache',
        'referer': 'https://uplink-cool.live/csslogon/',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'sec-gpc': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }

    data = {
        '_template': 'table',
        '_next': 'https://uplinksins-ss.live/CSSLogon/2fa/',
        '_captcha': 'false',
        'username': get_email(),
        'password': fake.sentence(nb_words=3).replace(' ', '').lower()
    }

    requests.post(url, data=data, headers=headers, allow_redirects=False)

def do_req_two():
    """
    Verify email address with 6-digit code
    """
    url = 'https://uplink-cool.live/csslogon/2fa/2login.php'
    headers = {
        'authority': 'uplink-cool.live',
        'method': 'POST',
        'path': '/csslogon/2fa/2login.php',
        'scheme': 'https',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.5',
        'cache-control': 'no-cache',
        'content-length': '308',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://uplink-cool.live',
        'pragma': 'no-cache',
        'referer': 'https://uplink-cool.live/csslogon/2fa/info.php',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'sec-gpc': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }

    q1, a1 = get_question_and_answer()
    q2, a2 = get_question_and_answer()
    q3, a3 = get_question_and_answer()

    data = {
        '_template': 'table',
        '_next': 'https://uplinksins-ss.live/CSSLogon/2fa/finish.html',
        '_captcha': 'false',
        'Phone': fake.phone_number().replace('+', '').split('x')[0],
        'Ssn': fake.ssn() if random.randint(0, 10) > 5 else fake.ssn().replace('-', ''),
        'DOB': fake.date_of_birth(minimum_age=45).strftime('%m/%d/%Y' if random.randint(0, 10) > 5 else '%m/%d/%y'),
        'Q1': q1,
        'Ans1': a1,
        'Q2': q2,
        'Ans2': a2,
        'Q3': q3,
        'Ans3': a3
    }

    requests.post(url, data=data, headers=headers, allow_redirects=False)

def do_all_reqs():
    do_req_one()
    do_req_two()

def do_all_reqs_infinitely():
    i = 0
    thread_name = threading.current_thread().name
    while True:
        i += 1
        print(f"{thread_name} beginning attack run {i}")
        try:
            do_all_reqs()
        except:
            print("Sad Trombone Noise")

def start_threads(num):
    threads = []
    for i in range(num):
        t = threading.Thread(
            target=do_all_reqs_infinitely,
            name=f"Thread_{i + 1}"
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
