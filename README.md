# This library no longer works.
The STM discontinued the xml data feed that was used by this library in favor of an [API](https://www.stm.info/en/about/developers).
I currently am not planning of updating the library to use the new API.

# stm-metro-client [![Build Status](https://api.travis-ci.org/kkr16/stm-metro-client.svg?branch=master)](https://travis-ci.org/kkr16/stm-metro-client) [![PyPI version](https://badge.fury.io/py/stm-metro-client.svg)](https://badge.fury.io/py/stm-metro-client)


A python client for the Montreal STM Metro line status.

I created this library to feed data to sensors for STM line status in my HomeAssistant based home automation setup.

Data is provided by the STM through a public xml feed found at http://www2.stm.info/1997/alertesmetro/esm.xml

DISCLAIMER: I am not affiliated to the STM, and bear no responsibility to the data provided by this library/API.

Install using pip:

pip3 install stm-metro-client

