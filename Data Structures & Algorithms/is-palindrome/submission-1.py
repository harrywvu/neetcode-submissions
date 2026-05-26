class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == "": return True

        # remove non alpha_num characters
        no_non_alphanum = "".join(char for char in s if char.isalnum())

        #turn into lowercase
        s = no_non_alphanum.lower()

        i = 0
        j = int(len(s)) - 1

        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        
        return True

