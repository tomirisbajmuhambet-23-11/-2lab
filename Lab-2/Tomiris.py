#15 вариант



# import random
#
# A= [random.randint(-20,20) for _ in range(10)]
# print("Massiv A:", A)
# n = [x for x in A if x < 0]
#
# if n:
#     max_n = max(n)
#     print("En ulken teris element:",max_n)
# else:
#     print("Teris san jok")




import random
n=10
A=[[random.randint(1,9)for _ in range(n)] for _ in range(n)]

print("Matrica A: ")
for row in A:
    print(row)

p = 1
for i in range (n):
    for j in range (n):
        if i + j > n - 1:
            p *= A[i][j]

print ("tolyktaysh diaganaldan tomen elementterdin tyndysy: ", p )



