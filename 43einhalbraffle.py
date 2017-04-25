import requests
from random import getrandbits
url = 'http://www.43einhalb.com/blog/adidas-originals-yeezy-boost-350-v2-blackred-raffle/2017/02/'

headers = {'User-Agent':
           'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

#Fill in Your Shit
def main(limit):
    for i in range(1, limit):
        num = getrandbits(40)
        email = 'davidmei6767@+{}@gmail.com'.format(num)
        title = 'Mr.' #doesn't matter
        name = ' David{}'.format(num) #first name
        surname = 'Mei{}'.format(num) #last name
        size = '9' #Enter Your Size Please Don't take my 9
        shipping = 'Shipping' #Don't Touch
        payload = {
            'action': 'contest',
            'title': title,
            'name': name,
            'surname': surname,
            'email': email,
            'size': size,
            'shipping': shipping,
        }
        resp = requests.post(url, data=payload, headers=headers)
        print('{}/{} registered.'.format(i, limit))

if __name__ == "__main__":
    main(10000)
            
            
            
