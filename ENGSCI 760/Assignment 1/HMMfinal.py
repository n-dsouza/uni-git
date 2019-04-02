import numpy as np
from collections import Counter

def constructEmissions(pr_correct,adj):
    ## This function takes in a matrix detailing the adjacent letters
    #  on a keyboard, and the probability of hitting the correct key 
    #  and outputs a matrix of emission probabilities
    ## INPUT
    # pr_correct - the probability of correctly hitting the intended 
    #               key;
    # adj - a 26 x 26 matrix with adj[i][j] = 1 if the i'th letter 
    #               in the alphabet is adjacent
    # to the j'th letter.
    # OUTPUT
    # b - a 26 x 26 matrix with b[i][j] being the probability of 
    #               hitting key j if you intended to hit key i 
    #               (the probabilities of hitting all adjacent 
    #               keys are identical).

    adj = np.array(adj)
    b = np.float32(adj)
    m = len(b)

    for i in range(m):
        rowSum = sum(b[i]) # Number of keys adjacent to intended key
        
        # Assign probabilities (equally) that intended key is NOT 
        # hit correctly
        for j in range(m):
                if (b[i,j] == 1):
                    b[i,j] = (1-pr_correct)/rowSum
        
        # Assign probability that the intended key IS hit 
        # correctly (0.5)
        b[i,i] = pr_correct
    
    return b

def constructTransitions(filename):
    # This function constructs tranisition matricies for lowercase 
    #  characters. It is assumed that the file 'filename' only 
    #  contains lowercase characters and whitespace.
    ## INPUT
    #  filename - is the file containing the text from which we 
    #               wish to develop a Markov process.
    ## OUTPUT
    #  p - is a 26 x 26 matrix containing the probabilities of  
    #               transition from a state to another state, based
    #               on the frequencies observed in the text. 
    #  prior - is a vector of prior probabilities based on how often
    #               each character appears in the text

    ## Read the file into a sting called text
    with open(filename, 'r') as myfile:
        text = myfile.read()

    # Use a large corpus of text to determine probabilities 
    #   of characters' occurrences
    
    # Object containing frequency of characters' occurrences
    res = Counter(text) 
    
    # Character frequency array
    prior = np.array([res[chr(i)] for i in range(97,123)]) 
    
    prior = prior/sum(prior) # Convert to probabilities
    numUniques = len(prior) # Number of unique characters

    # Define ranking function to convert characters a-z 
    # to integers from 0-25
    def rank(c):
        charRank = ord(c) - ord('a')
        if charRank < 0: # If character is "space"
            # Set an arbitrarily high value to exclude whitespace
            charRank = 999 
        return charRank

    # Convert ALL characters to integers (rank!)
    R = [rank(c) for c in text] 
    
    # Initialise vector of transition probabilities
    p = np.zeros((26,26))
    
    # Record frequency of EVERY possible tuples of characters 
    # (excl. whitespace)
    for (i,j) in zip(R,R[1:]): 
        if (i<numUniques) & (j<numUniques):
            p[i,j] += 1

    # Convert frequency array to probabilities
    for row in p:
        if sum(row) > 0:
            row[:] = [r/sum(row) for r in row]

    return (p, prior)

def HMM(p,pi,b,y):
    ## This function implements the Viterbi algorithm, to find 
    #   the most likely sequence of states given some set  
    #   of observations.
    ## INPUT
    #  p  - is a matrix of transition probabilies for states x;
    #  pi - is a vector of prior distributions for states x;
    #  b  - is a matrix of emission probabilities;
    #  y  - is a vector of observations.
    ## OUTPUT
    #  x  - is the most likely sequence of states, given the inputs.

    n=len(y) # Mumber of letters in /word/
    m=len(pi) # Mumber of characters in /language/

    # Initialise Matrices
    gamma = np.zeros((m,n)) # Joint probability of most likely 
                            # state sequence ending in state 'k'
    phi = np.zeros((m,n)) # Record of state in previous time period

    gamma[:,0] = b[:,y[0]] * pi[:] # initialisation step

    for t in range(1,n): # for each time step (each obsn)
        for k in range(m): # for each state 
            array = []

            # array = transition(j->k) * joint_prob 
            # (i.e. most likely state seq. ending @ j)
            array = [p[j,k] * gamma[j,(t-1)] for j in range(m)]

            # greatest joint probability
            gamma[k,t] = b[k,y[t]] * max(array)

            # most likely previous state (argmax) 
            phi[k,t] = array.index(max(array)) 

    # Initialise vector for "most likely state"
    best=0
    x=[]
    for t in range(n):
        x.append(0)

    # Find the final state in the most likely sequence x(n).
    for k in range(m):
        if best<=gamma[k,n-1]:
            best=gamma[k,n-1]
            x[n-1]=k

    # Backtrack through matrix of "most likely previous state" 
    # to find most likely state sequence (as a whole)
    for i in range(n-2,-1,-1):
        x[i] = int(phi[x[i+1],i+1])
        
    return x

def main():
    # The text messages you have received.
    msgs=[]
    msgs.append('cljlx ypi ktxwf a pwfi psti vgicien aabdwucg vpd me and vtiex voe zoicw')
    msgs.append('qe qzby yii tl gp tp yhr cpozwdt fwstqurzby')
    msgs.append('qee ypi xfjvkjv ygetw ib ulur vae')
    msgs.append('wgrrr zrw uiu')
    msgs.append('hpq fzr qee ypi vrpm grfw')
    msgs.append('qe zfr xtztvkmh')
    msgs.append('wgzf tjmr will uiu xjoq jp ywfw')

    #The probability of hitting the intended key.
    pr_correct= 0.5

    # An adjacency matrix, adj(i,j) set to 1 if the i'th letter 
    #   in the alphabet is next to the j'th letter in the 
    #   alphabet on the keyboard.
    adj=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,1],
         [0,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0],
         [0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0],
         [0,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,0,0],
         [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,0,0],
         [0,0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0],
         [0,1,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,1,0],
         [0,1,0,0,0,0,1,0,0,1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,1,0],
         [0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0],
         [0,0,0,0,0,0,0,1,1,0,1,0,1,1,0,0,0,0,0,0,1,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,1,1,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,1,0,0,0,0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,1,0,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
         [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],
         [0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
         [1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1],
         [0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0],
         [0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
         [0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0],
         [0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1],
         [0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0],
         [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0]]

    # Call a function to construct the emission probabilities 
    #   of hitting a key given you tried to hit a 
    #   (potentially) different key.
    b=constructEmissions(pr_correct,adj)

    # Call a function to construct transmission probabilities 
    #   and a prior distribution from the King James Bible.
    [p, prior]=constructTransitions('bible.txt')
        
    # Run the Viterbi algorithm on each word of the messages 
    #   to determine the most likely sequence of characters.
    for msg in msgs:
        #divide each message into a list of words
        s_in = msg.split(' ') 

        output=''
        
        for i in range(len(s_in)):
            y=[]
            
            for j in range(len(s_in[i])):
                #convert the letters to numbers 0-25
                y.append(ord(s_in[i][j])-97) 
            
            x=HMM(p,prior,b,y) #perform the Viterbi algorithm
            
            for j in range(len(x)):
                #convert the states x back to letters
                output=output+chr(x[j]+97) 
                  
            if i!=len(s_in)-1:
                output=output+' ' #recreate the message

        print(msg) #display received message
        print(output) #display decoded message
        print('')

if __name__ == "__main__":
    main()