# Hue Lights control in Python

This repository contains basic scripts for testing the Philips Hue APIs from Python. The available files include:

* `rest.py` an helper for easily sending request to a given API endpoint with a specific payload, and using a given HTTP verb
* `hue.py` a simple application for the Philips Hue API that turns all the available lamps on, in color-loop mode
* `hue_api.py` a basic Philips Hue library to be extended at will
* `hue_api_test.py` a simple test script that uses the `hue_api.py` module

_Please, notice that the `username` present in the code is provided as an example, and it is expected not to work._