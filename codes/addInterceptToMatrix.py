def addInteceptToMatrix(mat):
    matrix = []
    for i in range(len(mat)):
        lst = mat[i][:]
        lst.insert(0,1)
        matrix.append(lst)
    return matrix

if __name__ == '__main__' :
    mat = [[0,1,2,3], [4,5,6,7]]
    print(mat)

    mat2 = addInteceptToMatrix(mat)
    print(mat2)
    print(mat)

    tes = [1,2,3,4]
    tes.append(7)
    #print(tes)
    tes.insert(0, 9)
    #print(tes)