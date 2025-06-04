def solution(myString, pat):
    transform_myString = ""
    for char in myString:
        if char == "A":
            transform_myString += "B"
        elif char == "B":
            transform_myString += "A"
        else:
            transform_myString += char
    
    return 1 if pat in transform_myString else 0
