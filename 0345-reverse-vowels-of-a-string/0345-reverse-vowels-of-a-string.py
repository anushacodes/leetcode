class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")  # faster lookup than string
        chars = list(s)

        # collect vowels in order
        vowel_list = [ch for ch in chars if ch in vowels]

        # rebuild the string, replacing vowels with reversed ones
        for i, ch in enumerate(chars):
            if ch in vowels:
                chars[i] = vowel_list.pop()  # pop from end gives reverse order

        return "".join(chars)
