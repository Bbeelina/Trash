# ищем количесвто инверсий
def getInvCount(arr, n):
    inv_count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (arr[i] > arr[j]):
                inv_count += 1

    return inv_count


arr = [5.5, 5.1, 5.7, 5.2, 4.8, 5.7, 5.0, 6.5, 5.4, 5.8, 6.8, 6.6, 4.9, 5.4, 5.9, 5.4, 6.8, 5.8, 6.9, 5.5]
n = len(arr)
A = getInvCount(arr, n)
print("Number of inversions are", A)
# пусть гипотеза заключается в том, что наблюдения представляют собой независимые
# исходы случайной величины х, т.е. тренда нет. Область принятия тогда будет иметь вид:
# [A(20,1-alfa/2) = A(20, 0.975) < A <= A(20, alfa/2)] пусть alfa = 0.05
low_bound = 64  # значение из таблицы
up_bound = 125
if (A > low_bound) and (A <= up_bound):
    print("The hypothesis is accepted")
else:
    print("The hypothesis is declined")