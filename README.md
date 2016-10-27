# Spookyboo Mote Light Show

This project is for halloween 2016 using the [Pimoroni Mote light strips](https://shop.pimoroni.com/products/mote) to create a little light show in my window. This project also using Tweepy to scan for a keyword and then the Mote will change animation

## What do you need launcher scripts

- [Mote from Pimoroni](https://shop.pimoroni.com/products/mote)
- Raspberry Pi (and normal accessories)
- Scary cut out of bats and witches for your window

## Dependances 

- Tweepy
- [Mote library for Raspberry Pi](https://github.com/pimoroni/mote)
- Twitter API keys

## How to use

Place the Mote sticks on your window (works best if you have blinds). It's worth noting that you place the sticks in order.

Turn on your pi and make sure the date and time is correct then use the config_template.py to make a new file called config.py. Here you should put in your twitter API keys.

Run the script : irbufw on your Raspberry Pi so it runs in the background. (I prefer using the screen command.)

Then goto twitter send the hashtag '#spookyboo' and watch the animation!

## Videos

- [Vine: Testing the brightness](https://vine.co/v/5wQLuKn3i7O)
- [Vine: Testing tweepy and animations](https://vine.co/v/5dzaJvHleIO)
