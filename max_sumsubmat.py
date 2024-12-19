def max_sum_submatrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    max_sum = float('-inf')
    for left in range(cols):
        temp = [0] * rows
        for right in range(left, cols):
            for i in range(rows):
                temp[i] += matrix[i][right]
            maxx_sum = maxx(temp)
            if maxx_sum > max_sum:
                max_sum = maxx_sum
    return max_sum
def maxx(arr):
    max_sum = float('-inf')
    curr_sum = 0
    for i in range(len(arr)):
        curr_sum += arr[i]
        if curr_sum > max_sum:
            max_sum = curr_sum
        if curr_sum < 0:
            curr_sum = 0
    return max_sum
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
matrix = []
print("Enter the elements of the matrix : ")
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)
max_sum = max_sum_submatrix(matrix)
print("Maximum sum submatrix: ", max_sum)



