# Function 1
def valid_dna(sequence):
    if sequence == '':
        return False
    
    for x in sequence:
        if x not in "ATCG":
            return False
    return True

# Function 2
def count_nucleotides(sequence):
    a_count = 0 
    t_count = 0
    c_count = 0
    g_count = 0

    for x in sequence:
        if x == 'A':
            a_count += 1
        elif x == 'T':
            t_count += 1
        elif x == 'C':
            c_count += 1
        elif x == 'G':
            g_count += 1
    return (a_count, t_count, c_count, g_count)

# Function 3
def gc_content(sequence):
    total = count_nucleotides(sequence)
    c_g = total[2] + total[3]
    all = sum([x for x in total])
    answer = c_g / all * 100
    return answer

# Function 4
def complementary_dna(sequence):
    result = ''
    for x in sequence:
        if x == 'A':
            result += 'T'
        elif x == 'T':
            result += 'A'
        elif x == 'C':
            result += 'G'
        elif x == 'G':
            result += 'C'
    return result

# Function 5
def detect_subsitutions(original, mutated):
    mutations = []
    for i in range(len(original)):
        if original[i] != mutated[i]:
            mutations.append(i)
    return mutations 

# Function 6
def detect_deletions(original, mutated):
    position = 0
    for i in original:
        if original[:position] + original[position + 1:] == mutated:
            return position
        else:
            position += 1

# Function 7
def detect_insertions(original, mutated):
    position = 0
    for i in mutated:
        if mutated[:position] + mutated[position + 1:] == original:
            return position
        else:
            position += 1

    




# Stage 6: Main Program

# Part 1: Getting user Input
print('Welcome to TheCellCoded DNA Analyzer!')
sequence = input('Enter DNA Sequence: ')
# Part 2: Calling a Function to Determine if Sequence is Correct
y = valid_dna(sequence)
if y == True:
    print('Valid DNA')
    
    count = count_nucleotides(sequence)
    print('Nucelotide Count:')
    print('A Count:', count[0])
    print('T Count:', count[1])
    print('C Count:', count[2])
    print('G Count:', count[-1])
    
    c_and_g = gc_content(sequence)
    print('GC Content:', f'{round(c_and_g, 2)}%')

    opposite_DNA = complementary_dna(sequence)
    print('Complementary DNA:', opposite_DNA)

    mutated = input('Enter Your Comparison DNA Sequence: ')
    if valid_dna(mutated) == True:
        if len(mutated) == len(sequence):
            mutated_positions = detect_subsitutions(sequence, mutated)
            if mutated_positions == []:
                print('No Mutations Detected!')
            else:
                print('Mutations detected at indices', mutated_positions)
        elif len(mutated) > len(sequence):
            print('A Insertion occurs at index', detect_insertions(sequence, mutated))
        else:
            print('A Deletion occurs at index', detect_deletions(sequence, mutated))
    else:
        print('Comparison DNA invalid')


else:
    print('Invalid DNA: Restart Program')