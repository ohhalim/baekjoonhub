import sys

words =[sys.stdin.readline().strip()for _ in range(5)]
max_len = 0 
for word in words:
    if len(word) > max_len:
        max_len = len(word)
result = []

for i in range(max_len):
    for j in range(5):
        if i < len(words[j]):
            result.append(words[j][i])

print("".join(result))
