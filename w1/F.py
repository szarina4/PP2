n=int(input())
for i in range(n):
    t=int(input())
    if t<=10:
        print("Go to work!")
    if t>10 and t<=25:
        print("You are weak")
    if t>25 and t<=45:
        print("Okay, fine")
    if t>45:
        print("Burn! Burn! Burn Young!")