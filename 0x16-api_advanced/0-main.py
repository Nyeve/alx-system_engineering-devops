#!/usr/bin/python3
"""
import sys

if __name__ == '__main__':
    number_of_subsribers= __import__('0-subs').number_of_subscribers
    if len(sys.argv) < 2:
        print("Please oass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
