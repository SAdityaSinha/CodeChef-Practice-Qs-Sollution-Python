# First and Last Digit 
#give input n(int)''
# to obtain the sum of 1st and last digit of the number n

# t for testcases:: t(int[1,1000])
#n for the num ::(int[1, 1000000])

t=int(input())
if t>=1 and t<=1000:
	for i in range(t):
		n=input()
		if int(n)>=1  and int(n)<=1000000:
			print(int(n[0])+int(n[-1]))
