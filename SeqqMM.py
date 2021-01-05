import numpy as np

# the order used for the matricies
convert = {'A': 0, 'C': 1, 'T': 2, 'G': 3}

# return a list of the 100 training examples
def read_sequences(file_string):
    # remove the next line characters and make every character upper case
    # then split the string by '>'
    # then take the substring starting at index 1 because the first 
    # line is just the title of text file
    split_str = file_string.replace('\n','').upper().split(">")[1:]

    # make each element of the array constist of only the sequence, so after the period
    # in the title for each sequence
    # sequence_vector = np.array([seq[(seq.index('.') + 1):]  for seq in split_str])
    sequence_list = [seq[(seq.index('.') + 1):]  for seq in split_str]
    return sequence_list

# compute the transition matrix
def compute_transition_matrix(sequences):
    # row and column order: A, C, T, G
    # transition matrix
    P = np.zeros([4,4])

    # start probabilities
    pi = np.zeros([4,1])

    # first compute the number of pairs
    for seq in sequences:
        pi[convert[seq[0]]] += 1
        
        current = seq[0]
        for next in seq[1:]:
            P[convert[current], convert[next]] += 1
            current = next

    # starting probability
    pi = pi / 100
    # column vector with each row representing the sum or the row in P
    row_sums = np.sum(P, axis = 1)
    row_sums = row_sums.reshape(4,1)

    # ADD A CHECK FOR DIVIDE BY ZERO
    if [0] in row_sums:
        print("Cant divide by Zero, not all pairs are represented")
        exit()
    # divide each element element-wise in P by the sum of the row to get the probabilities
    # uses broadcasting
    P = P / row_sums
    # compute probabilities by doing P[i,j] = P[i,j] / np.sum(i th row, axis = 1)
    return P, pi

# compute the probability of the test sequence
def compute_test_probability(sequence, P, pi):
    # using the convert dict, get the index given nucliotide
    prob = np.log(pi[convert[sequence[0]]])
    current = sequence[0]
    for next in sequence[1:]:
        prob += np.log(P[convert[current], convert[next]])
        current = next
    # prob is an array, so make it just a number
    return prob.squeeze()

def main():
    with open("sequences.txt", "r") as input_file:
        train_str = input_file.read()
        train_sequences = read_sequences(train_str)
        test_file = open("test.txt", "r")
        test_seq = read_sequences(test_file.read())
        P, pi = compute_transition_matrix(train_sequences)
        log_prob = compute_test_probability(test_seq[0], P, pi)
        print("Probability (log base e probability) for first order MM:", log_prob)
        # print("Transition Matrix:")
        # print(P)
        # print("Starting Probabilities: ")
        # print(pi)
    
if __name__ == "__main__":
    main()


  