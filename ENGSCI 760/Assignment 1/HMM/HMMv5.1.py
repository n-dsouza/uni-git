def constructEmissions():
    ## This function takes in a matrix detailing the adjacent letters on a keyboard, and the
    #  probability of hitting the correct key and outputs a matrix of emission probabilities
    #
    ## INPUT
    # pr_correct - the probability of correctly hitting the intended key;
    # adj - a 26 x 26 matrix with adj[i][j] = 1 if the i'th letter in the alphabet is adjacent
    # to the j'th letter.
    #
    # OUTPUT
    # b - a 26 x 26 matrix with b[i][j] being the probability of hitting key j if you intended
    # to hit key i (the probabilities of hitting all adjacent keys are identical).

    # state 0 is low
    b = [[0.4,0.5,0.1,0],[0.1,0.2,0.5,0.2]]
    return b

def constructTransitions():
    # This function constructs tranisition matricies for lowercase characters.
    # It is assumed that the file 'filename' only contains lowercase characters
    # and whitespace.
    ## INPUT
    #  filename is the file containing the text from which we wish to develop a
    #  Markov process.
    #
    ## OUTPUT
    #  p is a 26 x 26 matrix containing the probabilities of transition from a
    #  state to another state, based on the frequencies observed in the text.
    #  prior is a vector of prior probabilities based on how often each character
    #  appears in the text

    prior = [0.5, 0.5]
    p = [[0.7,0.3],[0.3,0.7]] # Row: LH, col: HL
    #p = [[0.3,0.7],[0.7,0.3]] # try instead... then it goes HL, HL on both row and col...

    return (p, prior)

def HMM(p,pi,b,y):
    ## This function implements the Viterbi algorithm, to find the most likely
    # sequence of states given some set of observations.
    #
    ## INPUT
    #  p is a matrix of transition probabilies for states x;
    #  pi is a vector of prior distributions for states x;
    #  b is a matrix of emission probabilities;
    #  y is a vector of observations.
    #
    ## OUTPUT
    # x is the most likely sequence of states, given the inputs.

    n=len(y) # length of word - i.e. number of letters in word (y = obsn)
    m=len(pi) # = 26 (number of letters!)
    # for row in b:
    #     print(row)
    # print(n,m)
    # print()

    gamma={} # define dictionaries for gamma and phi
    phi={}



    # print(type(gamma), type(phi))

    ## You must complete the code below
    for k in range(2): # IF ERROR, CHANGE 'm' to '26'
        # Your code goes here (initialisation)
        # print('i: ' + str(i) + '    y[i]:' + str(y[i]) + '    pi[i]' + str(pi[i]))
        
        # Here t = 0: Hence we're looking at 'gamma' at t = 0 and 'y' at t =0 (i.e. y_0, first character of given word)
        #             We do this for all k states (k = 0 to 26)
        # b[k]][y[0]] is the emission probability of seeing the first observation given we're in state 'k' of which there are 26!
        gamma[k,0] = b[k][y[0]] * pi[k]

    # print(gamma)
    # letter by letter, from 2nd letter to final letter of word
    for t in range(1,n):
        for k in range(m):
            array = []
            gamma[k,t]=0
            for j in range(m):
                # Your code goes here
                # print(p[j][k], gamma[j,(t-1)])
                array.append(p[j][k] * gamma[j,(t-1)])
            gamma[k,t] = b[k][y[t]] * max(array)
            phi[k,t] = array.index(max(array))
    
    
    best=0
    x=[]
    for t in range(n):
        x.append(0)

    # Find the final state in the most likely sequence x(n).
    for k in range(m):
        if best<=gamma[k,n-1]:
            best=gamma[k,n-1]
            x[n-1]=k
    
    # Back track through states and find the remaining sequence from phi to find most likely state sequence
    for i in range(n-2,-1,-1):
        # Your code goes here
        best = 0
        for k in range(m):
            if best<=gamma[k,i]:
                best=gamma[k,i]
                x[i]=k
        print(i)

    print()
    return x

def main():
    # The text messages you have received.
    y=[1,3,2]
    b=constructEmissions()
    [p, prior]=constructTransitions()

    # print('b')
    # print(b)
    # print()
    # print('p')
    # print(p)
    # print()
    # print('prior')
    # print(prior)
    # print()

    x=HMM(p,prior,b,y) #perform the Viterbi algorithm
    print('x')
    print(x)
    print()

if __name__ == "__main__":
    # 1.
    # constructTransitions()

    # 2.
    # pr_correct= 0.5
    # adj=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,1],[0,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0],[0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0],[0,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,0,0],[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,0,0],[0,0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0],[0,1,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,1,0],[0,1,0,0,0,0,1,0,0,1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,0,1,0,1,1,0,0,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,0,1,1,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,1,0,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],[0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],[1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1],[0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],[0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0],[0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1],[0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0]]
    # constructEmissions()

    # 3.
    # HMM(p,pi,b,y)

    # 4.

    main()