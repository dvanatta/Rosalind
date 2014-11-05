def iev(array, weights=[1, 1, 1, .75, .5, 0]):
    result = 0
    for i in range(len(array)):
        result += array[i]*weights[i]
    return result*2

print iev([18032, 19982, 17084, 17192, 17430, 18315])
