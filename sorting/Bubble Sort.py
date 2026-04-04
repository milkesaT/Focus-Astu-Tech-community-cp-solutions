def sortbubble(a):
    count = 0 
    n = len(a)
    for i in range(n):
        for j in range(n - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                count += 1 
    return a, count
n = int(input())
arr = list(map(int, input().split()))
result, count = sortbubble(arr)
print("Array is sorted in " + str(count) + " swaps.")
print("First Element: " + str(result[0]))
print("Last Element: " + str(result[-1]))
