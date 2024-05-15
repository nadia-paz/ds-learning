class Solution:
    """
    Given an integer x, return true if x is a palindrome, and false otherwise.
    Input: x = 121
    Output: true
    Input: x = -121
    Output: false
    """
    def isPalindrome(self, x: int) -> bool:
        # much faster
        num_string = str(x)
        return num_string == num_string[::-1]

    def isPalindrome1(self, x: int) -> bool:
        num_string = str(x)
        for i in range(int(len(num_string) / 2)):
            if num_string[i] != num_string[0-1-i]:
                return False
                break
            else:
                return True
        

if __name__=="__main__":
    a = Solution()
    print("False Return")
    print(a.isPalindrome(-121))
    print(a.isPalindrome1(-121))
    print("\nTrue Return")
    print(a.isPalindrome(121))
    print(a.isPalindrome1(121))