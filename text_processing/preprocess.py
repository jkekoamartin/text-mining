with open('raw.txt', "r") as input_file:
    for line in input_file:
        input_clean = line.replace('! ' , '. ')
    for line in input_clean:
        input_clean = line.replace('? ', '. ')
    for line in input_clean:
        input_clean = line.replace('Mr. ', 'Mr ')
    for line in input_clean:
        input_clean = line.replace('Mrs. ', 'Mrs ')

    for line in input_clean:
        sentence_list = input_clean.split('. ')

print(sentence_list)