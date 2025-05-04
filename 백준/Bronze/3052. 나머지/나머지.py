# num_else = []
# for num in int(input()):
#     num_else = num % 42 
    
# print(len(set(num_else))) 

num_else = []
for _ in range(10):
    num = int(input())
    num_else.append(num % 42)

print(len(set(num_else)))