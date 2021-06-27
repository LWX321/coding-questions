
def print_matrix(matrix, top_left, top_right, bottom_right, bottom_left):
    if top_left >= top_right or top_left >= bottom_left:
        return
    
    for i in range(top_left, top_right + 1):
        print(matrix[top_left][i])

    for i in range(top_left + 1, bottom_left):
        print(matrix[i][top_right])

    for i in reversed(range(top_left, top_right + 1)):
        print(matrix[bottom_left][i])

    for i in reversed(range(top_left + 1, bottom_left)):
        print(matrix[i][top_left])

    print_matrix(matrix=matrix, top_left=top_left+1, top_right=top_right-1, bottom_right=bottom_right-1, bottom_left=bottom_left-1)


if __name__ == '__main__':

    matrix = [[1, 2, 3, 4, 5],
              [6, 7, 8, 9, 10], 
              [11,12,13,14,15], 
              [16,17,18,19,20]]

    top_left = 0
    top_right = bottom_right = len(matrix[0]) - 1
    bottom_left = len(matrix) - 1

    print_matrix(matrix, top_left, top_right, bottom_right, bottom_left)
