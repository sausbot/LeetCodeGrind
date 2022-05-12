'''
Interview Question
How many characters should be added to the string such that every character sequence is repeated the same number of tiemes

Input String: "baaabb"
Desired String: "bbbaaabbb"
Characters to add: 3
'''
def solution(S):
    # convert string to list
    seq = list(S)
    first_letter = seq[0]
    length = len(seq) - 1
    
    i = 1
    seq_count = 1
    max_seq_count = 1
    seq_count_save = []

    # Iterate through the list
    while i <= length:
        next_letter = seq[i]
        
        # Count while you find consecutive letters
        if next_letter == first_letter:
            seq_count +=1
        
        # When it is not consecutive append the prev count
        else: 
            seq_count_save.append(seq_count)
            
            # Save the max count
            if seq_count > max_seq_count:
                max_seq_count = seq_count
            seq_count = 1

            # handle the last letter case
            if i == length:
                seq_count_save.append(seq_count)
        i+=1
        # next letters to be checked
        first_letter = next_letter

    # See how many letters we should add
    letters_to_add = 0
    for count in seq_count_save:
        if count < max_seq_count:
            letters_to_add += max_seq_count - count

    return letters_to_add

# test
a = solution("babba")
print(a)
b = solution("bbabab")
print(b)
c = solution("bbbaaabbb")
print(c)