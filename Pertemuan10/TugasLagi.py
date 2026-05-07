class Node:
    def __init__(self, url):
        self.url = url
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None
        self.count = 0

    def is_empty(self):
        return self.top == 0

    def push(self, url):
        new_node = Node(url)
        new_node.next = self.top
        self.top = new_node

        self.count +=1


    def pop(self):
        if self.is_empty():
            return "Riwayat kosong"

        temp = self.top.url
        self.top = self.top.next
        self.count -= 1
        return temp


    def peek(self):
        if not self.is_empty():
            return self.top.url
        else:
            return None

    def size(self):
        return self.count

link = StackLinkedList()
link.push("ayam")
link.push("linkungan")
link.push("Nipis Madu-holic")

print(link.peek())
print(link.size())
print(link.pop())
print(link.peek())
print(link.is_empty())