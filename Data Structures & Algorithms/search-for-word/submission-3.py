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
            if board[r][c] != search[0]:
                return False

            if len(search)==1:
                return True
            
            visited.add((r,c))

            # print("row-col",r,c,"word",search)
            # print("visited",visited)
            # print()

            # print(board[r][c], search[0])

            a,b,d,e = False,False,False,False
            if r+1<len(board) and (r+1,c) not in visited:
                a = recurse(r+1,c,search[1:])
            if r>0 and (r-1,c) not in visited:
                b = recurse(r-1,c,search[1:])
            if c+1<len(board[0]) and (r,c+1) not in visited:
                d = recurse(r,c+1,search[1:])
            if c>0 and (r,c-1) not in visited:
                e = recurse(r,c-1,search[1:])
            
            visited.remove((r,c))

            return (a | b | e | d)
        
        
        for i in start_idx:
            if recurse(i[0],i[1], word) == True:
                return True

        return False
        