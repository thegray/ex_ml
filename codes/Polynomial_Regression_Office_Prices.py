# THIS IS ONE FAILURE EXPERIMENT
# I TRIED TO SOLVE THIS USING PURE PYTHON
# I DONT KNOW HOW TO GET THE CORRECT THETA OF POLYNOMIAL REGRESSION

# ------ matrix thingy ------
# ------ sometimes useful lol

def transposeMatrix(matrix):
    transposed = []
    transposed = [[row[i] for row in matrix] for i in range((len(matrix[0])))]
    return transposed

def transposeVector(vector):
    transposed = []
    transposed = [[i] for i in range(len(vector))]
    return transposed

def dotProductMatrix(mat, matTransposed):
    result = []
    col = len(mat[0])
    row = len(mat)
    for r in range(row):
        lst = []
        for r2 in range(row):
            sum = 0.0
            for c in range(col):
                #print("(r:{}, c:{}) * (c:{}, r2:{})".format(r,c,c,r2))
                sum += mat[r][c] * matTransposed[c][r2]
            lst.append(sum)
            #print("sum append")
        result.append(lst)
        #print("list append")
        
    return result

def addInteceptToMatrix(mat):
    matrix = []
    for i in range(len(mat)):
        lst = mat[i][:]
        lst.insert(0,1)
        matrix.append(lst)
    return matrix

# ------- end of matrix things -----

# ------- regression things -----

def getThetas(mat, y, num_iters, alpha):
    theta = [0] * (len(mat[0]) + 1)
    X = addInteceptToMatrix(mat)
    for r in range(num_iters):
        theta = gradientDescent(X, y, theta, alpha)
    return theta

def gradientDescent(X, y, theta, alpha):
    m = len(X)
    for i in range(len(theta)):
        theta[i] = theta[i] - ((alpha/m) * derivativeSum(X, y, theta, i))
    return theta

def derivativeSum(X, y, theta, curtheta):
    m = len(X)
    col = len(X[0])
    sum = 0.0
    #dot product to get vector delta (h - y)
    vDelta = []
    for r in range(m):
        sumrow = 0.0
        for c in range(col):
            sumrow += ((X[r][c] ** c) * theta[c]) # tried the polynomial things here, maybe this is not the correct way
        delta = sumrow - y[r]
        vDelta.append(delta)

    #get the value of derivative
    for v in range(len(vDelta)):
        sum += vDelta[v] * X[v][curtheta]

    return sum

# ----------------- calc price ---------------
def calculatePrice(Xtest, theta):
    prices = []
    m = len(Xtest)
    col = len(theta)
    for r in range(m):
        sum = 0.0
        for c in range(col):
            sum += ((Xtest[r][c] ** c) * theta[c]) # following the cost calculation
        prices.append(sum)
    return prices
# ---------

# ------ __main__ -------
if __name__ == '__main__':
    f, m = input().split(' ')
    f, m = [int(f), int(m)]

    num_iters = 400
    alpha = 0.0006

    lstdata = []
    X = []
    y = []
    for x in range(m):
        rowinput = list(map(float, input().split(' ')))
        lstdata.append(rowinput)
        X.append(rowinput[:-1])
        y.append(rowinput[-1])   

    tm = int(input().strip())
    Xtest = []
    for i in range(tm):
        rowinput = list(map(float, input().split(' ')))
        Xtest.append(rowinput)
        
    thetas = getThetas(X, y, num_iters, alpha)
    #print(thetas)

    Xtest1 = addInteceptToMatrix(Xtest)
    prices = calculatePrice(Xtest1, thetas)
    for p in prices:
        print(p)