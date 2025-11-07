import tkinter as tk
from tkinter import ttk

datasiswa=[]

def buka_halaman2():
    halaman2.tkraise()
    tampilkan_data()
    
def buka_halaman3():
    halaman3.tkraise()
    
def kembali():
    halaman1.tkraise()
    
def data():
    nama=entry.get()
    kelas=entry2.get()
    alamat=entry3.get()
    
    error=[]
    if not nama or not kelas or not alamat:
        error.append("Seluruh Form Wajib diisi")
        
    if not nama:
        error.append("Nama Wajib diisi")
        
    if not kelas:
        error.append("Kelas Wajib diisi")
        
    if not alamat:
        error.append("Alamat Wajib diisi")
        
    if error:
        hasil.config(text="\n".join(error), fg="#BF092F")  # ditambah join supaya tampil rapi
    else:
        datasiswa.append({"nama": nama, "kelas": kelas, "alamat": alamat})  # benerin: 'data' diganti 'datasiswa'
        entry.delete(0, tk.END)
        entry2.delete(0, tk.END)
        entry3.delete(0, tk.END)
        hasil.config(text="Data berhasil disimpan!", fg="#4C763B")
        
def tampilkan_data():
    for i in tree.get_children():
        tree.delete(i)
    if datasiswa:  # benerin: ganti dari data_siswa ke datasiswa
        for s in datasiswa:
            tree.insert("", tk.END, values=(s["nama"], s["kelas"], s["alamat"]))
    else:
        tree.insert("", tk.END, values=("Belum ada data", "-", "-"))
        
def cari_data():
    keyword = entry_cari.get().lower()
    for i in tree_cari.get_children():
        tree_cari.delete(i)
    hasil_cari = [s for s in datasiswa if keyword in s["nama"].lower()]  # benerin data_siswa jadi datasiswa
    if hasil_cari:
        for s in hasil_cari:
            tree_cari.insert("", tk.END, values=(s["nama"], s["kelas"], s["alamat"]))
    else:
        tree_cari.insert("", tk.END, values=("Data tidak ditemukan", "-", "-"))
        
root=tk.Tk()
root.title("Data Peserta Didik")
root.geometry("450x400")
root.config(bg="#473472")

# buat ngehias(kek css tp buat ttk)
style=ttk.Style()
style.theme_use("clam")
style.configure("TFrame", background="#fced90")#maksud TFrame ini adalah kek singkatan ttk.frame,jd kalo ttk.label jd TLabel dan pakai quotation
style.configure("TLabel", background="#fced90", font=("Times New Roman", 10))
style.configure("TButton", font=("Segoe UI", 10, "bold"), padding=5)
style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"), background="#4682b4", foreground="white")#jadi kepala tabel punya stylenya sendiri(terpisah dr yg lain gitu)
style.configure("Treeview", background="#fafafa", fieldbackground="#fafafa", foreground="black")#sama kek heading

halaman1=ttk.Frame(root)
halaman2=ttk.Frame(root)
halaman3=ttk.Frame(root)

for frame in(halaman1, halaman2, halaman3):
    frame.place(relx=0, rely=0, relheight=1, relwidth=1)
    
#hal1

judul1 = ttk.Label(halaman1, text="Form Tambah Data Peserta Didik A1", font=("Times New Roman", 14, "bold"), anchor="center")
judul1.pack(pady=10)

ttk.Label(halaman1, text="Masukkan Nama", font=("Arial",10), foreground="#000").pack()
entry=ttk.Entry(halaman1,width=30)
entry.pack()
ttk.Label(halaman1, text="Kelas", font=("Arial",10),foreground="#000").pack()
entry2=ttk.Entry(halaman1, width=30)
entry2.pack()
ttk.Label(halaman1, text="Alamat", font=("Arial",10),foreground="#000").pack()
entry3=ttk.Entry(halaman1, width=30)
entry3.pack()

ttk.Button(halaman1 ,text="Daftar", command=data).pack(pady=5)
ttk.Button(halaman1, text="Lihat Data",command=buka_halaman2).pack(pady=5)
ttk.Button(halaman1, text="Cari Data", command=buka_halaman3).pack(pady=5)
tk.Button(halaman1, text="Keluar", command=root.destroy, bg="#A72703", fg="white").pack(pady=5)  # dikasih pack biar tampil

hasil = ttk.Label(halaman1, text="", background="#fced90", font=("Segoe UI", 9))
hasil.pack(pady=5)

#halaman 2
judul2 = ttk.Label(halaman2, text="Daftar Data Peserta Didik", font=("Times New Roman", 14, "bold"))
judul2.pack(pady=10)

kolom = ("Nama", "Kelas", "Alamat")
tree = ttk.Treeview(halaman2, columns=kolom, show="headings")
for kol in kolom:
    tree.heading(kol, text=kol)
    tree.column(kol, width=120)
tree.pack(pady=10, fill="x", padx=20)

ttk.Button(halaman2, text="Kembali", command=kembali).pack(pady=10)
ttk.Button(halaman2, text="Ke Halaman Cari", command=buka_halaman3).pack()

#halaman 3
judul3 = ttk.Label(halaman3, text="Cari Data Peserta Didik", font=("Times New Roman", 14, "bold"))
judul3.pack(pady=10)

ttk.Label(halaman3, text="Masukkan Nama yang Dicari:").pack(pady=5)
entry_cari = ttk.Entry(halaman3, width=30)
entry_cari.pack(pady=5)

ttk.Button(halaman3, text="Cari", command=cari_data).pack(pady=5)
ttk.Button(halaman3, text="Kembali", command=kembali).pack(pady=5)

kolom_cari = ("Nama", "Kelas", "Alamat")
tree_cari = ttk.Treeview(halaman3, columns=kolom_cari, show="headings")
for kol in kolom_cari:
    tree_cari.heading(kol, text=kol)
    tree_cari.column(kol, width=120)
tree_cari.pack(pady=10, fill="x", padx=20)

halaman1.tkraise()
root.mainloop()
