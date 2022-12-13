class Solution:

    ans = []

    def totalNQueens(self, n: int) -> int:
        chess_board = [[0 for i in range(n)] for j in range(n)] 

        def in_attack_zone(row, col) -> bool:
            nonlocal chess_board
            return True if chess_board[row][col] > 0 else False 
        
        def get_position_string(i) -> str:
            return "." * i + "Q" + "." * (n-i-1)
        
        # def place_queen(row, col):
        #     nonlocal chess_board

        #     chess_board[row][col] += 1
        #     for i in range(n):
        #         chess_board[i][col]+=1
        #         chess_board[row][i]+=1
            
        #     i = row
        #     j = col 
        #     while i < n and j <n:
        #         chess_board[i][j]+= 1
        #         i+=1 
        #         j+=1
                        
        #     i = row
        #     j = col 
        #     while i >=0 and j>= 0:
        #         chess_board[i][j]+= 1
        #         i-=1
        #         j-=1


        # def remove_queen(row, col):
        #     nonlocal chess_board
        #     chess_board[row][col] -= 1
        #     for i in range(n):
        #         chess_board[i][col] -=1
        #         chess_board[row][i] -=1
            
        #     i = row
        #     j = col 
        #     while i < n and j <n:
        #         chess_board[i][j] -= 1
        #         i+=1 
        #         j+=1
            
        #     i = row
        #     j = col 
        #     while i >=0 and j>= 0:
        #         chess_board[i][j] -= 1
        #         i-=1
        #         j-=1
    

        def backtrack(row, current_solution, cols, diagonals, anti_diagonals):
             
            nonlocal count
            if row != len(current_solution):
                #couldn't place in previous row 
                return 

            if row == n:
                count += 1
                return 

            # for i in range(n):
            #     if not in_attack_zone(row, i):
            #         place_queen(row, i)
            #         current_solution.append(get_position_string(i))                        
            #         backtrack(row+1, current_solution)
            #         # if program comes here, we need to remove 
            #         current_solution.pop()
            #         remove_queen(row, i)

            for i in range(n):
                cur_diag = row - i
                cur_anti_diag = row + i
                if i in cols or cur_diag in diagonals or cur_anti_diag in anti_diagonals:
                    continue
                cols.add(i)
                diagonals.add(cur_diag)
                anti_diagonals.add(cur_anti_diag)
                current_solution.append(get_position_string(i)) 
                backtrack(row+1, current_solution, cols, diagonals, anti_diagonals)
                cols.remove(i)
                anti_diagonals.remove(cur_anti_diag)
                diagonals.remove(cur_diag)
                current_solution.pop()

        count = 0   
        backtrack(0, [], set(), set(), set()) 
        return count
