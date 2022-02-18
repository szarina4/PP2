numheads=int(input("Enter number of heads:"))
numlegs=int(input("Enter number of legs:"))
def solve(numheads,numlegs):
    rabbit=(numlegs-2*numheads)/2
    chicken=numheads-rabbit
    print("Number of chicken:",int(chicken))
    print("Number of rabbit:",int(rabbit))
solve(numheads,numlegs)
