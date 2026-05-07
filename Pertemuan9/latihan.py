class Node:
    def __init__(self, judul, pengarang):
        self.judul = judul
        self.pengarang = pengarang
        self.prev = None
        self.next = None

class Literasi:
    def __init__(self):
        self.head = None

    def insert_tail(self, judul, pengarang):
        new_node = Node(judul, pengarang)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node
        new_node.prev = current

    def print_forward(self):
        current = self.head
        while current:
            print(f"{current.judul} oleh {current.pengarang}", end=" <-> ")
            current = current.next
        print("None")

    def print_backward(self):
        if self.head is None:
            print("None")
            return

        current = self.head
        while current.next:
            current = current.next

        while current:
            print(f"{current.judul} oleh {current.pengarang}", end=" <-> ")
            current = current.prev
        print("None")

    def delete_by_judul(self, judul):
        current = self.head

        while current:
            if current.judul == judul:
                if current.prev is None:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                else:
                    current.prev.next = current.next

                    if current.next:
                        current.next.prev = current.prev
                return

            current = current.next

buku = Literasi()

buku.insert_tail("Laskar Pelangi", "Andrea Hirata")
buku.insert_tail("Bumi Manusia", "Pramoedya Ananta Toer")
buku.insert_tail("Sang Pemimpi", "Andrea Hirata")

print("Forward:")
buku.print_forward()

print("Backward:")
buku.print_backward()

buku.delete_by_judul("Bumi Manusia")

print("Setelah hapus Bumi Manusia:")
buku.print_forward()