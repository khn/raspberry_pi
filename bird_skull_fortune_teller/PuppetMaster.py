import json
import maestro
import time


class PuppetMaster:
    """Class controls all aspects of animitronic movement. It will parse a JSON file that contains all
    info regaurding a given set of fortunes. (Specified in the _init_ right now but might be passed in
    as an argument at some point.) It will play sounds, move servos, control the timing of each movement
    and will have a public method for returning how many total fortunes there are. The 'puppeteer' method
    might need to be broken out into its own class at some point"""

    with open('fortunes.json') as json_file:
        script = json.load(json_file)
    # Create maestro controller object (Might be abstracted to another class at some point)
    self.xys = maestro.Controller()

    def __init__(self):
        # Load in JSON file and parse it into an object


    def number_of_forutnes(self):
        for fortunes in self.script.values():
            print("How many fortunes total " + str(len(fortunes)))
            return len(fortunes)

    def play_fortune(self, fortune_num):

        for fortunes in self.script.values():
            for scenes in range(len(fortunes)):
                if fortune_num == fortunes[scenes]['fort_num']:
                    print("How many fortunes total " + str(len(fortunes)))
                    print("Fortune Name " + fortunes[scenes]['fort_name'])

                    for step in fortunes[scenes]['animate']:
                        print("Sequence " + str(step['SEQ']))
                        for seq in this['set_pos']:
                            print("  Channel - " + str(seq['channel']))
                            print("    Accel - " + str(seq['acceleration']))
                            print("    Speed - " + str(seq['speed']))
                            print("    Position - " + str(seq['position']))
                        print("Wait time " + str(step['wait']))
        pass

    def __puppeteer(self, accel, speed, position):
        # This might turn into its own class so that this object won't care what controller library we're using.

        pass

