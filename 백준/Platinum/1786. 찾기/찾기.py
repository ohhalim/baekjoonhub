class KMP:
    def __init__(self, pattern):
        self.pattern = pattern
        self.failure = self._build_failure_function()
    
    def _build_failure_function(self):
        """
        패턴의 실패 함수를 생성합니다.
        실패 함수는 각 위치에서 매칭 실패시 돌아갈 위치를 저장합니다.
        """
        m = len(self.pattern)
        failure = [0] * m
        j = 0
        
        for i in range(1, m):
            while j > 0 and self.pattern[i] != self.pattern[j]:
                j = failure[j - 1]
                
            if self.pattern[i] == self.pattern[j]:
                j += 1
                failure[i] = j
                
        return failure
    
    def search(self, text):
        """
        주어진 텍스트에서 패턴이 등장하는 모든 위치를 찾습니다.
        반환값: (매칭 횟수, 매칭 위치들의 리스트)
        """
        positions = []
        n, m = len(text), len(self.pattern)
        j = 0
        
        for i in range(n):
            while j > 0 and text[i] != self.pattern[j]:
                j = self.failure[j - 1]
                
            if text[i] == self.pattern[j]:
                if j == m - 1:
                    positions.append(i - m + 2)  # 시작 위치를 저장
                    j = self.failure[j]
                else:
                    j += 1
                    
        return len(positions), positions

def solve():
    text = input().rstrip()
    pattern = input().rstrip()
    
    kmp = KMP(pattern)
    count, positions = kmp.search(text)
    
    print(count)
    if positions:
        print(*positions)

if __name__ == "__main__":
    solve()