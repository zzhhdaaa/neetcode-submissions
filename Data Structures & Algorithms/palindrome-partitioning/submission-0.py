class Solution:
    def partition(self, s: str) -> List[List[str]]:
        checked = dict()
        res = []

        def is_pldr(par: str) -> bool:
            if par in checked:
                return checked[par]
            
            for i in range(len(par)//2):
                if par[i] != par[len(par)-1-i]:
                    checked[par] = False
                    return False
            checked[par] = True
            return True
        
        def backtrack(i: int, pars: []):
            if i >= len(s):
                for par in pars:
                    if not is_pldr(par):
                        return
                res.append(pars.copy())
                return
            
            # create a new partition
            pars.append(s[i])
            backtrack(i+1, pars)
            pars.pop()
            # append to last partition
            pars[-1] += s[i]
            backtrack(i+1, pars)
            pars[-1] = pars[-1][0:len(pars[-1])-1]
        
        backtrack(1, [s[0]])
        return res
