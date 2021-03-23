
import inflect


words = {
    1 : 'one',
    2 : 'two',
    3 : 'three',
    4 : 'four',
    5 : 'five',
    6 : 'six',
    7 : 'seven',
    8 : 'eight',
    9 : 'nine',
    10 : 'ten',
    11 : 'eleven',
    12 : 'twelve',
    13 : 'thirteen',
    14 : 'fourteen',
    15 : 'fifteen',
    16 : 'sixteen',
    17 : 'seventeen',
    18 : 'eighteen',
    19 : 'nineteen',
    20 : 'twenty',
    30 : 'thirty',
    40 : 'fourty',
    50 : 'fifty',
    60 : 'sixty',
    70 : 'seventy',
    80 : 'eighty',
    90 : 'ninety',
    100 : 'hundred',
    1000: 'thousand',
}

def number_letter_count(): 
    p = inflect.engine()
    MAX_NUM = 5
    my_sum = 0
    for x in range(1, MAX_NUM+1):
        word_with_space = p.number_to_words(x)
        word_without_space = word_with_space.replace(' ', '')
        word_without_hyphen = word_without_space.replace('-', '')
        my_sum += len(word_without_hyphen)
        print(word_without_hyphen, my_sum, len(word_without_hyphen))
    return my_sum


print(number_letter_count())