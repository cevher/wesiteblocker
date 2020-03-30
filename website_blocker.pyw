import time
from datetime import datetime as dt 

hosts_temp = "hosts"
# "/etc/hosts" for linux and mac
hosts_path = "C:\Windows\System32\drivers\etc\hosts"
redirect ="127.0.0.1"

# th list of websites to be blocked by the app
websites_to_block = ['www.facebook.com', "facebook.com", "youtube.com", "www.youtube.com"]

while True:
    if dt(dt.now().year,dt.now().month, dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month, dt.now().day,20):
        print("Working hour...")
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in websites_to_block:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        with(hosts_path, 'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websites_to_block):
                    file.write(line)
            file.truncate()
        print("Fun hours...")
    time.sleep(5)
