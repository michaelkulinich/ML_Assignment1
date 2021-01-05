# ML_Assignment1
The file sequences.txt consists of 100 DNA sequences of 10000 nucleotides each. In Python, using this file as training data, implement the following:

1. A first order Markov Chain

Once you have trained each model, use the model to compute the probability that the DNA sequence in test.txt was generated from each model.

You should write your code in a single Python file named SeqMM.py. Your code should train all models and output the computed probabilities simply by running the command "python3 SeqMM.py". You may assume sequences.txt and test.txt are in the same directory as SeqMM.py. The output of the program should consist of exactly 2 lines printed to the terminal of the form:

Probability for first order MM: X

Where X is the computed probabilities.
