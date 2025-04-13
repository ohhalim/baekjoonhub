def solution(babbling):
    answer = 0
    sounds = ["aya", "ye", "woo", "ma"]
    
    for word in babbling:
        for sound in sounds:
            if sound in word:
                word = word.replace(sound, "!", 1)
        
        word = word.replace("!", "")
        if word == "":
            answer += 1
            
    return answer