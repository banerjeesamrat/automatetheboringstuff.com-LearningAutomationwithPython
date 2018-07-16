
"""

Author: Samrat Banerjee
Dated: 16/07/2018
Description: Using an Assertion in a Traffic Light Simulation

"""

market_2nd = {'ns': 'green', 'ew': 'red'}   # market street and 2nd street, ns is north-south
mission_16th = {'ns': 'red', 'ew': 'green'} #mission street and 16th street, ew is east-west

def switchLights(stoplight):
    for key in stoplight.keys():
        if stoplight[key]=='green':
            stoplight[key]='yellow'
        elif stoplight[key]=='yellow':
            stoplight[key]='red'
        elif stoplight[key]=='red':
            stoplight[key]='green'
        assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight)

switchLights(market_2nd)
