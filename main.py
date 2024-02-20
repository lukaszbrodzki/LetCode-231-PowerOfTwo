class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        pow = 0

        while True:
            res = 2**pow
            if res == n:
                return True
            elif res > n:
                return False
            pow += 1


if __name__ == '__main__':
    s = Solution()
    n = 16
    print(s.isPowerOfTwo(n))
