import time

x = int(input("TIMW IN SECNTD: "))

time.sleep(1)


for i in range(x , 0 ,-1):
    hour = int(x / 3600)
    minute = int((x/60)%60)
    secound = (x % 60)
    print(f"{hour:02}:{minute:02}:{secound:02}")
    time.sleep(1)


print("Time's Up MF")