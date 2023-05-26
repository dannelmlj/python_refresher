def numSubmat( matrix: list[list[int]]):
        n = len(matrix)
        m = len(matrix[0])
        to_right = [[0] * m for _ in range(n)]
        for i in range(n):
            counter = 0
            for j in range(m-1,-1,-1):
                if matrix[i][j] == 1:
                    counter += 1
                else:
                    counter = 0
                to_right[i][j] = counter
                   
        output = 0
        for j in range(m):
            my_stack = []
            temp_sum = 0
            for i in range(n-1,-1,-1):
                c = 0
                while (len(my_stack) != 0) and (my_stack[-1][0] > to_right[i][j]):
                    temp_sum -= (my_stack[-1][1] + 1) * (my_stack[-1][0] - to_right[i][j])
                    c += my_stack[-1][1] + 1
                    my_stack.pop()
                temp_sum += to_right[i][j]
                output += temp_sum
                my_stack.append([to_right[i][j], c])
        
        return output



matrix = [[0,1,1,0],[0,1,1,1],[1,1,1,0]]
print(numSubmat(matrix))

        