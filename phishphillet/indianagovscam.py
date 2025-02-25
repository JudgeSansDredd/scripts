import random
import string
import threading

import requests
from faker import Faker

############################################################
# WARNING: This script reaches out to a scammer's website. #
# Don't run it unless you know what you're doing           #
############################################################

url = 'http://indianagov.us/uplink/account/merge'
fake = Faker('en-US')
email_domains = [
    'gmail.com',
    'yahoo.com',
    'msn.com',
    'hotmail.com'
]

def getEmail():
    return fake.email().split('@')[0] + '@' + random.choice(email_domains)


def doReqOne(email):
    """
    Initial Sign In
    """
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Length': '57',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': '70727=1920; 7b47f=1080; PHPSESSID=682707ae14f14cfab5ca412f8bbd0776; 26c7e8905aac3e25f021a56011d981f5=b9733fe5c7fdca4c54641784dc92c08f; b7b1834ffd04675bde1aae1e1fc43b85=1663049086',
        'Host': 'indianagov.us',
        'Origin': 'http://indianagov.us',
        'Pragma': 'no-cache',
        'Referer': 'http://indianagov.us/uplink/account/signin',
        'Sec-GPC': '1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }

    data = {
        'email': email,
        'password': fake.password(),
        'logsub': 'go'
    }

    res = requests.post(url, data=data, headers=headers, allow_redirects=False)
    print(res)

def doReqTwo():
    """
    Verify email address with 6-digit code
    """
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Length': '20',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': '70727=1920; 7b47f=1080; PHPSESSID=682707ae14f14cfab5ca412f8bbd0776; 26c7e8905aac3e25f021a56011d981f5=b9733fe5c7fdca4c54641784dc92c08f; b7b1834ffd04675bde1aae1e1fc43b85=1663049086',
        'Host': 'indianagov.us',
        'Origin': 'http://indianagov.us',
        'Pragma': 'no-cache',
        'Referer': 'http://indianagov.us/uplink/account/pp?conseled=true',
        'Sec-GPC': '1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }

    data = {
        'email': ''.join(random.choice(string.digits) for i in range(6)),
        'logp': 'go'
    }

    res = requests.post(url, data=data, headers=headers, allow_redirects=False)
    print(res)

def doReqThree(email):
    """
    Log in to your onedrive account
    """
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Length': '183',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': '70727=1920; 7b47f=1080; PHPSESSID=682707ae14f14cfab5ca412f8bbd0776; 26c7e8905aac3e25f021a56011d981f5=b9733fe5c7fdca4c54641784dc92c08f; b7b1834ffd04675bde1aae1e1fc43b85=1663049086',
        'Host': 'indianagov.us',
        'Origin': 'http://indianagov.us',
        'Pragma': 'no-cache',
        'Referer': 'http://indianagov.us/uplink/account/pre/mc',
        'Sec-GPC': '1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }

    data = {
        'i13': '0',
        'emainl': email,
        'loginfmt': '',
        'type': '11',
        'LoginOptions': '3',
        'lrt': '',
        'lrtPartition': '',
        'hisRegion': '',
        'hisScaleUnit': '',
        'thinub': 'ec5e6c6b7759f78ebc0b524be7889ef5',
        'emainlpass': fake.password()
    }

    res = requests.post(url, data=data, headers=headers, allow_redirects=False)
    print(res)

def doReqFour():
    """
    Verify your information
    """
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Length': '93',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': '70727=1920; 7b47f=1080; PHPSESSID=682707ae14f14cfab5ca412f8bbd0776; 26c7e8905aac3e25f021a56011d981f5=b9733fe5c7fdca4c54641784dc92c08f; b7b1834ffd04675bde1aae1e1fc43b85=1663049086',
        'Host': 'indianagov.us',
        'Origin': 'http://indianagov.us',
        'Pragma': 'no-cache',
        'Referer': 'http://indianagov.us/uplink/account/err?contndled=true',
        'Sec-GPC': '1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }

    fnn = fake.name()
    ssn = fake.ssn().split('-')
    dobRaw = fake.date_of_birth()
    dobMonth = str(dobRaw.month).rjust(2, '0')
    dobDay = str(dobRaw.day).rjust(2, '0')
    dobYear = str(dobRaw.year).rjust(4, '0')
    dob = f"{dobMonth}/{dobDay}/{dobYear}"
    dlOne = ''.join(random.choice(string.digits) for i in range(4))
    dlTwo = ''.join(random.choice(string.digits) for i in range(2))
    dlThree = ''.join(random.choice(string.digits) for i in range(4))
    dl = '-'.join([dlOne, dlTwo, dlThree])


    data = {
        'fnn': fnn,
        'ssn1': ssn[0],
        'ssn2': ssn[1],
        'ssn3': ssn[2],
        'dob': dob,
        'dl': dl,
        'nextoo': 'Continue'
    }

    res = requests.post(url, data=data, headers=headers, allow_redirects=False)
    print(res)

def doAllReqs():
    while True:
        # print(f"{threading.get_ident()}: Beginning attack run")
        email = getEmail()
        doReqOne(email)
        doReqTwo()
        doReqThree(email)
        doReqFour()

if __name__ == '__main__':
    threads = []
    for _ in range(50):
        t = threading.Thread(target=doAllReqs)
        t.daemon = True
        threads.append(t)
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
