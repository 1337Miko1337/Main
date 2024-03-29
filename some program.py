f = open('in.txt', 'r')
c = list(f)
matr = []
for row in c:
    el = list(map(int, row.split()))
    matr.append(el)
rmax = len(matr)
cmax = len(matr[0])
f.close()


def BFS(r, c, r_finish, c_finish, k=1):
    que = []
    matr[r][c] = 2
    que.append([r, c])
    while len(que) > 0:
        k += 1
        a = k
        tmp = que.pop(0)
        r = tmp[0]
        c = tmp[1]
        while matr[r][c] != a:
            a -= 1
        if matr[r_finish][c_finish] == 1:
            if ((c + 1) < cmax) and (matr[r][c + 1] == 1):
                que.append([r, c + 1])
                matr[r][c + 1] = a + 1
            if ((r + 1) < rmax) and (matr[r + 1][c] == 1):
                que.append([r + 1, c])
                matr[r + 1][c] = a + 1
            if ((c - 1) >= 0) and (matr[r][c - 1] == 1):
                que.append([r, c - 1])
                matr[r][c - 1] = a + 1
            if ((r - 1) >= 0) and (matr[r - 1][c] == 1):
                que.append([r - 1, c])
                matr[r - 1][c] = a + 1
    return a


def road(r, c, k=2):
    count = 0
    a = []
    while k > 2:
        if ((c + 1) < cmax) and (matr[r][c + 1] == k - 1):
            a.append([r, c + 1])
            count += 1
            c += 1
            k -= 1
        if ((r + 1) < rmax) and (matr[r + 1][c] == k - 1):
            a.append([r + 1, c])
            count += 1
            r += 1
            k -= 1
        if ((c - 1) >= 0) and (matr[r][c - 1] == k - 1):
            a.append([r, c - 1])
            c = c - 1
            k -= 1
            count += 1
        if ((r - 1) >= 0) and (matr[r - 1][c] == k - 1):
            a.append([r - 1, c])
            count += 1
            r -= 1
            k -= 1
    return a


r = int(input('Введіть номер рядка "входу": '))
col = int(input('Введіть номер стовпця "входу": '))
r_finish = int(input('Введіть номер рядка "виходу": '))
c_finish = int(input('введіть номер стовпця "виходу": '))
b = BFS(r, col, r_finish, c_finish)
a = road(r_finish, c_finish, b)
a.reverse()
print('Найкоротший шлях:')
for i in range(len(a)):
    print(a[i], end='')
    if i != len(a) - 1:
        print(end='-')
