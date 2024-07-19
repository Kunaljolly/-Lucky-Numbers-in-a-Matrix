class Solution:
    @staticmethod
    def luckyNumbers(matrix: list[list[int]]) -> list[int]:
        
        # row mins
        rmin = [min(x) for x in matrix]
        print(*matrix)
        print(zip(matrix))
        print(zip(*matrix))

        # col maxs
        cmax = [max(x) for x in zip(*matrix)]

        return list(set(rmin) & set(cmax))
