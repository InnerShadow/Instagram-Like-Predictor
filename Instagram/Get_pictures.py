from Data.data import *
import requests

import requests


def get_profile_photos(username):

    try:
        response = requests.get("https://scontent-ams2-1.cdninstagram.com/v/t51.2885-15/378529962_323115053710997_2419006730114321070_n.webp?stp=dst-jpg_e35&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_cat=105&_nc_ohc=Ny4QvcR2i4cAX9kHcvX&edm=ACWDqb8BAAAA&ccb=7-5&ig_cache_key=MzE5MzcyNjAwNzY4ODA0NDU5OQ%3D%3D.2-ccb7-5&oh=00_AfAgscOlYlMOgbu7_ZLO36OPTwnR4eT6-9EkhiNe551g7Q&oe=651DC4ED&_nc_sid=ee9879")

        with open('re.png', 'wb') as f:
            f.write(response.content)

        print("^)")
        return
    except Exception:
        return

