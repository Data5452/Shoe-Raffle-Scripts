import requests
from random import getrandbits
url = 'https://www.ymeuniverse.com/en/blog/2017/04/21/yeezy-boost-350-v2-cream-white/'

headers = {'User-Agent':
           'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

#CHANGE the fields as the comments say  
def main(limit):
    for i in range(1, limit):
        email = 'davidmei6767+{}@gmail.com'.format(getrandbits(40)) # CHANGE YOUR_EMAIL to your email prefix. don't change the +{} after.
        Name = 'David Mei' #first and last name here
        Shoe_Size = '8.5' #UK sizing find out and fill like this 9 or 9.5
        Enter_City = 'Medford' #city you live in
        payload = {

            'action': 'contest',
            'Name' : Name,
            'Email' : email,
            'Shoe_Size' : Shoe_Size,
            'Enter_City' : Enter_City

            }
        resp = requests.post(url, data=payload, headers=headers)
        print('{}/{} registered.'.format(i, limit))

if __name__ == "__main__":
    main(10000)
