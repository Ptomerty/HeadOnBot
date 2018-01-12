import praw
import praw.exceptions
import re
import time

def main():
    message = '[Apply directly to the forehead!](https://www.youtube.com/watch?v=f_SwD7RveNE)'

    reddit = praw.Reddit('HeadOnBot', user_agent='HeadOnBot the return')
    print('reddit client launched')

    while True:
        try:
            for comment in reddit.subreddit('all').stream.comments():
                match = re.search(r'\bhead on\b', comment.body, re.IGNORECASE)
                if match:
                    print("head on found")
                    try:
                        comment.reply(message)
                        print("replied")
                    except praw.exceptions.APIException:
                        time.sleep(60 * 10)  # ratelimit hit
                    except Exception as e:
                        print(e)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    main()
