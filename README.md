## What?

Automatically check application status for Canadian study permit. 

## Why? 

Frustration, that's why.

## Requirements:

- Python 2
- virtualenv (`sudo pip install virtualenv`)
- wget

- firefox (if you are a sadist and want to watch these screens slowly
  automatically get clicked by a robot) (or if you want to actually look at the
  website after the script is done)

(Tested on Ubuntu. 16.04. Hit me up if you have a sort of a similar system and
have problems. Otherwise, you're on your own)

## Your credentials:

Update the `data = { }` dictionary in `status.py` with your credentials.

Apologies for not maintaining config separately. Too sleepy.

## Usage:

`./checkstatus.sh`

(or for firefox):

`./checkstatus.sh geckodriver`

## Sample:

```
... gibberish ...

Logging in...
Pressed continue...
Pressed I agree...
Answering question...
Getting status...
Application 0 from May 12, 2017  06:25:12 a.m. EDT: status Refused. (messages: Read)
Application 1 from June 8, 2017  09:09:07 a.m. EDT: status Submitted. (messages: Read)

```

## TODO

- Andeoid notifications. (of course, I'm kidding!) 

## Credits

Inspiration from the ultimate mundane project by Karapudi:
https://github.com/kirankaranth1/ApplicationStatusFetcher
