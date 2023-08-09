# x = 121
# str_x = str(x)
# rev = str_x[::-1]
# rev_int = int(rev)

# print(rev_int)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x >= 0:
            strX = str(x)
            reverse = int(strX[::-1])
            if x == reverse:
                return True
        return False
    
chk = Solution()
print(chk.isPalindrome(0))