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
    matr[r][c] = 0
    print(r,c,end='',sep=',')
    if (r != r_finish) or (c != c_finish):
        print(' - ', end='')
        if ((c + 1) < cmax) and (matr[r][c + 1] == 1):
            DFS(r, c + 1, r_finish, c_finish)
        if ((r + 1) < rmax) and (matr[r + 1][c] == 1):
            DFS(r + 1, c, r_finish, c_finish)
        if ((c - 1) >= 0) and (matr[r][c - 1] == 1):
            DFS(r, c - 1, r_finish, c_finish)
        if ((r - 1) >= 0) and (matr[r - 1][c] == 1):
            DFS(r - 1, c, r_finish, c_finish)
    elif (r == r_finish) and (c == c_finish):
        exit()
        return a


r = int(input('Введіть номер рядка "входу": '))
col = int(input('Введіть номер стовпця "входу": '))
r_finish = int(input('Введіть номер рядка "виходу": '))
c_finish = int(input('введіть номер стовпця "виходу": '))
print('Можливий шлях до заданої точки:')
a=DFS(r,col,r_finish,c_finish)
print(a)