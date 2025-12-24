# 2. Given a list of strings, 
# write a program to group the words into sub-lists where each sub-list contains only words that are anagrams of each other.
def group_anagrams(words):
    anagram_list = []
    while words:
        word = words[0]
        words.remove(word)
        # print(words)
        #create sub-list for anagrams
        anagrams = [word]
        # print(anagrams)
        for other_word in words:
            if sorted(word) == sorted(other_word):
                anagrams.append(other_word)
                words.remove(other_word)

        anagram_list.append(anagrams)

    return anagram_list


words = ['tac', 'net', 'cat', 'ent', 'left', 'act', 'felt', 'ten']
print(group_anagrams(words))
    