import PuppetMaster
import click
<<<<<<< HEAD
import pygame
=======
import random
>>>>>>> 2d527bb5f39db7c55af5c0ff6da98762adfb6aaa

bird = PuppetMaster.PuppetMaster()


while True:
    print("Total number of fortunes to choose from - " + str(bird.number_of_fortunes()))
    x = click.getchar()
    rand = random.randint(1, 20)
    if x == "q":
        break
    try:
        if 1 <= int(x) <= bird.number_of_fortunes():
            bird.play_fortune(int(x))
        else:
            print("Please choose a number between 1 and " + str(bird.number_of_fortunes()))
    except Exception as e:
        print("Try again dumb dumb " + str(e))
    finally:
        print("Random Number - " + str(rand))