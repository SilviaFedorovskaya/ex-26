f = open("Кислота 2.txt")
n = f.readline()
A = []
for st in f.readlines():
    A.append(int(st))

# записываем значения объемов колб кислоты в массив А

f = open("Вода 2.txt")
n = f.readline()
B = []
for st in f.readlines():
    B.append(int(st))

# записываем значения объемов колб воды в массив В

A.sort(reverse=True)
B.sort(reverse=True)

print(A)
print(B)

# сортруем массивы по убыванию, чтобы программа теряла наименьшие значения, а оптимальные для нахождения максимальной суммы - учитывала

NORMAL = 0
VALUE = 0
MAX_O = 0
NEED = 20 # там вроде вначале писало, что 20 надо

# ищем к каждой колбе с кислотой наилучшую колбу с водой
# после нахождения убираем колбы из списка

for x in range(len(A)):
    if A[x] * 3 <= B[0]:
        VALUE += A[x] * 4
        B.pop(0)
NORMAL = VALUE
while VALUE < NEED and len(A) > 0:
    FREAK = []
    for x in range(len(A)):
        min_o = 0
        val = 0
        ind = -1
        for y in range(len(B)):
            if A[x] * 3 > B[y]:
                o = A[x]/B[y]
                v = A[x] + B[x]
                ind = y
                if o < min_o:
                    min_o = o
                    val = v
                    ind = y
                elif o == min_o and v > val:
                    val = v
                    ind = y
        FREAK.append((min_o, val, ind))
    FREAK.sort()
    VALUE += FREAK[0][1]
    B.pop(FREAK[0][2])
if VALUE < NEED and len(A) == 0:
    print("Недостаточно ингридиентов, чтобы создать партию!")
print(NORMAL, MAX_O)