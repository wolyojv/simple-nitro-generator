import requests
import random
import string

status = True


def url_generator():
    url = 'https://discord.gift/' + ''.join(
        random.choice(string.ascii_uppercase + string.digits +
                      string.ascii_lowercase) for x in range(19))
    return url


print(url_generator())


def check(link):
    url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + link + "?with_application=false&with_subscription_plan=true"
    req = requests.get(url)
    if req.status_code == 200:
        print("Valid Nitro --> {}".format(link))
        with open("nitro/valids.txt", "a") as dosya:
            dosya.write("{} \n".format(link))
    else:
      print("İnvalid Nitro --> {}".format(link))
      with open("nitro/invalids.txt","a") as dosya:
        dosya.write("{} \n".format(link))

while status:
  check(url_generator())
