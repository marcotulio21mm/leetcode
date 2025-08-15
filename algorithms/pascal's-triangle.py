class Solution(object):
    def generate(self, numRows):
        response = []
        if numRows <= 0:
            return response
        
        for i in range(numRows):
            sublist = []
            for j in range(i + 1):
                if i == j or j == 0:
                    sublist.append(1)
                else:
                    previousRowSamePosition = response[i-1][j]
                    previousRowPreviousPosition = response[i-1][j-1]
                    sumValue = previousRowPreviousPosition + previousRowSamePosition
                    sublist.append(sumValue)
            response.append(sublist)                
        return response