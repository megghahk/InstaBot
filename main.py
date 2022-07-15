from time import sleep

from instabot import Bot

my_bot = Bot()

# to login to our account
my_bot.login(username='meegghaaaa', password='******')
sleep(10)

# to follow an user
my_bot.follow('deepikapadukone')
sleep(20)

# to follow multiple users
my_bot.follow_users(['python.hub', 'python.learning', 'python.coder_'])
sleep(20)

# to unfollow
my_bot.unfollow_non_followers()

# to add a picture
# my_bot.upload_photo("image_link",caption = "my life my rules")
sleep(40)

# send message to user
my_bot.send_message("HELLO!!", '_veena_r')
sleep(100)

# like a post
my_bot.like_user('_veena_r', amount=2,filtration=False)
sleep(20)

# comment
user_id = my_bot.get_user_id_from_username('_veena_r')
media_id = my_bot.get_last_user_medias(user_id , 1 )
my_bot.comment(media_id[0], "Nyc")
sleep(20)

# get list of followers of anyone
followers_list = my_bot.get_user_followers('_veena_r')

following_list = my_bot.get_user_following('_veena_r')

for count,each_follower in enumerate(followers_list):
    if count > 4:
        continue
    sleep(6)
    print(my_bot.get_username_from_user_id(each_follower))

my_bot.logout()
