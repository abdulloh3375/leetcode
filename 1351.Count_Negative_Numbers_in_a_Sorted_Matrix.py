
class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        grid.sort()
        ls = []
        for i in grid:
            
            for j in i:
                if j < 0:
                    ls.append(j)
        return len(ls)
        if grid == 0:
            return None
        