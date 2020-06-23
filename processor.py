def add_matrix():
    r_c1 = input('Enter size of first matrix: > ').split()
    n = 0
    matrix1 = []
    print('Enter first matrix:')
    while n != int(r_c1[0]):
        m1 = [x for x in input('> ').split()]
        n += 1
        matrix1.append(m1)
    r_c2 = input('Enter size of second matrix: > ').split()
    m = 0
    matrix2 = []
    print('Enter second matrix:')
    while m != int(r_c2[0]):
        m2 = [x for x in input('> ').split()]
        matrix2.append(m2)
        m += 1

    result = []
    if r_c1 == r_c2:
        for i in range(len(matrix1)):
            s = []
            for n in range(len(matrix1[i])):
                if '.' in matrix1[i][n]:
                    f = float(matrix1[i][n]) + float(matrix2[i][n])
                    s.append(f)
                else:
                    f = int(matrix1[i][n]) + int(matrix2[i][n])
                    s.append(f)
            result.append(s)
    else:
        print('The operation cannot be performed.')

    for i in result:
        print('The result is:')
        print(*i)


def multiply_by_const():
    r_c = input('Enter size of the matrix: > ').split()
    n = 0
    matrix1 = []
    while n != float(r_c[0]):
        m1 = [float(x) for x in input('Enter matrix:\n> ').split()]
        n += 1
        matrix1.append(m1)
    const = float(input())
    for i in range(len(matrix1)):
        for n in range(len(matrix1[i])):
            matrix1[i][n] = matrix1[i][n] * const
    for row in matrix1:
        print('The result is:')
        print(*row)


def multiply_by_matrix():
    r_c1 = input('Enter size of first matrix: > ').split()
    n = 0
    matrix1 = []
    print('Enter first matrix:')
    while n != int(r_c1[0]):
        m1 = [x for x in input('> ').split()]
        n += 1
        matrix1.append(m1)
    r_c2 = input('Enter size of second matrix:> ').split()
    m = 0
    matrix2 = []
    print('Enter second matrix:')
    while m != int(r_c2[0]):
        m2 = [x for x in input('> ').split()]
        matrix2.append(m2)
        m += 1
    if r_c1[1] != r_c2[0]:
        print('The operation cannot be performed.')
    else:
        multiply_matrix = []
        for line in enumerate(matrix1):
            i = 0
            new_line = []
            while i != int(r_c2[1]):
                new = 0
                for n in enumerate(line[1]):
                    if '.' in matrix2[n[0]][i]:
                        new += float(n[1]) * float(matrix2[n[0]][i])
                    else:
                        new += int(n[1]) * int(matrix2[n[0]][i])
                new_line.append(new)
                i += 1
            multiply_matrix.append(new_line)
        print('The result is:')
        for row in multiply_matrix:
            print(*row)


def trans_key():
    print('1. Main diagonal\n2. Side diagonal\n'
          '3. Vertical line\n4. Horizontal line')
    key_tp = input('Your choice: > ').strip()
    if key_tp == '1':
        main_diagonal()
    elif key_tp == '2':
        side_diagonal()
    elif key_tp == '3':
        vertical_line()
    elif key_tp == '4':
        horizon_line()


def main_diagonal():
    r_c1 = input('Enter size of the matrix: > ').split()
    n = 0
    matrix = []
    print('Enter matrix:')
    while n != int(r_c1[0]):
        m1 = [x for x in input('> ').split()]
        n += 1
        matrix.append(m1)
    tp_matrix =[]
    i = 0
    while i != max(int(r_c1[1]), int(r_c1[0])):
        new_line = []
        for line in matrix:
            new = line[i]
            new_line.append(new)
        tp_matrix.append(new_line)
        i += 1
    print('The result is:')
    for row in tp_matrix:
        print(*row)
    print('\n')


def side_diagonal():
    r_c1 = input('Enter size of the matrix: > ').split()
    n = 0
    matrix = []
    print('Enter matrix:')
    while n != int(r_c1[0]):
        m1 = [x for x in input('> ').split()]
        n += 1
        matrix.append(m1)
    tp_matrix = []
    i = (max(int(r_c1[1]), int(r_c1[0])) - 1)
    while i != -1:
        new_line = []
        for line in matrix[::-1]:
            new = line[i]
            new_line.append(new)
        tp_matrix.append(new_line)
        i -= 1
    print('The result is:')
    for row in tp_matrix:
        print(*row)


def vertical_line():
    r_c1 = input('Enter size of the matrix: > ').split()
    n = 0
    matrix = []
    print('Enter matrix:')
    while n != int(r_c1[0]):
        m1 = [x for x in input('> ').split()]
        n += 1
        matrix.append(m1)
    tp_matrix = []
    for line in matrix:
        line = line[::-1]
        tp_matrix.append(line)
    print('The result is:')
    for row in tp_matrix:
        print(*row)
    print('\n')


def horizon_line():
    r_c1 = input('Enter size of the matrix: > ').split()
    n = 0
    matrix = []
    print('Enter matrix:')
    while n != int(r_c1[0]):
        m1 = [x for x in input('> ').split()]
        n += 1
        matrix.append(m1)
    tp_matrix = matrix[::-1]
    print('The result is:')
    for row in tp_matrix:
        print(*row)


def calculate_det():
    r_c1 = input('Enter size of the matrix: > ').split()
    n = 0
    matrix = []
    print('Enter matrix:')
    while n != int(r_c1[0]):
        m1 = [x for x in input('> ').split()]
        n += 1
        matrix.append(m1)
    if r_c1[0] == '2':
        print('The result is:')
        print(det_for_2x2(matrix))
    elif r_c1[0] == '3':
        print('The result is:')
        print(det_for_3x3(matrix))
    elif r_c1[0] == '1':
        print('The result is:')
        print(*matrix[0])
    elif r_c1[0] == '4':
        print('The result is:')
        print(det_for_4_and_more(matrix))
    else:
        print('The result is:')
        print(define_det(det_for_4_and_more(matrix)))
        print()


def define_det(*argw):
    det = 0
    z = 0
    det_0, co_fact = argw[0]
    for i in range(len(det_0)):
        if z % 2 == 0:
            det += int(det_0[i]) * int(co_fact[i])
        else:
            det -= int(det_0[i]) * int(co_fact[i])
        z += 1
    return det


def det_for_2x2(matr):
    if '.' in matr[0][0]:
        return float(matr[0][0]) * float(matr[1][1]) - float(matr[0][1]) * float(matr[1][0])
    else:
        return int(matr[0][0]) * int(matr[1][1]) - int(matr[0][1]) * int(matr[1][0])


def det_for_3x3(matr):
    count = 0
    matrix_2x2 = []
    co_fact = []
    while count != len(matr):
        zhong = []
        for line_ind in range(0, len(matr)):
            if line_ind == count:
                co_fact.append(matr[line_ind][0])
            else:
                zhong.append(matr[line_ind][1:])
        matrix_2x2.append(det_for_2x2(zhong))
        count += 1
    det = 0
    z = 2
    for ind in range(len(co_fact)):
        if z % 2 == 0:
            if '.' in co_fact[ind]:
                det += float(co_fact[ind]) * float(matrix_2x2[ind])
            else:
                det += int(co_fact[ind]) * int(matrix_2x2[ind])
        else:
            if '.' in co_fact[ind]:
                det -= float(co_fact[ind]) * float(matrix_2x2[ind])
            else:
                det -= int(co_fact[ind]) * int(matrix_2x2[ind])
        z += 1
    return det


def det_for_4_and_more(matr):
    count = 0
    matrix_2x2 = []
    co_fact = []
    while count != len(matr):
        zhong = []
        for line_ind in range(0, len(matr)):
            if line_ind == count:
                co_fact.append(matr[line_ind][0])
            else:
                zhong.append(matr[line_ind][1:])
        matrix_2x2.append(zhong)
        count += 1
    new_m = 0
    if len(matrix_2x2[0]) == 3:
        new_m = []
        for matrix1 in matrix_2x2:
            new_m.append(det_for_3x3(matrix1))
    if new_m != 0:
        z = 0
        det = 0
        for ind in range(len(co_fact)):
            if z % 2 == 0:
                if '.' in co_fact[ind]:
                    det += float(co_fact[ind]) * float(new_m[ind])
                else:
                    det += int(co_fact[ind]) * int(new_m[ind])
            else:
                if '.' in co_fact[ind]:
                    det -= float(co_fact[ind]) * float(new_m[ind])
                else:
                    det -= int(co_fact[ind]) * int(new_m[ind])
            z += 1
        return det
    m_4 = []
    for matrix_1 in matrix_2x2:
        m_4.append(det_for_4_and_more(matrix_1))
    return co_fact, m_4


def inverse_matrix():
    r_c1 = input('Enter size of the matrix: > ').split()
    n = 0
    matrix = []
    print('Enter matrix:')
    while n != int(r_c1[0]):
        m1 = [x for x in input('> ').split()]
        n += 1
        matrix.append(m1)
    det_i = 0
    if r_c1[0] == '2':
        print("This matrix doesn't have an inverse.")
    elif r_c1[0] == '3':
        det_i = det_for_3x3(matrix)
    elif r_c1[0] == '1':
        print("This matrix doesn't have an inverse.")
    elif r_c1[0] == '4':
        det_i = det_for_4_and_more(matrix)
    else:
        det_i = define_det(det_for_4_and_more(matrix))
    det5 = co_factors(matrix)
    z = 0
    a_1 = []
    t = 0
    if r_c1[0] == '3':
        if det_i != 0:
            for x in det5:
                # print(x)
                if z % 2 == 0:
                    num = ((1 / det_i) * x)
                    if num == 0:
                        a_1.append(0)
                    else:
                        a_1.append(num)
                else:
                    num = ((1 / det_i) * x * (-1))
                    if num == 0:
                        a_1.append(0)
                    else:
                        a_1.append(num)
                z += 1
        print('The result is:')
        ty = 0
        for i in range(int(r_c1[0])):
            a = a_1[ty:int(r_c1[0]) + ty]
            print(*a)
            ty += int(r_c1[0])
    else:
        for i in range(int(r_c1[0])):
            a = det5[t:int(r_c1[0]) + t]
            a_1.append(a)
            t += int(r_c1[0])
        final_m = []
        for row in a_1:
            if z % 2 != 0:
                a = [1 / det_i * a * (-1) for a in row]
                final_m.append(a)
            else:
                row = [1 / det_i * a for a in row]
                final_m.append(row)
            z += 1
        print('The result is:')
        for line in final_m:
            print(*line)


def co_factors(matr):
    count = 0
    matrix_2x2 = []
    co_fact = []
    len_list = 0
    for x in matr:
        len_list += len(x)
    count1 = 0
    cc = 0
    while count != len_list:
        if count1 == len(matr):
            count1 = 0
            cc += 1
        zhong = []
        for line_ind in range(0, len(matr)):
            if len(co_fact) <= len_list - 1:
                co_fact.append(matr[line_ind][count1])
            if len(matr) == 3:
                if line_ind != count1:
                    if cc == 0:
                        zhong.append(matr[line_ind][1:])
                    elif len(matr) - 1 > cc >= 1:
                        lst1 = matr[line_ind][:(len(matr[line_ind]) // 2) + cc - 1]
                        lst2 = matr[line_ind][(len(matr[line_ind]) // 2) + 1 + cc - 1:]
                        sum_lst = lst1 + lst2
                        zhong.append(sum_lst)
                    else:
                        zhong.append(matr[line_ind][:-1])
            else:
                if line_ind != count1:
                    if cc == 0:
                        zhong.append(matr[line_ind][1:])
                    elif len(matr) - 1 > cc >= 1:
                        lst1 = matr[line_ind][:(len(matr[line_ind]) // 2) + cc - 2]
                        lst2 = matr[line_ind][(len(matr[line_ind]) // 2) + cc - 1:]
                        sum_lst = lst1 + lst2
                        zhong.append(sum_lst)
                    else:
                        zhong.append(matr[line_ind][:-1])
        count1 += 1
        matrix_2x2.append(zhong)
        count += 1
    if len_list == 9:
        det9 = []
        for mat in matrix_2x2:
            det9.append(det_for_2x2(mat))
        return det9
    if len_list == 16:
        det16 = []
        for mat in matrix_2x2:
            det16.append(det_for_3x3(mat))
        for i in range(len(det16)):
            if i % 2 != 0:
                det16[i] = det16[i] * (-1)
        return det16
    if len_list > 16:
        det17 = []
        for mat in matrix_2x2:
            det17.append(det_for_4_and_more(mat))
        for i in range(len(det17)):
            if i % 2 != 0:
                det17[i] = det17[i] * (-1)
        return det17


while True:
    print('1. Add matrices\n2. Multiply matrix by a constant\n'
          '3. Multiply matrices\n4. Transpose matrix\n'
          '5. Calculate a determinant\n6. Inverse matrix\n0. Exit')
    key = input('Your choice: > ').strip()
    if key == '1':
        add_matrix()
    elif key == '2':
        multiply_by_const()
    elif key == '3':
        multiply_by_matrix()
    elif key == '4':
        trans_key()
    elif key == '5':
        calculate_det()
    elif key == '6':
        inverse_matrix()
    elif key == '0':
        break
