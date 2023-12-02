#!/bin/bash

# Make a request that causes the server to respond with the message "You got me!"
curl -sLX OPTIONS 0.0.0.0:5000/catch_me -H "Origin: HolbertonSchool" -d "user_id=98"
