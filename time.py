import time

minutes = int(input("Enter the number of minutes to fucus:"))
seconds = minutes * 60

while seconds:
     mins, secs = divmod(seconds, 60)
     timer = '{:02d}:{:02d}'.format(mins,secs)
     print(timer, end="\r")
     time.sleep(1)
     second -= 1
     
print("Time is up!")
