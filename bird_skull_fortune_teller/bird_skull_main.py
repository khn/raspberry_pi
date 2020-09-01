import fortun_teller
import click

bird = fortun_teller.Head()


while True:
    x = click.getchar()
    print("Key Pressed " + str(x))
    if x == "r":
        bird.move("right", "fast")
    elif x == "l":
        bird.move("left", "fast")
    elif x == "u":
        bird.move("up", "fast")
    # keyboard shortcuts
    elif x == "a": # left
        bird.move("turnl",200)
    elif x == "d": # right
        bird.move("turnr",200)
    elif x == "w": # up
        bird.move("up",200)
    elif x == "s": # Down
        bird.move("down",200)
    elif x == "e": # tilt right
        bird.move("tiltr",200)
    elif x == "q": # tilt left
        bird.move("tiltl",200)
    elif x == ",": # Center
        bird.move("centerlr",180)
    elif x == ".": # Center
        bird.move("centerud",180)
    elif x == "x": # Center
        bird.move("center",150)
    elif x == "1": # Quit to terminal
        bird.close()
        break
    else:
        bird.move("error", "fast")
