import fortun_teller

bird = fortun_teller.Head()


while True:
    x = input('Where would you like me to go? ')
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
