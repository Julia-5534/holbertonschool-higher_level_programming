#!/usr/bin/python3
message = "{:0=2d}"
for num in range(100):
    if(num <= 98):
        print(message.format(num), end=", ")
    else:
        print(99)
