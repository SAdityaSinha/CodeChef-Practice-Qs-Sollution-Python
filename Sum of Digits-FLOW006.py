# you have to calculate sum of digits of an intiger N 

# input t==(t:int{no. of test cases})
#n that would the value of those
#1<= t <= 1000
#1<= n <= 1000000

#output would be the sum of those intigers 

t = int(input())
if t>= 1 and t<= 1000:
    for i in range(t):
        n=input()
        sm=0
        for k in n:
            k=int(k)
            sm+=k
        print(sm)
