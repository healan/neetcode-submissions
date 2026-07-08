class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordDic={}
        anagrams=[]
        for word in strs:
            key = "".join(sorted(word))  
            if key not in wordDic:
                wordDic[key]=[]
            wordDic[key].append(word)
        
        for k in wordDic:
            anagrams.append(wordDic[k])
        
        return anagrams

        

        
        
   

            