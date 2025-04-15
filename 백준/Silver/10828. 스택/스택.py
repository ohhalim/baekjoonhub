import sys

# Stack 클래스 정의
class Stack:
    def __init__(self):
        # 빈 리스트로 스택 초기화
        self.stack = []
    
    def push(self, X):
        # 정수 X를 스택에 추가
        self.stack.append(X)
    
    def pop(self):
        # 스택이 비어 있지 않으면 맨 위 요소를 제거하고 반환, 비어 있으면 -1 반환
        if self.stack:
            return self.stack.pop()
        else:
            return -1
    
    def size(self):
        # 스택의 크기 반환
        return len(self.stack)
    
    def empty(self):
        # 스택이 비어 있으면 1, 아니면 0 반환
        return 1 if not self.stack else 0
    
    def top(self):
        # 스택이 비어 있지 않으면 맨 위 요소를 반환, 비어 있으면 -1 반환
        if self.stack:
            return self.stack[-1]
        else:
            return -1

# 메인 코드
if __name__ == "__main__":
    # 명령의 수 입력
    n = int(input())
    # Stack 인스턴스 생성
    stack = Stack()
    
    # 명령 처리
    for _ in range(n):
        command = sys.stdin.readline().strip().split()
        
        if command[0] == 'push':
            # push 명령: 정수를 스택에 추가
            stack.push(int(command[1]))
        
        elif command[0] == 'pop':
            # pop 명령: 결과를 출력
            print(stack.pop())
        
        elif command[0] == 'size':
            # size 명령: 결과를 출력
            print(stack.size())
        
        elif command[0] == 'empty':
            # empty 명령: 결과를 출력
            print(stack.empty())
        
        elif command[0] == 'top':
            # top 명령: 결과를 출력
            print(stack.top())