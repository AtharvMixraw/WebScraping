This script is a basic example of handling HTTP and URL errors when trying to fetch the HTML content of a website. It also demonstrates the use of SSL to ensure secure connections.

import certifi
import ssl
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
ssl_context = ssl.create_default_context(cafile=certifi.where())

''' ssl stands for secure socket layer. Here, an SSL context is created using the ssl.create_default_context() function, 
and the certifi.where() function is used to set the location of the CA file. This helps ensure secure connections, especially when working with HTTPS. '''

try:
    html = urlopen('https://pythonscrapingthisurldoesnotexist.com')
except HTTPError as e:
    print(e)
except URLError as e:
    print('The server could not be found!')
else:
    print('It worked')
