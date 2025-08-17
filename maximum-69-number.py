class Solution(object):
    def maximum69Number (self, num):
        strNum = str(num)
        if not "6" in strNum:
            return num
        number_list = list(strNum)
        index = number_list.index("6")
        number_list[index] = "9"
        number_string = "".join(number_list)
        return int(number_string)
        