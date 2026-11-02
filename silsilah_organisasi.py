
class Node:
    def __init__(self, id, nama, jabatan):
        self.id = id
        self.nama = nama
        self.jabatan = jabatan
        self.children = []

    def tambah_anak(self, node):
        self.children.append(node)


class Tree:
    def __init__(self):
        self.root = None

    # Membuat root atau pimpinan tertinggi
    def set_root(self, node):
        self.root = node

    # 1. INSERT NODE
    # Menambahkan pegawai di bawah atasan tertentu
    def insert_node(self, id, nama, jabatan, nama_atasan):
        atasan = self.search_node(nama=nama_atasan)

        if atasan is None:
            print(f"Atasan '{nama_atasan}' tidak ditemukan!")
            return

        # Memeriksa ID agar tidak duplikat
        if self.search_by_id(id) is not None:
            print(f"ID '{id}' sudah digunakan!")
            return

        node_baru = Node(id, nama, jabatan)
        atasan.tambah_anak(node_baru)

        print(f"Berhasil menambahkan {nama} "
              f"sebagai {jabatan} di bawah {atasan.nama}.")

    # 2. SEARCH NODE berdasarkan nama atau jabatan
    def search_node(self, nama=None, jabatan=None):
        if self.root is None:
            return None

        return self._search(self.root, nama, jabatan)

    def _search(self, node, nama, jabatan):
        cocok_nama = (
            nama is not None and
            node.nama.lower() == nama.lower()
        )

        cocok_jabatan = (
            jabatan is not None and
            node.jabatan.lower() == jabatan.lower()
        )

        if cocok_nama or cocok_jabatan:
            return node

        for child in node.children:
            hasil = self._search(child, nama, jabatan)
            if hasil is not None:
                return hasil

        return None

    # Pencarian berdasarkan ID
    def search_by_id(self, id):
        if self.root is None:
            return None

        return self._search_id(self.root, id)

    def _search_id(self, node, id):
        if node.id == id:
            return node

        for child in node.children:
            hasil = self._search_id(child, id)
            if hasil is not None:
                return hasil

        return None

    # Menampilkan informasi node
    def tampilkan_node(self, node):
        if node is None:
            print("Data tidak ditemukan!")
        else:
            print("ID       :", node.id)
            print("Nama     :", node.nama)
            print("Jabatan  :", node.jabatan)

    # 3. PREORDER TRAVERSAL
    # Root -> Anak
    def preorder(self, node=None, level=0):
        if node is None:
            if self.root is None:
                return
            node = self.root

        print("  " * level +
              f"{node.nama} ({node.jabatan})")

        for child in node.children:
            self.preorder(child, level + 1)

    # 4. INORDER TRAVERSAL
    # Anak pertama -> Root -> Sisa anak
    # General Tree menggunakan definisi inorder ini.
    def inorder(self, node=None, level=0):
        if node is None:
            if self.root is None:
                return
            node = self.root

        if len(node.children) > 0:
            self.inorder(node.children[0], level + 1)

        print("  " * level +
              f"{node.nama} ({node.jabatan})")

        for child in node.children[1:]:
            self.inorder(child, level + 1)

    # 5. POSTORDER TRAVERSAL
    # Anak -> Root
    def postorder(self, node=None, level=0):
        if node is None:
            if self.root is None:
                return
            node = self.root

        for child in node.children:
            self.postorder(child, level + 1)

        print("  " * level +
              f"{node.nama} ({node.jabatan})")


# ==========================================
# PROGRAM UTAMA
# ==========================================

organisasi = Tree()

# Membuat pimpinan tertinggi
rektor = Node("001", "Prof. Ahmad",
              "Rektor")
organisasi.set_root(rektor)

# Menambahkan Wakil Rektor
organisasi.insert_node(
    "002", "Dr. Budi",
    "Wakil Rektor I", "Prof. Ahmad"
)

organisasi.insert_node(
    "003", "Dr. Hasan",
    "Wakil Rektor II", "Prof. Ahmad"
)

organisasi.insert_node(
    "004", "Dr. Siti",
    "Wakil Rektor III", "Prof. Ahmad"
)

# Menambahkan Dekan
organisasi.insert_node(
    "005", "Dr. Andi",
    "Dekan Fakultas Sains dan Teknologi",
    "Dr. Budi"
)

organisasi.insert_node(
    "006", "Dr. Rahman",
    "Dekan Fakultas Syariah",
    "Dr. Budi"
)

# Menambahkan Ketua Program Studi
organisasi.insert_node(
    "007", "Pak Rudi",
    "Ketua Prodi Teknik Informatika",
    "Dr. Andi"
)

organisasi.insert_node(
    "008", "Bu Maya",
    "Ketua Prodi Sistem Informasi",
    "Dr. Andi"
)

# Menambahkan Dosen dan Staf
organisasi.insert_node(
    "009", "Pak Heru",
    "Dosen Teknik Informatika",
    "Pak Rudi"
)

organisasi.insert_node(
    "010", "Pak Dedi",
    "Dosen Teknik Informatika",
    "Pak Rudi"
)

organisasi.insert_node(
    "011", "Bu Lina",
    "Staf Fakultas Sains dan Teknologi",
    "Dr. Andi"
)


# ==========================================
# MENAMPILKAN STRUKTUR ORGANISASI
# ==========================================

print("\n===== STRUKTUR ORGANISASI =====")
organisasi.preorder()


# ==========================================
# PENCARIAN DATA
# ==========================================

print("\n===== PENCARIAN BERDASARKAN NAMA =====")
hasil = organisasi.search_node(nama="Pak Heru")
organisasi.tampilkan_node(hasil)

print("\n===== PENCARIAN BERDASARKAN JABATAN =====")
hasil = organisasi.search_node(
    jabatan="Dekan Fakultas Syariah"
)
organisasi.tampilkan_node(hasil)


# ==========================================
# MENAMBAHKAN DATA BARU
# ==========================================

print("\n===== MENAMBAHKAN PEGAWAI BARU =====")
organisasi.insert_node(
    "012", "Bu Nisa",
    "Dosen Sistem Informasi",
    "Bu Maya"
)


# ==========================================
# TRAVERSAL
# ==========================================

print("\n===== PREORDER TRAVERSAL =====")
organisasi.preorder()

print("\n===== INORDER TRAVERSAL =====")
organisasi.inorder()

print("\n===== POSTORDER TRAVERSAL =====")
organisasi.postorder()
