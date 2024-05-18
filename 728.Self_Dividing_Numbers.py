
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for i in range(left, right+1):
            count = 0
            if "0" in str(i):
                continue 
            for j in str(i):
                if i % int(j) != 0:
                    break
                count +=1
            if count == len(str(i)):
                result.append(i)
        return result
    