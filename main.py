# Simple Counter
# by cscheerer on GitHub
# Put in "reset" to reset the counter.

import time

count = 0
newcount = 0

while True:
    time.sleep(0.2)
    newcount = input("Add: ")

    if newcount == "reset":
        count = 0
    else:
        newcount = int(newcount)
        count = count + newcount
        print(count)


