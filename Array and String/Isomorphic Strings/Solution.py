def isIsomorphic(self, s: str, t: str) -> bool:
    ds = {}
    dt = {}
    for i in range(len(s)):
        c1, c2 = s[i], t[i]
        if (c1 in ds.keys() and ds[c1] != c2) or (c2 in dt.keys() and dt[c2] != c1):
            print(dt)
            return False
        else:
            ds[c1] = c2
            dt[c2] = c1
    return True
