# cook your dish here
# 1 submission in 30s
# contest is of x*60s
# no submission in last 5s
# submission time = x*60 - 5 s



# to get the maximum number of submission 


t = int(input())
for i in range(0,t):
    x = int(input())
    # output possible
    time = x*60
    subm = time // 30
    print(subm)
