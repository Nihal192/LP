class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        output=[1] # ahiya apde list of list na balde sirf list laisu to make sure we use o(k) only
        for i in range(1,rowIndex+1):
            output.append(1)  #we have append the result instead of taking new temp variable like we did in normal pascal triangle
            for j in range(len(output)-2,0,-1): # loop for tracking/going backwards
                output[j] += output[j-1]
        return output     
