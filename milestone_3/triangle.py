
def get_triangle(rows: int):

    p_triangle = []

    for i in range(rows):
        row = [1] * (i+1)
        for j in range(1, i):
            row[j] = (p_triangle[i-1][j-1]+p_triangle[i-1][j])
        p_triangle.append(row)

    for r in p_triangle:
        print(r)


get_triangle(5)


def triangle_centrated(rows: int):
    p_triangle = []

    for i in range(rows):
        row = [1] * (i+1)
        for j in range(1, i):
            row[j] = (p_triangle[i-1][j-1]+p_triangle[i-1][j])
        p_triangle.append(row)

    triangle_centrated = []

    for i in range(rows):
        row = ""
        for j in range(len(p_triangle[i])):
            row = row + str(p_triangle[i][j])+" "

        triangle_centrated = triangle_centrated+[row]

    lmax = len(triangle_centrated[rows-1])-1

    for i in range(rows):
        s = triangle_centrated[i]
        lenth = len(s) - 1
        print(" "*((lmax-lenth) // 2), end='')
        print(s)


triangle_centrated(int(input("please input your value: ")))
