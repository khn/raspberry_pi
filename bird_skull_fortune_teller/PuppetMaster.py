import json
import maestro_uart
import time
# import pygame


class PuppetMaster:
    """Class controls all aspects of animitronic movement. It will parse a JSON file that contains all
    info regaurding a given set of fortunes. (Specified in the _init_ right now but might be passed in
    as an argument at some point.) It will play sounds, move servos, control the timing of each movement
    and will have a public method for returning how many total fortunes there are. The 'puppeteer' method
    might need to be broken out into its own class at some point. I'm either going to delete the print
    statements or wrap them up as debugging messages."""

    def __init__(self):
        # Load in JSON file and parse it into an object
        self.servo_controller = maestro_uart.MaestroUART()
        with open('fortunes.json') as json_file:
            self.script = json.load(json_file)
        # Initialize pygame to play sounds
        # pygame.init()

    def number_of_fortunes(self):
        # Returns the total number of fortunes in the JSON file.
        for fortune_list in self.script.values():
            print("How many fortunes total " + str(len(fortune_list)))
            return len(fortune_list)

    def play_fortune(self, fortune_num):
        """The JSON file referenced has several nested structures. Some are converted to dictionaries, some lists."""
        # Open lists of fortunes. (Outer most structure that holds a list of the possible fortunes)
        for fortune_list in self.script.values():
            # Loops through all the fortunes in the LIST
            for fortune in range(len(fortune_list)):
                # Finds the fortune DICTIONARY we're looking for.
                if fortune_num == fortune_list[fortune]['fort_num']:
                    # At this level we have access to fortune number, fortune name and the path to the sound file.
                    print("Fortune Name " + fortune_list[fortune]['fort_name'])
                    # Loads sound file (pulled from JSON) and begins play.
                    # pygame.mixer.music.load(str(fortune_list[fortune]['sound_file']))
                    # Play once
                    # pygame.mixer.music.play()
                    # Loops through LIST each sequence or movement set, of the full animation.
                    for step in fortune_list[fortune]['animate']:
                        # Access to the sequence number of the animation
                        print("Sequence " + str(step['SEQ']))
                        # and a LIST of DICTIONARY entries that sets each of the servos
                        for seq in step['set_pos']:
                            # Access to the DICTIONARY that has all the info for the servo
                            self.__puppeteer(seq['channel'], seq['acceleration'], seq['speed'], seq['position'])
                            print("  Channel - " + str(seq['channel']))
                            print("    Accel - " + str(seq['acceleration']))
                            print("    Speed - " + str(seq['speed']))
                            print("    Position - " + str(seq['position']))
                        time.sleep(float(step['wait']))
                        print("Wait time " + str(float(step['wait'])))
                        # Wait time until moving on to the next step

    def __puppeteer(self, channel, accel, speed, position):
        # Sends the movement commands using the maestro library.
        # This might turn into its own class so that this object won't care what controller library we're using.
        # pass
        self.servo_controller.set_acceleration(channel, accel)
        self.servo_controller.set_speed(channel, speed)
        self.servo_controller.set_target(channel, position)


