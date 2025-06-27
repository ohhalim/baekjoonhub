def solution(my_string, indices):
    answer_list = []
    for i ,char in enumerate(my_string):
        if i not in indices:
            answer_list.append(char)
    return "".join(answer_list)