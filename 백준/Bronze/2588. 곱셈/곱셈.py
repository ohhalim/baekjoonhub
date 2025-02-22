num1 = int(input())
num2 = int(input())

ones = num2 % 10 
tens = (num2 // 10) % 10
hundreds = num2 // 100

line1 = num1 * ones
line2 = num1 * tens
line3 = num1 * hundreds
result = num1 * num2

print(line1)
print(line2)
print(line3)
print(result)