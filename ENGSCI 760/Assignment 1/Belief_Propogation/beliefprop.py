import numpy as np

def main():
######################## USER INPUT STARTS HERE ###########################

    # Specify the names of the nodes in the Bayesian network
    # N: Can be characters OR strings
    nodes=['G','O','S','T']

    # Defining arcs which join pairs of nodes (nodes are indexed 1...N)
    # N: Arcs defined as a list (B)
    B=[]

    # This example is for arcs in our three-node network
    B.append(['A','B']) # N: Arc from node 1 to 2
    B.append(['B','C']) # N: Arc from node 2 to 3
    
    # Set up information struction (dictionary)
    info={}

    # Set up conditional distribution structure (dictionary)
    M={};

    # Specify any given information for each event (a vector of 1s means there is no information given for that event.
    # If information is given for an event, place a 0 corresponding to any outcome that is impossible.
    # N: info dictionary is a bunch of arrays
    # N: [1,1] means no information (that node is not an evidence node)
    # N: [1,0] or [0,1] means we HAVE information (this is an evidence node)
    info['A']=np.array([0,1])
    info['B']=np.array([1,1])
    info['C']=np.array([1,0])
    info['C']=np.array([1,0])

    # Specify prior and conditional distributions
    M['A']=np.array([0.2,0.8]) # N: Prior distribution
    M['B']=np.array([[0.8,0.2],[0.3,0.7]]) # N: Specified conditionals in terms of ROWS of matrices
    M['C']=np.array([[0.6,0.4],[0.2,0.8]])

    #Specify the root node and a list of leaf nodes
    root_node='A' # N: might be string
    leaf_nodes=['C'] # N: List of leaf nodes: Node 3 is the ONLY leaf node in this network

######################### USER INPUT ENDS HERE ############################

    # Set up structures to store parent and child information for each node
    parent={}
    children={}
    count={}
    # Define A to be the number of arcs in the Bayesian network
    #A=len(B)

    # Go through arcs, and define parents and children
    for i in range(len(B)):
        if B[i][1] not in parent:
            parent[B[i][1]]=B[i][0]
        else:
            print("Multiple parent nodes dectected for node " + str(B[i][1]))

        if B[i][0] not in children:
            children[B[i][0]]=[]
            count[B[i][0]]=0

        count[B[i][0]]+=1
        children[B[i][0]].append(B[i][1])


    # Set up structures for belief propagation algorithm
    lambda_={}
    lambda_sent={}
    pi={}
    BEL={}
    pi_received={}

    # First pass, from the leaf nodes to the root node
    Q=leaf_nodes
    while len(Q)!=0:
        i=Q.pop(0)

        lambda_[i]=info[i];
        if i in children:
            for j in children[i]:
                lambda_[i]=lambda_[i]*lambda_sent[j]

        if i in parent: # if the node is not the root node, send information to its parent node
            lambda_sent[i]=M[i].dot(lambda_[i])
            count[parent[i]]-=1
            if count[parent[i]]==0:
                Q.append(parent[i])

    # Second pass, from the root node to the leaf nodes
    Q=[root_node]
    while len(Q)!=0:
        i=Q.pop(0)
        if i not in parent: # if the node is the root node, pi is set to be the prior distribution at the node
            pi[i]=M[i].T;
        else: # otherwise, pi is the matrix product of the message from the parent and the conditional probability at the node
            pi[i]=M[i].T.dot(pi_received[i]);
    
        # compute a normalised belief vector
        BEL[i]=pi[i]*lambda_[i]
        BEL[i]=BEL[i]/sum(BEL[i])
        
        # send adjusted and normalised messages to each child
        if i in children:
            for j in children[i]:
                pi_received[j]=BEL[i]/lambda_sent[j] 
                pi_received[j]=pi_received[j]/sum(pi_received[j]);
                Q.append(j)

    # Display the updated distributions, given the information.
    for i in nodes:
        print(str(i) +": "+str(BEL[i]))



if __name__ == "__main__":
    main()
