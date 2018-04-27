with open('raw.txt', "r") as input_file:
    for line in input_file:
        input_clean = line.replace('!', '.')
    input_clean = input_clean.replace('?', '.')
    input_clean = line.replace('Mr.', 'Mr')
    input_clean = line.replace('Mrs.', 'Mrs')
print(input_clean)
for line in input_clean:
    sentence_list = input_clean.split('. ')

#print(sentence_list)