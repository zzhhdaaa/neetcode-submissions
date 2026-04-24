class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split("/")
        res = []

        for p in paths:
            if p == "..":
                if res:
                    res.pop()
            elif p != "" and p != ".":
                res.append(p)
        
        return "/" + "/".join(res)