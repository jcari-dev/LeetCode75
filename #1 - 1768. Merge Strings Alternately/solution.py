class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        longest = word1 if len(word1) > len(word2) else word2
        shortest = word2 if word1 == longest else word1

        merge = []
        for index, letter in enumerate(shortest):
            merge.append(word1[index])
            merge.append(word2[index])
        
        merge.append(longest[len(shortest):])

        return "".join(merge)