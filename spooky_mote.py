#!/usr/bin/env python


import sys, subprocess, urllib, time, tweepy, json, datetime
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import config

import time
from colorsys import hsv_to_rgb
import math
from mote import Mote

import threading

print("""Rainbow

Press Ctrl+C to exit.
""")

mote = Mote()

mote.configure_channel(1, 16, False)
mote.configure_channel(2, 16, False)
mote.configure_channel(3, 16, False)
mote.configure_channel(4, 16, False)

status = 1

def single(strip, led):
        i = 0
        while i < 6:
                i = i + 1
                time.sleep(0.03)
                mote.clear()
                mote.set_pixel(strip, led, 255, 255, 255)
                mote.show()
                time.sleep(0.03)
                mote.set_pixel(strip, led, 0, 0, 0)
                mote.show()

def flash():
        i = 0
        while i < 6:
                i = i + 1
                time.sleep(0.03)
                mote.clear()
                for channel in range(1, 5):
                        for pixel in range(16):
                                mote.set_pixel(channel, pixel, 255, 255, 255)
                mote.show()
                time.sleep(0.03)
                for channel in range(1, 5):
                        for pixel in range(16):
                                mote.set_pixel(channel, pixel, 0, 0, 0)
                mote.show()

def fadered():
        red = 0
        while red < 255:
                red = red + 10
                mote.clear()
                for channel in range(1, 5):
                        for pixel in range(16):
                                mote.set_pixel(channel, pixel, red, 0, 0)
                mote.show()
                time.sleep(0.1)

def idle():
	try:
    		while True:
        		t = time.time()
        		for channel in range(4):
            			for pixel in range(16):
                			#hue = (h + (channel * 64) + (pixel * 4)) % 60
					hue = 15 + (math.sin(t) * 15)
					r, g, b = [int(c * 255) for c in hsv_to_rgb(hue/360.0, 1.0, 1.0)]
                			mote.set_pixel(channel + 1, pixel, r, g, b)
        		mote.show()
       			time.sleep(0.01)
			global status
			while status == 2:
				time.sleep(0.01)

	except KeyboardInterrupt:
    		mote.clear()
    		mote.show()


def replywithpic(tweetdata):
        msg = "@%s OoOoOoOoOoOoOo You ain't afraid of ghost.. are you?     %s" % (tweetdata['username'], tweetdata['date'])
        file = 'spooky.jpg'
        if len(msg) <= 140:
                api.update_with_media(file, status=msg, in_reply_to_status_id=tweetdata['tweetId'])
        else:
                print "tweet not sent. Too long. 140 chars Max."

def parsetweet(tweet):
        tweetId = tweet['id']
        username = tweet['user']['screen_name'].encode('utf-8')
        now = datetime.datetime.now()
        date = now.strftime("%H:%M:%S %d-%m-%Y")
        text = tweet['text'].encode('utf-8')
        tweetdata = {'tweetId': tweetId, 'username': username, 'date': date, 'text': text};
        return tweetdata

class StdOutListener(StreamListener):
        def on_data(self, data):
		global status
                tweet = json.loads(data)
                # Print Usernam[Be
                print(tweet['user']['name']).encode('utf-8')
                # Print Text from tweet *note* encode is used because of speical charaters causing exception
                print(tweet['text']).encode('utf-8')
                # ----- do something
                tweetdata = parsetweet(tweet)
                if "#spookyboo" in tweetdata['text']:
                	status = 2
			replywithpic(tweetdata)
			flash()
			single(1,5)
			single(4,15)
			single(2,3)
			single(3,9)
			single(1,1)
			single(3,15)
			single(2,0)
			single(4,4)
			flash()
			fadered()
			flash()
			status = 1
                return True

        def on_error(self, status):
                # Print errors numbers
                if status == '403':
                        print('User forcing duplication:  %s' % status)
                else:
                        print(status)

if __name__ == '__main__':
        # OAuth to Twitter
        l = StdOutListener()
        auth = OAuthHandler(config.consumer_key, config.consumer_secret)
        auth.secure = True
        auth.set_access_token(config.access_token, config.access_token_secret)
        api = tweepy.API(auth)

	idle = threading.Thread(target=idle)
	idle.start()

        # Start Stream Tracking
        stream = Stream(auth, l)
        #user = ["robinjamberlin"]
        keywords = ["#spookyboo"]
        stream.filter(track=keywords)
