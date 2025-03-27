import sys

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self,n):
        self.head = Node(1)
        current = self.head

        # 1부터 n까지의 노드 생성 및 연결
        for i in range(2,n+1):
            current.next = Node(i)
            current = current.next

        # 마지막 노드를 첫 번째 노드에 연결하여 원형 리스트 완성
        current.next = self.head


    def josephus(self,n,k):
        result = []
        current = self.head
        prev = None

        # 첫 노드의 이전 노드 찾기 (마지막 노드)
        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        prev = temp

        # n개의 노드를 모두 제거할 때까지 반복
        for _ in range(n):
            # k-1번 이동해서 k번째 노드 찾기
            for _ in range(k-1):
                prev = current
                current = current.next

            # k번쨰 노드 제거
            result.append(current.data)
            prev.next = current.next

            # 다음음 시작 위치 설정
            current = current.next

            # 모든 노드가 제거되었는 지 확인
            if prev.next == prev:
                result.append(prev.data)
                break

        return result
    


def josephus_problem(n,k):
    if n == 1:
        return [1]
    

    circular_list = CircularLinkedList(n)
    result = circular_list.josephus(n,k)
    return result


n,k = map(int,sys.stdin.readline().split())
result = josephus_problem(n,k)


# 출력 형식에 맞게 결과 출력
print("<", end="")
print(", ".join(map(str,result)),end="")
print(">")