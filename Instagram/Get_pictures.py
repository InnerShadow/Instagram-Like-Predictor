import instaloader

def get_profile_photos(username):
    L = instaloader.Instaloader()

    profile = instaloader.Profile.from_username(L.context, username)
    postas = L.get_feed_posts() #Do it later
    photo_urls = []

    for post in profile.get_posts():
        photo_urls.append(post.mediacount)

    return photo_urls



    