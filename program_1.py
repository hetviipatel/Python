name = input("enter your name=")

reverse_name = name[::-1]
if(name == reverse_name):
    print("given strings is palindrome")
else:
    print("given string is not palindrome")

vowels_count = 0
consonant_count = 0
for ch in name:
    if ch in 'aeiouAEIOU':
        vowels_count = vowels_count+1
    else :
        consonant_count = consonant_count+1
print("vowels are=",vowels_count)
print("consonants are=",consonant_count)


update_name = name.lower()
print("lowercase string is=",update_name)
        