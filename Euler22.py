'''Open the file, read in the text, break it into letters, divide by commas, add to list'''
name_letters = []
the_name_list = []
with open('c:\\HTML\\p022B_names.txt', 'r') as names_to_be_read:
    for line in names_to_be_read:
        for letter in line:
            if letter != ",":
                if letter != "\"":
                    name_letters.append(letter)
            else:
                the_name_list.append(name_letters)
                name_letters = []
'''Close file'''
names_to_be_read.close()

print(the_name_list)
the_name_list.sort()
print(the_name_list)

sum = 0
mult = 0
total_sum = 0
for parse_name_list in range(0, len(the_name_list)):
    for l in range(0, len(the_name_list[parse_name_list])):
        sum += (ord(the_name_list[parse_name_list][l].upper()) - 64)
    mult = sum * parse_name_list
    total_sum += mult
print(total_sum)