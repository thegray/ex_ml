def transposeMatrix(matrix):
    transposed = []
    transposed = [[row[i] for row in matrix] for i in range((len(matrix[0])))]
    return transposed

def transposeVector(vector):
    transposed = []
    transposed = [[i] for i in range(len(vector))]
    return transposed

if __name__ == '__main__':
    ll = [0,1,2,3]
    print(ll)

    tes = transposeVector(ll)
    print(tes)