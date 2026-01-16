word_to_validate = ['m','a','d','a','m']
len_array = 0

for index, value in enumerate(word_to_validate):
    len_array += 1
    print(index, value)

print(f'{len_array}')

# One start in the end of the word, and another pointer start in the beginner of the word and I need compare boths in each cicle.