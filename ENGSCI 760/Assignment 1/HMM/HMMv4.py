def constructEmissions(pr_correct,adj):
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

	## Your code goes here.

    # for row in adj:
    #     print(row)    

    # Pre-define the emission probability matrix
    b = adj
    
    # Create loop for each row (loop through intended keystroke)
    for i in range(26):
        
        # Determine how many keys are adjacent to the i'th intended key
        rowSum = sum(b[i])

        # Assign probabilities of hitting adjacent keys without intending to
        for j in range(26):
            if (adj[i][j] == 1):
                b[i][j] = (1-pr_correct)/rowSum
        
        # Assign probability of 0.5 (pr_correct) that the intended key is hit
        b[i][i] = pr_correct

    # for row in b:
    #     print(row)
    return b

def constructTransitions(filename):
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

    ## Read the file into a sting called text
    with open(filename, 'r') as myfile:
    # with open('test.txt', 'r') as myfile:
        text = myfile.read()
        
	## Your code goes here.
    
    # Remove all whitespaces and other unwanted characters
    # text = text.replace(' ','')
    text = text.replace('  ','')
    text = text.replace('   ','')
    text = text.replace('\n','')
    text = text.replace('\r','')
    text = text.replace('(','')
    text = text.replace(')','')
    text = text.replace('!','')

    from collections import Counter
    
    # Initialise variable for frequency of each letter's appearance in corpus.
    res = Counter(text)

    # numLetters = sum(res.values())-res[" "] # not counting "space" characters
    
    # Total number of letters in the entire corpus
    numLetters = sum(res.values())
    
    # Initialise vector for priors
    prior = [] # SURELY THERE'S A BETTER WAY TO DO THIS...
    
    # Fill vector of priors: proportion of each letter in corpus
    prior.append(res["a"]/numLetters)
    prior.append(res["b"]/numLetters)
    prior.append(res["c"]/numLetters)
    prior.append(res["d"]/numLetters)
    prior.append(res["e"]/numLetters)
    prior.append(res["f"]/numLetters)
    prior.append(res["g"]/numLetters)
    prior.append(res["h"]/numLetters)
    prior.append(res["i"]/numLetters)
    prior.append(res["j"]/numLetters)
    prior.append(res["k"]/numLetters)
    prior.append(res["l"]/numLetters)
    prior.append(res["m"]/numLetters)
    prior.append(res["n"]/numLetters)
    prior.append(res["o"]/numLetters)
    prior.append(res["p"]/numLetters)
    prior.append(res["q"]/numLetters)
    prior.append(res["r"]/numLetters)
    prior.append(res["s"]/numLetters)
    prior.append(res["t"]/numLetters)
    prior.append(res["u"]/numLetters)
    prior.append(res["v"]/numLetters)
    prior.append(res["w"]/numLetters)
    prior.append(res["x"]/numLetters)
    prior.append(res["y"]/numLetters)
    prior.append(res["z"]/numLetters)
    # print(prior)
    # print(text)
    numUniques = len(set(text))
    # print(numUniques)

    # Define ranking function to convert letters into numbers to compare them
    def rank(c):
        charRank = ord(c) - ord('a')
        if charRank < 0:
            charRank = numUniques - 1 
        # print(charRank)
        return charRank

    # Vectorise corpus into numbers (rank) with rank('a') = 0, rank('b') = 1 and so on.
    T = [rank(c) for c in text]
    # print(T)
    # print()
    # print(numUniques)
    # print()

    # Frequency table for occurrence of each letter AFTER a given letter 
    # (e.g. in the corpus, how many times a 'b' appears after an 'a' and so on.)
    p = [[0]*(numUniques - 1) for _ in range(numUniques - 1)]
    for (i,j) in zip(T,T[1:]):
        # print(i,j)
        if (i<numUniques-1) & (j<numUniques-1):
            p[i][j] += 1
    
    # print()
    
    # for row in p:
    #     print(row)

    # print()
    # Convert frequencies to probabilities
    # (i.e. in the corpus, given we are on 'a', what is the probability of finding a 'b' next)
    for row in p:
        s = sum(row)
        # print(s)
        if s > 0:
            row[:] = [f/sum(row) for f in row]

    # for row in p:
    #     print(row)

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
    for k in range(26): # IF ERROR, CHANGE 'm' to '26'
        # Your code goes here (initialisation)
        # print('i: ' + str(i) + '    y[i]:' + str(y[i]) + '    pi[i]' + str(pi[i]))
        
        # Here t = 0: Hence we're looking at 'gamma' at t = 0 and 'y' at t =0 (i.e. y_0, first character of given word)
        #             We do this for all k states (k = 0 to 26)
        # b[k]][y[0]] is the emission probability of seeing the first observation given we're in state 'k' of which there are 26!
        gamma[k,0] = b[k][y[0]] * pi[k]

    # print(gamma)
    # letter by letter, from 2nd letter to final letter of word
    for t in range(1,n):
        for k in range(26):
            gamma[k,t]=0
            for j in range(26):
                # Your code goes here
                # print(p[j][k], gamma[j,(t-1)])
                array = p[j][k] * gamma[j,(t-1)]
            gamma[k,t] = b[k][y[t]] * max(array)
            phi[k,t] = array.index(min(array))
    
    
    best=0
    x=[]
    for t in range(n):
        x.append(0)

    # Find the final state in the most likely sequence x(n).
    for k in range(26):
        if best<=gamma[k,n-1]:
            best=gamma[k,n-1]
            x[n-1]=k

    for i in range(n-2,-1,-1):
        # Your code goes here
        i = 0 # BSSS!!!

    print()
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
    pr_correct= 0.5 # Complete this line

    # An adjacency matrix, adj(i,j) set to 1 if the i'th letter in the alphabet is next
    # to the j'th letter in the alphabet on the keyboard.
    adj=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,1],[0,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0],[0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0],[0,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,0,0],[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,0,0],[0,0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0],[0,1,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,1,0],[0,1,0,0,0,0,1,0,0,1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,0,1,0,1,1,0,0,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,0,1,1,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,1,0,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],[0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],[1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1],[0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],[0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0],[0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1],[0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0]]

    # Call a function to construct the emission probabilities of hitting a key
    # given you tried to hit a (potentially) different key.
    b=constructEmissions(pr_correct,adj)
    # Call a function to construct transmission probabilities and a prior distribution
    # from the King James Bible.
    [p, prior]=constructTransitions('bible.txt')
        
    # Run the Viterbi algorithm on each word of the messages to determine the
    # most likely sequence of characters.

    print()
    # for row in msgs:
    #     print(row)
    # print()


    # decoding one message (line) at a time
    for msg in msgs:
        s_in = msg.split(' ') #divide each message into a list of words
        output='' # initialise output string
        
        # decoding message, one word at a time (word by word)
        for i in range(len(s_in)):
            y=[]
            print("coded word: " + s_in[i])
            
            # convert letters to numbers, one letter at a time (letter by letter)
            for j in range(len(s_in[i])):
                y.append(ord(s_in[i][j])-97) #convert the letters to numbers 0-25
            # end

            print("coded number array, y: " + str(y))

            x=HMM(p,prior,b,y) #perform the Viterbi algorithm

            output=''
            for j in range(len(x)):
                output=output+chr(x[j]+97) #convert the states x back to letters
                    
            if i!=len(s_in)-1:
                output=output+' ' #recreate the message
        print("--")
                
        print(msg) #display received message
        print(output) #display decoded message
        print('')
        print("--")

if __name__ == "__main__":
    # 1.
    # constructTransitions('test.txt')

    # 2.
    # pr_correct= 0.5
    # adj=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,1],[0,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0],[0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0],[0,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,0,0],[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,0,0],[0,0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0],[0,1,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,1,0],[0,1,0,0,0,0,1,0,0,1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,0,1,0,1,1,0,0,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,0,1,1,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,1,0,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],[0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],[1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1],[0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],[0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0],[0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1],[0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0]]
    # constructEmissions(pr_correct, adj)

    # 3.
    # HMM(p,pi,b,y)

    # 4.

    main()