def alpha_sequence_order(str1):
    words=str1.split('-')
    words.sort()
    new_string='-'.join(words)
    print(new_string)
    return new_string
str2="green-red-yellow-black-white"
alpha_sequence_order(str2)