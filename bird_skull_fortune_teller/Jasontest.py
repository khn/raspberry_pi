import json
import maestro
import time

# Opening JSON file
with open('fortunes.json') as json_file:
    data = json.load(json_file)

for scene in data.values():
    for splort in range(len(scene)):
        if 1 == scene[splort]['fort_num']:
            print("How many fortunes total " + str(len(scene)))
            print("Fortune Name " + scene[splort]['fort_name'])

            for this in scene[splort]['animate']:
                print("Sequence " + str(this['SEQ']))
                for seq in this['set_pos']:
                    print("  Channel - " + str(seq['channel']))
                    print("    Accel - " + str(seq['acceleration']))
                    print("    Speed - " + str(seq['speed']))
                    print("    Position - " + str(seq['position']))
                print("Wait time " + str(this['wait']))


class Tempest:

    def __init__(self):
        pass

