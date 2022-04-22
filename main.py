import praw

reddit = praw.Reddit(
    client_id="uC-tW8fNIAoST-Du5KVXgw",
    client_secret="ViRjfin43izo86xOLc9ppCspQmJ5aQ",
    user_agent="CaffeineAgent",
    username="CaffeineVL",
    password="vb!7!9xu",
    check_for_async=False
)

import random
import time
def karma():
    try:
        messages = ["I upvoted your post! Can you also upvote mine?", "Upvoted! Please upvote my posts as well!", "Upvoted you. Care to share?"]
        for submission in reddit.subreddit("FreeKarma4U+FreeKarma4You").stream.submissions():
            submission.upvote()
            rand = random.randint(0,(len(messages)-1))
            print(submission.title)
            submission.reply(messages[rand])
            time.sleep(30)
        except:
            time.sleep(300)
            karma()
    karma()
