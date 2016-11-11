class Solution(object):
    def checkDist(self, word1, word2):
        same_count = 0
        for i in range(len(word1)):
            if word1[i] == word2[i]:
                if same_count > 1:
                    return False
                same_count += 1
        return True
        
        
    def checkAnswer(endWord, wordList):
        for word in wordList:
            if checkDist(word, endWord):
                return True
        return False
            

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        candidate_list = list(wordList)
        current_word = beginWord
        while True:
            for word in candiate_list:
                if checkDist(current_word, word):
                    candidate_list.remove(word)
                    
                
        
        
        return hops
    