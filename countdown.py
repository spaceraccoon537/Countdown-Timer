import time
def countdown(t):
    print("this window will remain open for",t,"seconds")
    while(t>0):
        print(t,end="...")
        time.sleep(1)
        t=t-1
    print("goodbye")
t=int(input("Enter the time in seconds upto which you want the window to remain opened:"))
countdown(t)
