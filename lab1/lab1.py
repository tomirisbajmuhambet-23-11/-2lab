# # 1-tapsyrma
# a=10
# b=a*(a+1)//2
# print("b=",b)

# 2-tapsyrma
n=int(input("N="))
length=0
while n>0:
    n//=10
    length+=1
print("Dlinna slov=",length)

