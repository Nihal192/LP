
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]  # res will record the previous rows.
        for i in range(numRows - 1):  # out_of_bounds check karvu
            temp = [0] + res[-1] + [0]  # temp ni andar logic che ke 0+value+0 jeanthi new row apde form kari sakiye
            row = []  # this is the new row apde ane build karisu next for loop ma which is J.
            for j in range(len(res[-1]) + 1):
                row.append(temp[j] + temp[j + 1])  # ahiya j is pointer jenathi apde check kariye
            res.append(row)
        return res
