import time

n = 2
rate = True
char = 30
while rate:
    time.sleep(0.1)
    if n < 3:
        print(f"{int(char)}")
        char -= 0.1
        if char < 1:
            char += 60
            print(f"{int(char)}")
            n += 1
            print (n)
    else:
        rate = False
rattle = char / 15
print(int(rattle))        