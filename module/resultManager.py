
class ResultManager:
    # 빈 큐를 초기화 (주어진 인자로 큐의 최대) 길이 설정
    def __init__(self, n):
        self.maxCount = n
        self.data = [None] * n
        self.count = 0

    def plusCount(self):
        self.count += 1
        if self.count == self.maxCount:
            self.count = 0 
    
    def push(self, element):
        self.plusCount()
        self.data[self.count] = element
        currnet = element
        for item in self.data:
            if item != currnet:
                return False

        return True
