import requests, multiprocessing

urls = [
    'http://www.heroku.com',
    'http://python-tablib.org',
    'http://httpbin.org',
    'http://python-requests.org',
    'http://kennethreitz.com'
]
p = multiprocessing.Pool(5)
print(p.map(requests.get, urls))
