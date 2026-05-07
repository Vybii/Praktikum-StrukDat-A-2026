class StackList:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, url):
        self.items.append(url)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return "Riwayat kosong"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)

stack = StackList()
kosong = stack.is_empty()
tambah = stack.push("halo")
back = stack.pop()
last_ada_apa = stack.peek()
panjang = stack.size()

print(kosong)
print(last_ada_apa)
print(panjang)