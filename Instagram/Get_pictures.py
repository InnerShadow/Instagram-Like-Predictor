import sys
import subprocess as sp

def get_profile_photos(username):

    folfer = f"Data/Training_Data/{username}"

    cmd = ' '.join(
        [
            f'python3 -m instaloader {username} --dirname-pattern {folfer}'
        ]
    )

    pipe = sp.Popen(cmd, shell = True)

    _ = pipe.communicate()

    if pipe.returncode != 0:
        print('Error!!!')
        sys.exit(1)

    print('Success!!!')

