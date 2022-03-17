import math
import time
num=int(input())
secn=int(input())
time.sleep(secn/1000)
print(f"Square root of {num} after {secn} miliseconds is {math.sqrt(num)}")