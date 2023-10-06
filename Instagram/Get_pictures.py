from Data.data import *

import sys
import subprocess as sp

def get_profile_photos(username):

    cmd = ' '.join(
        [
            f'python3 -m instaloader {username}'
        ]
    )

    pipe = sp.Popen(cmd, shell = True)

    _ = pipe.communicate()

    if pipe.returncode != 0:
        print('Error!!!')
        sys.exit(1)

    print('Success!!!')

