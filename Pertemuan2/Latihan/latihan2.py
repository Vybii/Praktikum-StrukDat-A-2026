nilai = [75, 80, 65, 90, 85]

nilai.append(95)
print("1.", nilai)

lowest = min(nilai)
nilai.remove(lowest)
print("2.", nilai)

nilai.sort()
print("3.", nilai)

higest = max(nilai)
print("4. ")
print("Terbesar =", higest)
print("Terkecil =", lowest)
print(sum(nilai))

print(sum(nilai)/len(nilai))

print(end = "\n\n")
#Tuple
dosen = ("D001", "Dr. Andi", "Struktur Data", 12)
print("1.", dosen[1:3])

print("2. ", end = "")
for x in dosen:
  print(x, end = ", ")
print("")

y = list(dosen)
y[1] = "kiwi"
x = tuple(y)
print("3.", x)

print("4. Kelebihan tuple adalah tidak bisa diubah. Agar tidak berubah secara tidak sengaja")