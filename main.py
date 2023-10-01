import requests
from PIL import Image
from io import BytesIO
from Instagram.Get_pictures import *

def __main__():
    username = "_asha.n"
    get_profile_photos(username)

    # for index, url in enumerate(photo_urls, start = 1):
    #     response = requests.get(url)
    #     img = Image.open(BytesIO(response.content))
    #     img.show()
    #     i = input("AAA: ")


if __name__ == "__main__":
    __main__()

