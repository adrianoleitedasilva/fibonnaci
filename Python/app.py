def fibonnaci(num):

    # exception numero negativo
    if num < 0:
        raise Exception("Num precisa ser um número inteiro e positivo!")

    res = []
    prev, curr = 0, 1

    for i in range(num):
        res.append(curr)
        # curr passa a ter seu valor após somarmos curr + prev
        # prev passa a ter o valor de curr
        curr, prev = curr + prev, curr

    print(res)
    return res
    
fibonnaci(5)
fibonnaci(0)
fibonnaci(-5)