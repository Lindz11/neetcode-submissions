class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        my_ans = []
        for w in words:
            for i in range(len(words)): 
                if words[i] is not w and words[i] in w:
                    my_ans.append(words[i])
        
        return list(set(my_ans))