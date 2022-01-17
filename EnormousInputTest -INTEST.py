# We have to consider the enormous Input/Output 
# that be able tp process at least 2.5 MB of data per secound at runtime

#input begun with n,k ==(n:int,k:<=10**7)
# and then the n lines of input taking ti ==(ti<10**9)

#single int output denoting how many ti are divisible by k

n,k = map(int,input().split())
ct=0
for i in range(n):
    ti = int(input())
    if ti%k==0:
        ct+=1
print(ct)
