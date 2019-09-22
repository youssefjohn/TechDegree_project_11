import json



#
#
#
#
#
# def loadjsonfile(filename):
#     results = {}
#
#
#     with open(filename)
#
#
#






with open('details.json') as jfile:
    file = json.load(jfile)
    for thing in file:
        print(thing)


