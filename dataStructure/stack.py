
'''
[연산 정의]
 size(): 현재 스택에 들어있는 원소의 개수
 isEmpty(): 스택이 비어있는지 판단
 push(x): x를 스택에 추가
 pop(): 맨 위에 저장된 원소를 제거(반환)
 peek(): 맨 위에 저장된 원소를 반환o, 제거x

'''



class ArrayStack:

    # 빈 스택 초기화
    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    # 원소 추가
    def push(self, item):
        self.data.append(item)

    # 원소 삭제
    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]


class LinkedListStack:

    def __init__(self):
        self.data = DoublyLinkedList()

    def size(self):
        return self.data.getLength()

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        node = Node(item)
        self.data.insertAt(self.size()+1, node)

    def pop(self):
        return self.data.popAt(self.size())

    def peek(self):
        return self.data.getAt(self.size()).data


