"""
Created on Apr 20, 2015
Updated on April 24, 2017

@author: Dario Bonino
@author: Luigi De Russis

Copyright (c) 2015-2017 Dario Bonino and Luigi De Russis
 
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0
 
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License
"""

import math
from hue_api import HueBridge


def compute_hue(value, max_value):
    hue_red = 65535
    hue_green = 25500
    
    # compute the right parameters needed to convert the given numeric value to the right hue value
    ratio = 1
    if max_value > 0:
        ratio = min(1, value / max_value) 
    # compute the current hue
    return int(math.floor(hue_green + (hue_red - hue_green) * ratio))


def main():
    # the Hue bridge id
    bridge = HueBridge("http://192.168.0.201/api/1jlyVie2nvwtNwl0hv8KdZOO0okdvNcIIdPXWsdX")
    # we want to change the hue value of this lamp
    lamp_id = 1
    
    # init the string to ask user for
    string = ""
    while string != 'exit':
        # get the next input
        string = input("Insert a number between 0 and 255 (or type 'exit'):\n> ")
        
        # if the given string is "exit" interrupt the loop and say goodbye
        if string == 'exit':
            print('Goodbye!')
        else:
            try:
                # get the requested hue
                req_hue = int(string)
                # compute the actual hue
                hue = compute_hue(req_hue, 255.0)
                # debug
                print('Hue: {}'.format(hue))
                # set the hue to the given lamp
                bridge.set_hue(lamp_id, hue)
            except:
                pass
    

if __name__ == '__main__':
    main()
