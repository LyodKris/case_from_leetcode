class Solution:
    def uniqueMorseRepresentations(self, words):
        alphabet = {'a' : ".-", 'b' : "-...", 'c' : "-.-.", 'd' : "-..", 'e' : ".", 'f' : "..-.", 'g' : "--.", 'h' : "....", 'i' : "..", 'j' : ".---", 'k' : "-.-", 'l' : ".-..", 'm' : "--", 'n' : "-.", 'o' : "---", 'p' : ".--.", 'q' : "--.-", 'r' : ".-.", 's' : "...", 't' : "-", 'u' : "..-", 'v' : "...-", 'w' : ".--", 'x' : "-..-", 'y' : "-.--", 'z' : "--.."}
        dict = {}
        for i in range(len(words)):
            s = ""
            for j in range(len(words[i])):
                s += alphabet[words[i][j]]
            dict[s] = 0
        return len(dict)


if __name__ == '__main__':
    w = ["a"]
    a = Solution()
    print(a.uniqueMorseRepresentations(w))