import time

up = True
n = 0
i = 50
while True:
    if up:
        n += 1
        if n == i:
            up = False

    if not up:
        n -= 1
        if n == 0:
            up = True


    print("#" * n)
    time.sleep(0.01)
