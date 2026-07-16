class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # print(board.index("C"))
        start_idx = [] 
        for i,n in enumerate(board):
            for j,k in enumerate(n):
                if k == word[0]:
                    start_idx.append([i,j])
        
        visited = set()
        
        def recurse(r,c,search):
            # if board[r][c] != search[0]:
            #     return False
            
            if r<0 or c<0 or r>=len(board) or \
                        c>=len(board[0]) or \
                            (r,c) in visited or \
                                board[r][c] != search[0]:
                return False
            
            if len(search)==1:
                return True
            
            visited.add((r,c))
                 
            res = (
                    recurse(r+1,c,search[1:]) or 
                    recurse(r-1,c,search[1:]) or 
                    recurse(r,c+1,search[1:]) or 
                    recurse(r,c-1,search[1:])
                )
            
            visited.remove((r,c))
            return res
        
        
        for i in start_idx:
            if recurse(i[0],i[1], word) == True:
                return True

        return False
        