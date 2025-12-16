# def solution(participant, completion):
#         name_count = {}
#         for name in participant:
#             if name in name_count:
#                 name_count[name] += 1 
#             else: 
#                 name_count[name] = 1
            
#         for name in completion:
#              name_count[name] -= 1 

#         for name, count in name_count.items():
#              if count > 0:
#                 return name
             
    
def solution(participant, completion):
    name_count ={}
    for name in participant:
        if name in name_count:
            name_count[name] += 1
        else:
            name_count[name] =1 
    
    for name in completion:
        name_count[name] -= 1
    
    for name, count in name_count.items(): # items 딕셔너리 키 값을 튜플 (key, value)형태로 반환
        if count > 0:
            return name 
            
            