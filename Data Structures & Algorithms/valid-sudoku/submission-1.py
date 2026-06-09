class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        

            # maybe do a check here 
            thrxthr = [False] * 9
            col_chk = [False] * 9
            row_chk = [False] * 9

            thrCheck = defaultdict(list)

            


        # row check 
            for i in range(0,len(board)):
                row_chk = [False] * 9 # restart the row 

                for j in range(0,len(board[i])):
                    if board[i][j] != "." : 
                        num = int(board[i][j]) -1 

                        if row_chk[num] == True: 
                            print("THIS IS ROW CHECK")
                            return False 
                        else:
                            row_chk[num] = True 

            # col check 
            for i in range(0,len(board)):
                col_chk = [False] * 9 # restart the col 

                for j in range(0, len(board[i])):
                  #  print("THIS IS J:", j)

                    if board[j][i]  != ".":
                        num = int(board[j][i]) -1

                        if col_chk[num] == True: 
                             print("THIS IS COL CHECK")
                             return False 
                        else:
                            col_chk[num] = True

            # thr by thr check 
            for i in range(0,len(board)):
                for j in range(0,len(board[i])):
                    
                        if board[i][j] != ".":
                          #  num = int(board[i][j]) -1

                            key = (i//3, j//3)
                          #  print("THIS IS CAUSEING AN ERROR", board[i//3][j//3], type(board[i//3][j//3]))

                            if board[i][j] in thrCheck[key]: 
                                #  print(board[i][j], "and", )
                                #  print("THIS IS 3 BY 3 CHECK")
                                #  print("THIS IS THE SET:", thrCheck)
                                 return False

                            else:
                                
                                thrCheck[key] += [board[i][j]]
                              #  print("THIS IS THE SET:", thrCheck)



                

            return True # if falses weren't thrown then true

                        
            