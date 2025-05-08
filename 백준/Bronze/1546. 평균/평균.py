# N = int(input())
# # for i in len(int(input())):
# scores = list(map(int, input().split()))
# # for _ in range(N):
# #     score = int(input())
# #     scores.append(score)

# max_num = max(scores)

# all_num = sum(scores)

# k = all_num/(max_num*100)

# print(k)
# # for _ in range(N):
# #     score = int(input())
# #     scores.append(score)


N = int(input())
scores = list(map(int, input().split()))
max_num = max(scores)
new_scores_sum = 0 
for score in scores:
    new_score = (score / max_num) * 100
    new_scores_sum += new_score
k = new_scores_sum / N
print(k)
