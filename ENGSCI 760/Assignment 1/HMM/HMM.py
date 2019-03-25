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

    b = adj
    
    for i in range(26):
        
        rowSum = sum(b[i])

        for j in range(26):
            if (adj[i][j] == 1):
                b[i][j] = pr_correct/rowSum
        b[i][i] = pr_correct

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
    with open('test.txt', 'r') as myfile:
    # with open('test.txt', 'r') as myfile:
        text = myfile.read()
        
	## Your code goes here.
    # remove all whitespaces and other shit
    # text = text.replace(' ','')
    text = text.replace('  ','')
    text = text.replace('   ','')
    text = text.replace('\n','')
    text = text.replace('\r','')
    text = text.replace('(','')
    text = text.replace(')','')
    text = text.replace('!','')

    from collections import Counter

    res = Counter(text)
    # numLetters = sum(res.values())-res[" "] # not counting "space" characters
    numLetters = sum(res.values())
    prior = [] # SURELY THERE'S A BETTER WAY TO DO THIS...
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
    prior.append(res[" "]/numLetters)
    print(prior)

    def rank(c):
        return ord(c) - ord('a')

    # for c in text:
        # print(c)
    T = [rank(c) for c in text]
    # print(T)

    p = [[0]*26 for _ in range(26)]
    for  (i,j) in zip(T,T[1:]):
        # print(i,j)
        p[i][j] += 1

    # convert to probabilities
    for row in p:
        s = sum(row)
        if s > 0:
            row[:] = [f/sum(row) for f in row]

    for row in p:
        print(row)
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

    n=len(y)
    m=len(pi)

    gamma={}
    phi={}

    ## You must complete the code below
    for i in range(26):
        # Your code goes here (initialisation)
        i=1 # this is a bs line

    for t in range(1,n):
        for k in range(26):
            gamma[k,t]=0
            for j in range(26):
                # Your code goes here
                i=0 # BS line...
    
    
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
    for msg in msgs:
        s_in = msg.split(' ') #divide each message into a list of words

        output=''
        
        for i in range(len(s_in)):
            y=[]
            
            for j in range(len(s_in[i])):
                y.append(ord(s_in[i][j])-97) #convert the letters to numbers 0-25
            # end

            x=HMM(p,prior,b,y); #perform the Viterbi algorithm

            output=''
            for j in range(len(x)):
                output=output+chr(x[j]+97) #convert the states x back to letters
                    
            if i!=len(s_in)-1:
                output=output+' ' #recreate the message
                
        print(msg) #display received message
        print(output) #display decoded message
        print('')

if __name__ == "__main__":
    constructTransitions('test.txt')

    # pr_correct= 0.5
    # adj=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,1],[0,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0],[0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0],[0,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,0,0],[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,0,0],[0,0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0],[0,1,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,1,0],[0,1,0,0,0,0,1,0,0,1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,0,1,0,1,1,0,0,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,0,1,1,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,1,0,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],[0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],[1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1],[0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],[0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0],[0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1],[0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0]]
    # constructEmissions(pr_correct, adj)

    # for row in adj:
    #     print(row)

    # constructEmissions()
