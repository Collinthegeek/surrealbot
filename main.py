import os, random, moviepy, shutil
from InstagramAPI import InstagramAPI

insta = InstagramAPI('username', 'password')
insta.login()

file = random.choice([x for x in os.listdir("images/surreal") if os.path.isfile(os.path.join("images/surreal", x))])
caption = random.choice(open("/usr/share/dict/words").readlines())
photo = "images/surreal/" + file

insta.uploadPhoto(photo, caption=caption)

shutil.move(photo, 'images/surreal/used')
