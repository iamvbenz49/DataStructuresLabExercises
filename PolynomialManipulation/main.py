def add(poly1,poly2):
    max_degree = max(len(poly1),len(poly2))
    res  = [0]*max_degree
    for index,number in enumerate(poly1[::-1]):
        res[index] += number
    for index,number in enumerate(poly2[::-1]):
        res[index] += number
    return res[::-1]
def multiply(poly1,poly2):
    max_degree = len(poly1) + len(poly2) -1
    res = [0]*max_degree
    for i,n1 in enumerate(poly1[::-1]):
        for j,n2 in enumerate(poly2[::-1]):
            res[i+j] += n1*n2
    return res[::-1]
def display(poly1):
    res = []
    for degree,coeff in enumerate(poly1[::-1]):
        res.append(f"{coeff}x^{degree}")
    return "+".join(res[::-1])
poly1 = [2,0,1]
poly2 = [1,3]
print("Polynomial 1 : ",display(poly1))
print("Polynomial 2 : ",display(poly2))
print("Sum : ",display(add(poly1,poly2)))
print("Product : ",display(multiply(poly1,poly2)))