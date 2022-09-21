class Solution:
    def isValid(self, s: str) -> bool:
        #key value pairs of brackets
        hashmap = { ")" : "(", "]" : "[", "}" : "{"}
        munchstack = []

        #check if string is uneven, if it is then just return false
        #unevenstr = len(s) % 2
        #if unevenstr != 0:
	     #   return False
        
        for i in s:
            if i in hashmap:
                if munchstack and munchstack[-1] == hashmap[i]:
                    munchstack.pop()
                else:
                    return False
            else:
                munchstack.append(i)
        
        if not munchstack:
            return True
        else:
            return False
