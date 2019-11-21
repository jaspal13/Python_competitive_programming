import math
class Solution(object):
    def pathInZigZagTree(self, label):
        """
        :type label: int
        :rtype: List[int]
        """
        answer = []
        def findCorrectPlace(n):
            if int(math.log(n,2))%2==0:
                return n
            else:
                return ((math.pow(2,int(math.log(n,2))+1)-1)-n)+math.pow(2,int(math.log(n,2)))
        def findParent(n):
            if int(math.log(n,2))%2==0:#even depth
                parent = findCorrectPlace(int(n/2))
            else:
                parent = int(findCorrectPlace(n)/2)
            return int(parent)
        answer.append(label)
        while label!=1:
            x = findParent(label)
            answer.append(x)
            label = x
        return answer[::-1]

s = Solution()
print(s.pathInZigZagTree(5))