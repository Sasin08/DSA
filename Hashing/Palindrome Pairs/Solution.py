class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        res = []
        d={word[::-1]:i for i, word in enumerate(words)}
        for i,word in enumerate(words):
            if "" in d and d[""]!=i and word==word[::-1]:
                res.append([i,d[""]])
            for j in range(1,len(word)+1):
                l=word[:j]
                r=word[j:]
                if l in d and d[l]!=i and r==r[::-1]:
                    res.append([i,d[l]])
                if r in d and d[r]!=i and l==l[::-1]:
                    res.append([d[r],i])
        return res

---------------------------------------------------------------------------------------------------------------------------------------------
#Explantion:
def palindromePairs(self, words: List[str]) -> List[List[int]]:
    res = []
    
    """Step 1: Create a dictionary where the key is the reversed word and the value is its index.
    This helps in quick lookup for reversed words later.
    Example: words = ["bat", "tab", "cat"]
    d = {"tab": 0, "bat": 1, "tac": 2}"""
    d = {word[::-1]: i for i, word in enumerate(words)}
    
    # Step 2: Loop through each word to find valid palindrome pairs
    for i, word in enumerate(words):
        
        """Case 1: If there's an empty string in the list and the current word is a palindrome,
        we can pair the word with the empty string in both orders.
        Example: ["", "aba"] => "aba" + "" = "aba" is a palindrome"""
        if "" in d and d[""] != i and word == word[::-1]:
            res.append([i, d[""]])
        
        # Case 2: Try all possible ways to split the word into two parts: left (l) and right (r)
        for j in range(1, len(word)+1):  # start from 1 to avoid empty left side
            l = word[:j]   # left part
            r = word[j:]   # right part
            
            """Case 2a: If left part's reverse exists in dictionary and right part is a palindrome,
            then the current word + that matching word will form a palindrome.
            Example: word = "bat", l = "b", r = "at"
            If there's a word "b" (i.e., "b"[::-1] = "b") in the list, and "at" is a palindrome,
            then "bat" + "b" = "batb" can be a palindrome if "at" is a palindrome."""
            if l in d and d[l] != i and r == r[::-1]:
                res.append([i, d[l]])
            
            """Case 2b: If right part's reverse exists and left part is a palindrome,
            then that matching word + current word will form a palindrome.
            Example: word = "tab", l = "ta", r = "b"
            If "b"[::-1] = "b" exists and "ta" is a palindrome, then "b" + "tab" = "btab" """
            if r in d and d[r] != i and l == l[::-1]:
                res.append([d[r], i])
    
    return res
