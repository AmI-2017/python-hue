"""
Created on Apr 15, 2014
Updated on April 20, 2016

@author: Dario Bonino
@author: Luigi De Russis

Copyright (c) 2014-2016 Dario Bonino and Luigi De Russis
 
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

import rest


class HueBridge:
    """
    A class representing a Philips Hue bridge
    """
    def __init__(self, url):
        
        # remove trailing slashes
        if url[-1] == '/':
            url = url[:-1]
        
        # store the base API URL
        self.url = url
        
        # build the lights URL
        self.lights_url = self.url+"/lights"
        
    def get_all_lights(self):
        """
        Provide a dictionary of all available lamps and capabilities
        """
        return rest.send(url=self.lights_url)

    def turn_all_off(self):
        """
        Turn all the lights off
        """
        # get all lights
        all_lights = self.get_all_lights()
        for light in all_lights:
            url_to_call = self.lights_url+'/'+light+'/state'
            # prepare the "turn off" request
            body = '{ "on": false }'
            rest.send('PUT', url_to_call, body, {'Content-Type': 'application/json'})

    def change_light_state(self, light_id, state):
        """
        Turn a given lamp on or off
        :param light_id: the light to act on
        :param state: the "on" or "off" string
        """
        # compose the specific light URL
        url_to_call = self.lights_url + '/' + str(light_id) + '/state'
        # set the given on/off value
        if state == 'on':
            state = 'true'
        else:
            state = 'false'
        body = '{{ "on" : {} }}'.format(state)
        # send the request
        rest.send('PUT', url_to_call, body, {'Content-Type': 'application/json'})

    def set_hue(self, light_id, hue):
        """
        Change the hue value of a given light
        :param light_id: the id of the light to control
        :param hue: the hue value to set
        """
        # compose the specific light URL
        url_to_call = self.lights_url+'/'+str(light_id)+'/state'
        # set the given hue value
        body = '{{ "on" : true, "hue" : {} }}'.format(hue)
        # send the request
        rest.send('PUT', url_to_call, body, {'Content-Type': 'application/json'})
