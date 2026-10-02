class Solution:
    def replaceWords(self, dictionary, sentence):
        root = {}

        for word in dictionary:
            cur = root
            for ch in word:
                cur = cur.setdefault(ch, {})
            cur["#"] = True

        def find(word):
            cur = root
            prefix = ""

            for ch in word:
                if ch not in cur:
                    return word

                prefix += ch
                cur = cur[ch]

                if "#" in cur:
                    return prefix

            return word

        return " ".join(find(word) for word in sentence.split())
