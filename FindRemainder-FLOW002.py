#Find remainder -FLOW002
#1st input t (for the number of test cases)
# constrain{1<=t<=1000)
#then take two input a ,b(int: [1,10000])
#check find reminder when A is divided by B

t=int(input())
if t>=1 and t<=1000:
	for i in range(t):
		a,b = map(int,input().split())
		if (a and  b) >= 1 and (a and b ) <= 10000:
			print(a%b)
