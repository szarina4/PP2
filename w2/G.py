N=int(input())
demons=dict()
for i in range(N):
  a=input().split() 
  if a[1] in demons:
    demons[a[1]]+= 1
  else:
    demons[a[1]] = 1
n = int(input()) 
hunter = dict() 
for i in range(n):
  b = input().split() 
  if b[1] in hunter:
    hunter[b[1]]+=int(b[2])
  else:
    hunter[b[1]]=int(b[2])

surv = 0

for x in demons.keys():
  if x in hunter:
    if demons[x] >hunter[x]:
      surv += demons[x]-hunter[x]
  else:
    surv += demons[x]

print("Demons left:",surv)