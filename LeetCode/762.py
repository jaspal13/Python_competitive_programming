class Solution:
    def countPrimeSetBits(self, L, R):
        def is_prime(n):
            if n<=1:
                return False
            if n <=3:
                return True
            if n%2==0 or n%3==0:
                return False
            i=5
            while i*i<=n:
                if n%i==0 or n%(i+2)==0:
                    return False
                i = i+6
            return True

        def count_set_bits(n):#Brian Kernighan's algorithm
            count = 0
            while n:
                n = n & (n-1)
                count += 1
            return count
        answer = 0
        for i in range(L,R+1):
            if (is_prime(count_set_bits(i))):
                answer += 1
        return answer
s = Solution()
print(s.countPrimeSetBits(10,15))