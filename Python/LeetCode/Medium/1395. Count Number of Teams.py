class Solution:
    def numTeams(self, rating: List[int]) -> int:
        asc, dsc = 0, 0
        for m in range(len(rating)):
            middle = rating[m]
            l_asc, l_dsc = 0, 0
            for l in range(0,len(rating[:m])):
                left = rating[l]
                if left < middle:
                    l_asc += 1
                else:
                    l_dsc += 1
            
            r_asc, r_dsc = 0, 0
            for r in range(len(rating[:m+1]),len(rating)):
                right = rating[r]
                if middle < right:
                    r_asc += 1
                else:
                    r_dsc += 1
            
            asc += l_asc * r_asc
            dsc += l_dsc * r_dsc
        
        return asc + dsc
