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

def getEmail():
    return fake.email().split('@')[0] + '@' + random.choice(email_domains)

def getPassword():
    return fake.sentence(nb_words=3).replace(' ', '').lower()

def getRandId():
    return ''.join(
        random.choice(string.ascii_lowercase + string.digits)
        for _ in range(32)
    )

def doReqOne(email, randId, randPageId):
    """
    Enter your email
    """
    url = f'https://deskuser-clientservice7.duckdns.org/{randId}/submission@login'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.5',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Length': '33',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'PHPSESSID=db674589cb4a5b388ed4459425b6dafb',
        'Host': 'deskuser-clientservice7.duckdns.org',
        'Origin': 'https://deskuser-clientservice7.duckdns.org',
        'Pragma': 'no-cache',
        'Referer': f'https://deskuser-clientservice7.duckdns.org/{randId}/{randPageId}.aspx',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Sec-GPC': '1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }
    data = {
        'email': email,
        'submit': 'Submit'
    }

    requests.post(url, data=data, headers=headers, allow_redirects=False)

def doReqTwo(randId, randPageId):
    """
    Enter your password
    """
    url = f'https://deskuser-clientservice7.duckdns.org/{randId}/submission@continue'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.5',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Length': '37',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'PHPSESSID=db674589cb4a5b388ed4459425b6dafb',
        'Host': 'deskuser-clientservice7.duckdns.org',
        'Origin': 'https://deskuser-clientservice7.duckdns.org',
        'Pragma': 'no-cache',
        'Referer': f'https://deskuser-clientservice7.duckdns.org/{randId}/{randPageId}.aspx',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Sec-GPC': '1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }
    data = {
        'password': getPassword(),
        'submit': 'Submit'
    }

    requests.post(url, data=data, headers=headers, allow_redirects=False)

def doReqThree(randId, name, randPageId):
    """
    Fill out all your information
    """
    url = f'https://deskuser-clientservice8.duckdns.org/{randId}/submission@billing'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.5',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Length': '198',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'PHPSESSID=db674589cb4a5b388ed4459425b6dafb',
        'Host': 'deskuser-clientservice7.duckdns.org',
        'Origin': 'https://deskuser-clientservice7.duckdns.org',
        'Pragma': 'no-cache',
        'Referer': f'https://deskuser-clientservice7.duckdns.org/{randId}/{randPageId}.aspx',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Sec-GPC': '1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }
    dobRaw = fake.date_of_birth()
    dobMonth = str(dobRaw.month).rjust(2, '0')
    dobDay = str(dobRaw.day).rjust(2, '0')
    dobYear = str(dobRaw.year).rjust(4, '0')
    dob = f"{dobMonth}/{dobDay}/{dobYear}"
    data = {
        'country': 'US',
        'fullname': name,
        'phone': fake.phone_number(),
        'address': fake.street_address(),
        'address2': '',
        'city': fake.city(),
        'state': fake.state_abbr(),
        'zipcode': fake.zipcode(),
        'dob': dob,
        'ssn': fake.ssn(),
        'submit': 'Submit'
    }

    requests.post(url, data=data, headers=headers, allow_redirects=False)

def doReqFour(randId, name, randPageId):
    """
    Enter payment info
    """
    url = f'https://deskuser-clientservice7.duckdns.org/{randId}/submission@card'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.5',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Length': '61',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'PHPSESSID=db674589cb4a5b388ed4459425b6dafb',
        'Host': 'deskuser-clientservice7.duckdns.org',
        'Origin': 'https://deskuser-clientservice7.duckdns.org',
        'Pragma': 'no-cache',
        'Referer': f'https://deskuser-clientservice7.duckdns.org/{randId}/{randPageId}.aspx',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Sec-GPC': '1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }
    fakeExpiry = fake.credit_card_expire().split('/')
    data = {
        'noc': name,
        'cn': fake.credit_card_number(),
        'acid': '',
        'cem': fakeExpiry[0],
        'cey': f'20{fakeExpiry[1]}',
        '3d': fake.credit_card_security_code()
    }

    requests.post(url, data=data, headers=headers, allow_redirects=False)

def doAllReqs():
    email = getEmail()
    randId = getRandId()
    randPageId = getRandId()
    name = fake.name()
    doReqOne(email, randId, randPageId)
    doReqTwo(randId, randPageId)
    doReqThree(randId, name, randPageId)
    doReqFour(randId, name, randPageId)


def doAllReqsInfinitely():
    i = 0
    threadName = threading.current_thread().name
    while True:
        i += 1
        print(f"{threadName} beginning attack run {i}")
        try:
            doAllReqs()
        except:
            print("Sad Trombone Noise")

def startThreads(num):
    threads = []
    for i in range(num):
        t = threading.Thread(
            target=doAllReqsInfinitely,
            name=f"Thread_{i}"
        )
        t.daemon = True
        threads.append(t)
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


if __name__ == '__main__':
    # doAllReqs()
    startThreads(50)
