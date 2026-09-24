class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        words=set(wordList)
        if endWord not in words:
            return 0
        q=deque([(beginWord,1)])
        while q:
            word, steps=q.popleft()
            if word==endWord:
                return steps
            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    new=word[:i]+ch+word[i+1:]
                    if new in words:
                        words.remove(new)
                        q.append((new,steps+1))
        return 0
        
