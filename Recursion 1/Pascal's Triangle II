class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0:
            return [1]
        row = [1]
        p=self.getRow(rowIndex-1)
        for i in range(len(p)-1):
            row.append(p[i] + p[i + 1])
        row.append(1)
        return row
