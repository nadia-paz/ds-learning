def minkowski_distance(a, b, p = 1):
    # len(a) = len(b)
    distance = 0

    #based on formula D(x, y) = sum(abs(xi - yi)^p)^(1/p)
    for d in range(len(a)):
        distnce += abs(a[d] - b[d]) ** p

    return distance ** (1/p)

def manhattan_distance(a, b, p):
    #sum(abs(xi - yi))
    #or the same as minkowski distance with p = 1
    return minkowski_distance(a, b, 1)

def euclidean_distance(a, b, p):
    #sqrt(sum((xi - yi)^2))
    #or the same as minkowski distance with p = 2
    return minkowski_distance(a, b, 2)
