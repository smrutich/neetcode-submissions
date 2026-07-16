class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res,temp = [],[]
        # openopt = ['(']*n
        # closeopt = [')']*n
        count = defaultdict(int)


        def recurse(ind):
            print(ind)

            for i in ['(',')']:
                if i == ')':
                    if count['('] <= count[')']:
                        return 
                if i == '(':
                    if count['(']>=n:
                        continue
                print("temp",temp,count)

                temp.append(i)
                count[i] = count.get(i,0)+ 1

                recurse(ind+1)

                if len(temp)==n*2:
                    res.append(''.join(temp.copy()))

                c = temp.pop()
                count[c] -= 1

        recurse(0)
        return res




        