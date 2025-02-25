import random
import string
import threading

import requests
from utils.fake import fake, getDOBAsWritten, getEmail, getPassword, getRandId
from utils.threading import startThreads

############################################################
# WARNING: This script reaches out to a scammer's website. #
# Don't run it unless you know what you're doing           #
############################################################

def doReqOne(username, password):
    """
    Enter your username and password
    """
    url = 'https://customersagent.com/sfb/s/a/b/verify_session_index'
    headers = {
        "authority": "customersagent.com",
        "method": "POST",
        "path": "/sfb/s/a/b/verify_session_index",
        "scheme": "https",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "cache-control": "no-cache",
        "content-length": "31",
        "content-type": "application/x-www-form-urlencoded",
        "cookie": "logged_in=1; cf_chl_2=08b94c8003ea453; cf_clearance=KNp87PlSkf3xL4M_16Yjx7Z6eGw7LkaIV.VA1R7aVOg-1670619059-0-160; Br3HTGjOuHry_0hiUTyRh7-JN7U=gGrpNHTWVjRBr5IMuF0fAXzQ8NE; fI5rN6xWYxedYmV9HH5cUDobbeY=1670619044; NkHfUCBnnFEj06JHs_7l7cw5sX8=1670705444; g9FSN8PpOS9v9c4XZbzLD4HWUv8=-2Clz03FjMzYDZH3J2_6Im70494; D8qBuPFoXta53tH2UoEFAK0o06U=hSG0ipmMB7_zYzxLNii4P5PGjwU; uOXX4PES0Kro0fQpvtcr34aVv-o=1670619058; 7EC2zxFrvkayPdytfxomwDbaMMM=1670705458; SnqCSrDAwXnlfhe5YMDx6M93sck=mUGELSWUHdJbDU4jGNlM0qaLgOw; hJsEsicaR7LRWKpg3g47lH65ysc=ITM_hCtDbo4U9VQUv5VGkaKn9RE; LD7qrT_IsdXVcb5K13bacuGWytY=1670619055; WzOLmM2AGBptnRGtsazQCl2jve4=1670705455; 57FLmw02FwpuA52AqQ9ySIEp7eM=WAYS2ZSifk4KLyHiYt3mQtUiXPk; __cf_bm=t33f41bNzPu9ZDEjFzc8XYPx_nEVBacx4bPaNVwFN9g-1670619060-0-ARjeR5YPojwttwGdk7/CNEyurRR+Pub3suzyoToBlXW7FXLsE6GlICEMuj45WIp83O/V8tyObjXVQHOzcLP6igPwkkE3tOvgNCwnB2ZCIUqfvOIiWqKqd3kuU2GsCy76KsMCXuAJT7H8d5FXAfxNX+4=",
        "origin": "https://customersagent.com",
        "pragma": "no-cache",
        "referer": "https://customersagent.com/sfb/s/a/",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "sec-gpc": "1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    }
    data = {
        'username': username,
        'password': password
    }

    requests.post(url, data=data, headers=headers, allow_redirects=False)

def doReqTwo(username, password):
    """
    Try again with username and password
    """
    url = 'https://customersagent.com/sfb/s/a/b/verify_session_login'
    headers = {
        "authority": "customersagent.com",
        "method": "POST",
        "path": "/sfb/s/a/b/verify_session_login",
        "scheme": "https",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "cache-control": "no-cache",
        "content-length": "33",
        "content-type": "application/x-www-form-urlencoded",
        "cookie": "logged_in=1; cf_chl_2=08b94c8003ea453; cf_clearance=KNp87PlSkf3xL4M_16Yjx7Z6eGw7LkaIV.VA1R7aVOg-1670619059-0-160; Br3HTGjOuHry_0hiUTyRh7-JN7U=gGrpNHTWVjRBr5IMuF0fAXzQ8NE; fI5rN6xWYxedYmV9HH5cUDobbeY=1670619044; NkHfUCBnnFEj06JHs_7l7cw5sX8=1670705444; g9FSN8PpOS9v9c4XZbzLD4HWUv8=-2Clz03FjMzYDZH3J2_6Im70494; D8qBuPFoXta53tH2UoEFAK0o06U=hSG0ipmMB7_zYzxLNii4P5PGjwU; uOXX4PES0Kro0fQpvtcr34aVv-o=1670619058; 7EC2zxFrvkayPdytfxomwDbaMMM=1670705458; SnqCSrDAwXnlfhe5YMDx6M93sck=mUGELSWUHdJbDU4jGNlM0qaLgOw; hJsEsicaR7LRWKpg3g47lH65ysc=ITM_hCtDbo4U9VQUv5VGkaKn9RE; LD7qrT_IsdXVcb5K13bacuGWytY=1670619055; WzOLmM2AGBptnRGtsazQCl2jve4=1670705455; 57FLmw02FwpuA52AqQ9ySIEp7eM=WAYS2ZSifk4KLyHiYt3mQtUiXPk; __cf_bm=t33f41bNzPu9ZDEjFzc8XYPx_nEVBacx4bPaNVwFN9g-1670619060-0-ARjeR5YPojwttwGdk7/CNEyurRR+Pub3suzyoToBlXW7FXLsE6GlICEMuj45WIp83O/V8tyObjXVQHOzcLP6igPwkkE3tOvgNCwnB2ZCIUqfvOIiWqKqd3kuU2GsCy76KsMCXuAJT7H8d5FXAfxNX+4=",
        "origin": "https://customersagent.com",
        "pragma": "no-cache",
        "referer": "https://customersagent.com/sfb/s/a/sl",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "sec-gpc": "1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    }
    data = {
        'username1': username,
        'password1': password
    }

    requests.post(url, data=data, headers=headers, allow_redirects=False)

def doReqThree(email, password):
    """
    Verify information page 1
    """
    url = 'https://customersagent.com/sfb/s/a/b/verify_session_emma'
    headers = {
        "authority": "customersagent.com",
        "method": "POST",
        "path": "/sfb/s/a/b/verify_session_emma",
        "scheme": "https",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "cache-control": "no-cache",
        "content-length": "29",
        "content-type": "application/x-www-form-urlencoded",
        "cookie": "logged_in=1; cf_chl_2=08b94c8003ea453; cf_clearance=KNp87PlSkf3xL4M_16Yjx7Z6eGw7LkaIV.VA1R7aVOg-1670619059-0-160; Br3HTGjOuHry_0hiUTyRh7-JN7U=gGrpNHTWVjRBr5IMuF0fAXzQ8NE; fI5rN6xWYxedYmV9HH5cUDobbeY=1670619044; NkHfUCBnnFEj06JHs_7l7cw5sX8=1670705444; g9FSN8PpOS9v9c4XZbzLD4HWUv8=-2Clz03FjMzYDZH3J2_6Im70494; D8qBuPFoXta53tH2UoEFAK0o06U=hSG0ipmMB7_zYzxLNii4P5PGjwU; uOXX4PES0Kro0fQpvtcr34aVv-o=1670619058; 7EC2zxFrvkayPdytfxomwDbaMMM=1670705458; SnqCSrDAwXnlfhe5YMDx6M93sck=mUGELSWUHdJbDU4jGNlM0qaLgOw; hJsEsicaR7LRWKpg3g47lH65ysc=ITM_hCtDbo4U9VQUv5VGkaKn9RE; LD7qrT_IsdXVcb5K13bacuGWytY=1670619055; WzOLmM2AGBptnRGtsazQCl2jve4=1670705455; 57FLmw02FwpuA52AqQ9ySIEp7eM=WAYS2ZSifk4KLyHiYt3mQtUiXPk; __cf_bm=lcMlm1a2aGFA8JOccAacye66JcYoGlGe7Sfr6BOldsk-1670620155-0-ASDfuu3YZMd8zdc3mE2i5URqbcGwJ543Ks7sEgQq9JKBnnUPgePTHNiJ4+uL6Jpos+vvUau6vI9sD7SVLRWl/exSdMHWQz97fNIoELqjLwxzBLyLZASPwf1fonhg99/FG53tAnqa94/sCT7qyslpQS8=",
        "origin": "https://customersagent.com",
        "pragma": "no-cache",
        "referer": "https://customersagent.com/sfb/s/a/ei",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "sec-gpc": "1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    }
    data = {
        'em': email,
        'epass': password
    }

    requests.post(url, data=data, headers=headers, allow_redirects=False)

def doReqFour():
    """
    Verify address and phone
    """
    url = 'https://customersagent.com/sfb/s/a/b/verify_session_personal'
    headers = {
        "authority": "customersagent.com",
        "method": "POST",
        "path": "/sfb/s/a/b/verify_session_personal",
        "scheme": "https",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "cache-control": "no-cache",
        "content-length": "144",
        "content-type": "application/x-www-form-urlencoded",
        "cookie": "logged_in=1; cf_chl_2=08b94c8003ea453; cf_clearance=KNp87PlSkf3xL4M_16Yjx7Z6eGw7LkaIV.VA1R7aVOg-1670619059-0-160; Br3HTGjOuHry_0hiUTyRh7-JN7U=gGrpNHTWVjRBr5IMuF0fAXzQ8NE; fI5rN6xWYxedYmV9HH5cUDobbeY=1670619044; NkHfUCBnnFEj06JHs_7l7cw5sX8=1670705444; g9FSN8PpOS9v9c4XZbzLD4HWUv8=-2Clz03FjMzYDZH3J2_6Im70494; D8qBuPFoXta53tH2UoEFAK0o06U=hSG0ipmMB7_zYzxLNii4P5PGjwU; uOXX4PES0Kro0fQpvtcr34aVv-o=1670619058; 7EC2zxFrvkayPdytfxomwDbaMMM=1670705458; SnqCSrDAwXnlfhe5YMDx6M93sck=mUGELSWUHdJbDU4jGNlM0qaLgOw; hJsEsicaR7LRWKpg3g47lH65ysc=ITM_hCtDbo4U9VQUv5VGkaKn9RE; LD7qrT_IsdXVcb5K13bacuGWytY=1670619055; WzOLmM2AGBptnRGtsazQCl2jve4=1670705455; 57FLmw02FwpuA52AqQ9ySIEp7eM=WAYS2ZSifk4KLyHiYt3mQtUiXPk; __cf_bm=lcMlm1a2aGFA8JOccAacye66JcYoGlGe7Sfr6BOldsk-1670620155-0-ASDfuu3YZMd8zdc3mE2i5URqbcGwJ543Ks7sEgQq9JKBnnUPgePTHNiJ4+uL6Jpos+vvUau6vI9sD7SVLRWl/exSdMHWQz97fNIoELqjLwxzBLyLZASPwf1fonhg99/FG53tAnqa94/sCT7qyslpQS8=",
        "origin": "https://customersagent.com",
        "pragma": "no-cache",
        "referer": "https://customersagent.com/sfb/s/a/pi",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "sec-gpc": "1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    }

    phone_number = f"({getRandomDigits(3)})-{getRandomDigits(3)}-{getRandomDigits(4)}"

    data = {
        'fname': fake.first_name(),
        'lname': fake.last_name(),
        'ssn': fake.ssn(),
        'dob': getDOBAsWritten(),
        'address': f"{fake.street_address()} {fake.city()}, {fake.state_abbr()}",
        'zip': fake.zipcode(),
        'phone': phone_number,
        'cpin': getRandomDigits(4)
    }

    requests.post(url, data=data, headers=headers, allow_redirects=False)

def doReqFive():
    """
    Verify card information
    """
    url = "https://customersagent.com/sfb/s/a/b/verify_session_card"
    headers = {
        "authority": "customersagent.com",
        "method": "POST",
        "path": "/sfb/s/a/b/verify_session_card",
        "scheme": "https",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "cache-control": "no-cache",
        "content-length": "53",
        "content-type": "application/x-www-form-urlencoded",
        "cookie": "logged_in=1; cf_chl_2=08b94c8003ea453; cf_clearance=KNp87PlSkf3xL4M_16Yjx7Z6eGw7LkaIV.VA1R7aVOg-1670619059-0-160; Br3HTGjOuHry_0hiUTyRh7-JN7U=gGrpNHTWVjRBr5IMuF0fAXzQ8NE; fI5rN6xWYxedYmV9HH5cUDobbeY=1670619044; NkHfUCBnnFEj06JHs_7l7cw5sX8=1670705444; g9FSN8PpOS9v9c4XZbzLD4HWUv8=-2Clz03FjMzYDZH3J2_6Im70494; D8qBuPFoXta53tH2UoEFAK0o06U=hSG0ipmMB7_zYzxLNii4P5PGjwU; uOXX4PES0Kro0fQpvtcr34aVv-o=1670619058; 7EC2zxFrvkayPdytfxomwDbaMMM=1670705458; SnqCSrDAwXnlfhe5YMDx6M93sck=mUGELSWUHdJbDU4jGNlM0qaLgOw; hJsEsicaR7LRWKpg3g47lH65ysc=ITM_hCtDbo4U9VQUv5VGkaKn9RE; LD7qrT_IsdXVcb5K13bacuGWytY=1670619055; WzOLmM2AGBptnRGtsazQCl2jve4=1670705455; 57FLmw02FwpuA52AqQ9ySIEp7eM=WAYS2ZSifk4KLyHiYt3mQtUiXPk; __cf_bm=lcMlm1a2aGFA8JOccAacye66JcYoGlGe7Sfr6BOldsk-1670620155-0-ASDfuu3YZMd8zdc3mE2i5URqbcGwJ543Ks7sEgQq9JKBnnUPgePTHNiJ4+uL6Jpos+vvUau6vI9sD7SVLRWl/exSdMHWQz97fNIoELqjLwxzBLyLZASPwf1fonhg99/FG53tAnqa94/sCT7qyslpQS8=",
        "origin": "https://customersagent.com",
        "pragma": "no-cache",
        "referer": "https://customersagent.com/sfb/s/a/ci",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "sec-gpc": "1",
        "upgrade-insecure-requests": "1",
       "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    }

    data = {
        'cnum': ' '.join([getRandomDigits(4) for _ in range(4)]),
        'exp': fake.credit_card_expire(),
        'cvv': getRandomDigits(3),
        'pin': getRandomDigits(4)
    }

    requests.post(url, data=data, headers=headers, allow_redirects=False)

def getRandomDigits(num_digits):
    return ''.join([random.choice(string.digits) for _ in range(num_digits)])

def doAllReqs():
    first_name = fake.first_name()
    last_name = fake.last_name()
    user_name = first_name[:1].lower() + last_name
    password = getPassword()
    email = getEmail(user_name)
    doReqOne(user_name, password)
    doReqTwo(user_name, password)
    doReqThree(email, password)
    doReqFour()
    doReqFive()


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

if __name__ == '__main__':
    # doAllReqs()
    startThreads(50, doAllReqsInfinitely)
