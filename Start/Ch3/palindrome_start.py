# test_word = "Madam, I'm Adam."
# test_word = "RACE CAR!"
test_word = "Hello, world"
# test_word = "Radar?"
# test_word = "A man, a plan, a canal Panama!"

print(test_word)

def is_palindrome(teststr):
    s = []
    palindrome = False
    teststr = teststr.lower()
    

    for c in range(len(teststr)):
        if teststr[c].isalpha() :
            s += teststr[c]
        
   

    for i in range(len(s)):
        if s[i] == s[len(s) - i - 1]:
            palindrome = True
        else :
            palindrome = False
  
    print(f"{test_word} is a palindrome? {palindrome}")
    return palindrome


is_palindrome(test_word)