class Solution:
    def longestCommonPrefix(self, v: list[str]) -> str:
        llpString = ""
        v.sort()
        firstWord = v[0]
        lastWord = v[-1]
        minRange = min(len(firstWord), len(lastWord))

        for i in range(minRange):
            if(firstWord[i]!=lastWord[i]):
                return llpString
            llpString += firstWord[i]
        return llpString 

chk = Solution()
print(chk.longestCommonPrefix(["dog","racecar","car"]))

# ["flower","flow","flight"]