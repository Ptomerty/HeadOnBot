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
            for comment in reddit.redditor('headonbot_').comments.new(limit=None):
                if comment.score <= int(-2):
                    comment.delete()
                    print("deleted bad comment")
        except Exception as e:
            print(e)

if __name__ == '__main__':
    main()
