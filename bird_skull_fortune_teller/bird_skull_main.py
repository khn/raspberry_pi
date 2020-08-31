import fortun_teller
import click

bird = fortun_teller.Head()


while True:
    print("Ready to move the head")
    x = click.getchar()
    print(str(x))
    if x == "r":
        bird.move("right", "fast")
    if x == "l":
        bird.move("left", "fast")
    if x == "u":
        bird.move("up", "fast")
    if x == "d":
        bird.move("down","fast")
    if x == "q":
        bird.close()
        break
