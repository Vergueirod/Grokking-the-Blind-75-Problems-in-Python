word_to_validate = ['m','a','d','a','m']
#word_to_validate = ['d','i','e','g','o']
#word_to_validate = ['r','a','d','a','r']


len_array = 0

for index, value in enumerate(word_to_validate):
    len_array += 1
    print(index, value)

print(f'{len_array}')

# One start in the end of the word, and another pointer start in the beginner of the word and I need compare boths in each cicle.

invert_word_array = []

for index in word_to_validate[::-1]:
    invert_word_array.append(index)
    print(index)

print(invert_word_array)

count = 0

for i in range(0,len(word_to_validate),1):
    if word_to_validate[i] != invert_word_array[i]:
        print(f"This is not a palindrome.")
        break
    else:
        count += 1

if count == len(word_to_validate):
    print("It is a palindrome!")

    # Step 1: I need create the object for received the array.

class PalindromeChecker:

    def __init__(self, char_array):
        self.chars = char_array


enginee = PalindromeChecker(word_to_validate)
print(enginee.chars)
