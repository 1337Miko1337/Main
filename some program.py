f = open('in.txt', 'r')
c = list(f)
matr = []
for row in c:
    el = list(map(int, row.split()))
    matr.append(el)
rmax = len(matr)
cmax = len(matr[0])
f.close()


def DFS(r, c):
    matr[r][c] = 0
    print( r, '-', c)
    if ((c + 1) < cmax) and (matr[r][c + 1] == 1):
        DFS(r, c + 1)
    if ((r + 1) < rmax) and (matr[r + 1][c] == 1):
        DFS(r + 1, c)
    if ((c - 1) >= 0) and (matr[r][c - 1] == 1):
        DFS(r, c - 1)
    if ((r - 1) >= 0) and (matr[r - 1][c] == 1):
        DFS(r - 1, c)


r = int(input('Введіть номер рядка "входу": '))
col = int(input('Введіть номер стовпця "входу": '))
a=DFS(r,col)
