class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        if temperatures == []:
            return 0
        
        result = [0 for i in range(len(temperatures))]
        temps = {}
        for i in range(len(temperatures))[::-1]:
            day = str('inf')
            for temp in range(temperatures[i]+1, 101):
                if temp in temps:
                    day = min(day, temps[temp]-i)
            
            if day != str('inf'):
                result[i] = day
            temps[temperatures[i]] = i
    
        return result
