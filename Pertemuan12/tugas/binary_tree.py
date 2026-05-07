class Node:
    def __init__(self, data):
        self.data = data
        self.kiri = None
        self.kanan = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_manual(self):
        # A adalah Root
        self.root = Node('A')
        
        self.root.kiri = Node('B')
        self.root.kanan = Node('C')
        
        self.root.kiri.kiri = Node('D')
        self.root.kiri.kanan = Node('E')
        
        self.root.kanan.kanan = Node('F')

    def traverse_preorder(self, node, hasil):
        if node is not None:
            hasil.append(node.data)
            self.traverse_preorder(node.kiri, hasil)
            self.traverse_preorder(node.kanan, hasil)

    def traverse_inorder(self, node, hasil):
        if node is not None:
            self.traverse_inorder(node.kiri, hasil)
            hasil.append(node.data)
            self.traverse_inorder(node.kanan, hasil)

    def traverse_postorder(self, node, hasil):
        if node is not None:
            self.traverse_postorder(node.kiri, hasil)
            self.traverse_postorder(node.kanan, hasil)
            hasil.append(node.data)

    def get_leaf_nodes(self, node, hasil):
        if node is not None:
            if node.kiri is None and node.kanan is None:
                hasil.append(node.data)
            self.get_leaf_nodes(node.kiri, hasil)
            self.get_leaf_nodes(node.kanan, hasil)

if __name__ == "__main__":
    print('SISTEM AUDIT DISTRIBUSI "CEPAT SAMPAI"')
    print("======================================")
    print("[INFO] Membangun Struktur Gudang...")
    
    gudang_tree = BinaryTree()
    gudang_tree.insert_manual()
    
    print("[INFO] Struktur berhasil dibuat.\n")
    print("HASIL AUDIT:")
    
    pre_hasil = []
    gudang_tree.traverse_preorder(gudang_tree.root, pre_hasil)
    print(f"1. Pre-Order : {' - '.join(pre_hasil)}")
    
    in_hasil = []
    gudang_tree.traverse_inorder(gudang_tree.root, in_hasil)
    print(f"2. In-Order : {' - '.join(in_hasil)}")
    
    post_hasil = []
    gudang_tree.traverse_postorder(gudang_tree.root, post_hasil)
    print(f"3. Post-Order : {' - '.join(post_hasil)}\n")
    
    leaf_hasil = []
    gudang_tree.get_leaf_nodes(gudang_tree.root, leaf_hasil)
    print(f"[DATA] Gudang Ujung (Leaf Nodes): {', '.join(leaf_hasil)}")
    
    print("======================================")
    print("Audit Selesai!")