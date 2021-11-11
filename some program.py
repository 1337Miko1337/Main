f = open('in.txt', 'r')
c = list(f)
matr = []
for row in c:
    el = list(map(int, row.split()))
    matr.append(el)
rmax = len(matr)
cmax = len(matr[0])
f.close()


def DFS(r, c, r_finish, c_finish):
    print( r, '-', c)
    print(r != r_finish)
    print(c != c_finish)
    if (r != r_finish) or (c != c_finish):
        if ((c + 1) < cmax) and (matr[r][c + 1] == 1):
            DFS(r, c + 1, r_finish, c_finish)
        if ((r + 1) < rmax) and (matr[r + 1][c] == 1):
            DFS(r + 1, c, r_finish, c_finish)
        if ((c - 1) >= 0) and (matr[r][c - 1] == 1):
            DFS(r, c - 1, c_finish)
        if ((r - 1) >= 0) and (matr[r - 1][c] == 1):
            DFS(r - 1, c, r_finish)
    elif (r == r_finish) and (c == c_finish):
        exit()
        return


r = int(input('Введіть номер рядка "входу": '))
col = int(input('Введіть номер стовпця "входу": '))
a=DFS(r,col,9,1)
