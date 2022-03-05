import requests

# 200 taken
# 404 available

users = open('usernames.txt', 'r')
readusers = users.read().splitlines()
for line in  readusers:

    r = requests.get(f'https://www.snapchat.com/add/{line}')
    if r.status_code == 200: # taken users
        print(f"{r.status_code}\t{line} is taken")

    elif r.status_code == 404: # available users
        print(f"{r.status_code}\t{line} is available")
        with open('available.txt', 'a', encoding='utf-8') as save:
            save.write(line + "\n")
            save.close()
    else: # usernames that were not checked
        print(f"{r.status_code}\tyou are being rate limited!")
        with open('error.txt', 'a', encoding='utf-8') as error:
            error.write(line + "\n")
            error.close()
print(" DONE! ")
close = input("press enter to close!")
exit()
