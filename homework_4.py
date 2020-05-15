def find_unique(string):
    unique_letters = ''
    last = len(string)-1
    index = 0
    longest = ''
    while index<=last:
        if string[index] not in unique_letters:
            unique_letters+=string[index]
            index+=1
        else:
            if len(unique_letters)>len(longest):
                longest = unique_letters
            unique_letters = ''
            
    return longest



if __name__ == '__main__':
    string = 'alppkgtcect'
    print(find_unique(string))
