# nearestATMs

**NearestATMs** is a Telegram bot, fot get a list of the nearest ATMs, 
taking into account the location of the user.

## Details

Telegram bot, build using Python.

For the moment, only take in account the ATMs situated in 
[*Autonomous City of Buenos Aires (CABA) - Argentina*](https://en.wikipedia.org/wiki/Buenos_Aires).

You can use this bot [here](https://t.me/nearest_ATMs_bot).

### Demo

<p align="center">
<img src="./resources/demo.gif" width="270" alt="demo">
</p>

## Requirements

* Python >=3.6

## Installation

* Clone this repo
* It's recommended create and activate a virtual environment
* `make init`
* Register a new bot in Telegram, you can doit using [BotFather](http://t.me/BotFather). 
This will give you a token that identify your bot, put that token value in the setting TOKEN in [settings.py](nearest_atms/settings.py)
* `make install`

## Run

* `make run` Whit this, a server for the bot will be up and running.
* Now you can go to Telegram, to the chat with you new bot, that you registered in installation step, and start using it.

## Using

In Argentina, the ATMs are mainly on two networks: *Link* y *Banelco*. 
You can define which of this networks you want to search.

* **/link** get up to 3 ATMs nearest, of the link network
* **/banelco** get up to 3 ATMs nearest, of the banelco network

## Test

Run the unit tests with: `make test`

## TODO

* [x] The commands must be case-insensitive
* [x] ATMs must be listed less than 500m away from the user (distance
geographical direct to the user, without considering streets)
* [x] A maximum of 3 ATMs must be listed
* [x] Each ATM must indicate its address and its respective bank
* [ ] The search algorithm for nearby ATMs must implement a solution
better than linear in the average case
* [ ] Interactive map, with the points of the ATMs and the person
* Tests
  * [ ] Command case-insensitive
  * [ ] Integration tests
* [ ] Deploy in a server, could be in GCP.
