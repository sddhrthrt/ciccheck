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

Update the `data = { }` dictionary with your credentials.

## Usage:

`./checkstatus.sh`

(or for firefox):

`./checkstatus.sh geckodriver`
