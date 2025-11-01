class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")  
        chars = list(s)

        vowel_list = [ch for ch in chars if ch in vowels]

        for i, ch in enumerate(chars):
            if ch in vowels:
                chars[i] = vowel_list.pop()  

        return "".join(chars)
