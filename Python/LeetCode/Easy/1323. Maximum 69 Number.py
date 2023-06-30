class Solution:
    def maximum69Number (self, num: int) -> int:
        str_num = str(num)
        temp = num

        for i in range(len(str_num)):
            if str_num[i] == '6':
                temp_str = str_num[:i] + '9' + str_num[i+1:]
            else:
                temp_str = str_num[:i] + '6' + str_num[i+1:]
            temp = max(temp, int(temp_str))
        
        return temp
