import sys

class UCPC:

    # 속성 생성
    def __init__(self,year):
        self.year = year
        self.alphabet = "A"

    # 메소드 생성
    
    def ask_number(self):
        print(self.alphabet)



year = int(sys.stdin.readline().strip())



ucpc = UCPC(year)
ucpc.ask_number()