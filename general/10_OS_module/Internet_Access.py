"""There are a number of modules for accessing the internet and processing internet protocols. 
Two of the simplest are 
urllib.request for retrieving data from URLs and 
smtplib for sending mail:"""
from urllib.request import urlopen
import urllib.error

url = 'http://worldtimeapi.org/api/timezone/etc/UTC.txt'  # Include the scheme (http or https)
try:
    with urlopen(url) as response:
        # Read the content of the response
        html = response.read()
        
        # Decode the content to a string
        html_str = html.decode('utf-8')
        
        # Print the content
        print(html_str)
except urllib.error.URLError as e:
    print(f"Failed to fetch URL: {e.reason}")
except urllib.error.HTTPError as e:
    print(f"HTTP error: {e.code} {e.reason}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")