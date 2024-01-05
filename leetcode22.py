class Solution(object):
    def closeStrings(self, w1, w2):
        """
        :type w1: str
        :type w2: str
        :rtype: bool
        """  
        a = list(w1)
        b = list(w2)
        c = set(a)
        d = set(b)
        s1 = list()
        s2 = list()
        
        if len(w1) == len(w2) and c == d:
            for j in c:
                s1.append(a.count(j))
                s2.append(b.count(j))
            s1.sort()
            s2.sort()
            if(s1==s2):
                return True
        
        return False
