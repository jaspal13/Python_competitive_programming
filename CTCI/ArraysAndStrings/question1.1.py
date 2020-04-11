class CheckUniqueChars:
    def __init__(self):
        pass

    def run(self,s):
        '''
        Checks if input s has all unique chars or not, assume ASCII char set with max unique 128 chars
        :param s: input string
        :return: boolean true if s has all unique chars else false
        '''
        if (len(s)>128):
            return false
        #Option 1
        # char_dict = {}
        # for char in s:
        #     if char in char_dict:
        #         return False
        #     else:
        #         char_dict[char]=1
        # return True
        #Option 2
        return (len(s)==len(set(s)))

obj = CheckUniqueChars();
print(obj.run("abcda"))
