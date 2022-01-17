# poooj want X $USD
#machine accepts X only in the multiple of 5
#for each successful withdrawal the bank charges 0.5 $USD
# calculate Pooja's account balance after an attempted transaction 

# 0<X<2000      // Amount to be withdrawn 
#0<=Y<=2000     // Amount in her account initially
# Y chould with of two digit of pricission  e.g. Y=100.00

#if (Y>X){
#   Y-X).float()}
#else{
#   y.float()}


X , Y = input().split()
X=int(X)
Y=float(Y)
if Y>=(X+0.5) and X%5==0:
    v=(Y-X-0.5)
    print('%.2f'%v)
else:
    print('%.2f'%Y)

