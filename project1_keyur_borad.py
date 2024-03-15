import copy
import numpy as np
closed_set=set()

#defining moves
def move_left(node,row,col):
    #Swapping element values
    node[row][col-1],node[row][col]=node[row][col],node[row][col-1]
    return node
def move_right(node,row,col):
    #Swapping element values
    node[row][col+1],node[row][col]=node[row][col],node[row][col+1]
    return node
def move_up(node,row,col):
    #Swapping element values
    node[row-1][col],node[row][col]=node[row][col],node[row-1][col]
    return node
def move_down(node,row,col):
    #Swapping element values
    node[row+1][col],node[row][col]=node[row][col],node[row+1][col]
    return node
#updating visited node as a nested dictionary
def visited_node(node):
    node_dict={node[0]:{node[1]:node[2]}}
    visited_nodes.update(node_dict)
#Checking if a node is already visited or not
def is_already_node(node):
    s=()
    for row in node:
    # for i in row:
        s=s+tuple(row)

    if {s}.issubset(closed_set):
        return True
    else:
        return False

    # for value in visited_nodes.values():
    #     for nest_value in value.values():
    #         # print("value: ", nest_value)
    #         # print("Node: ", node)

    #         if nest_value==node:
    #             # print("Node is present")
    #             return True
    # return False

#implementing Breadth first search algo which returns bactracked path
def BFS(goal,input,Node_index_i=1,Parent_Node_index_i=0):
    #inintialising first Unvisisted node ,i.e. Input node
    unvisited_node=[[Node_index_i,Parent_Node_index_i,input]]
    Flag=True
    # for nodes in unvisited_node:
    while Flag:
        while unvisited_node:
            #popping unvisited node value on the basis of FIFO
            nodes=unvisited_node.pop(0)
            #incrementing parent node index 
            Parent_Node_index_i+=1
            #Finding zero in a given node
            Zero=[(x,y) for x, row in enumerate(nodes[2]) for y,i in enumerate(row) if i==0]
            zero_row=Zero[0][0]
            zero_col=Zero[0][1]
            #Adding the current node into visited node list
            visited_node(nodes)
            s=()
            for row in nodes[2]:
            # for i in row:
                s=s+tuple(row)
            closed_set.add(s)
            
            #Now Node can move in different directions based on the location of zero in the node
            #checking if there is sufficient column available to move left
            if zero_col>0: 
                node_1 = move_left(copy.deepcopy(nodes[2]),zero_row,zero_col)
                #Checking if this node is already present in the visited node list
                if is_already_node(node_1)==False:
                    #if not then incrementing the index number and appending it to the node list
                    Node_index_i+=1
                    node_list.append([Node_index_i,Parent_Node_index_i,node_1])
                #Cecking if the given node is goal node
                if node_1==goal:
                    #if yes then add this explored node into cisited and print found node
                    visited_node([Node_index_i,Parent_Node_index_i,node_1])
                    print("Found node")
                    # Assign FLag as false to exit the outer while loop
                    Flag=False
                    #Exit the inner while loop
                    break
                
            #checking if there is sufficient column available to move right
            if zero_col<2: 
                node_1 = move_right(copy.deepcopy(nodes[2]),zero_row,zero_col)
                #Checking if this node is already present in the visited node list
                if is_already_node(node_1)==False:
                    #if not then incrementing the index number and appending it to the node list
                    Node_index_i+=1
                    node_list.append([Node_index_i,Parent_Node_index_i,node_1])
                #Cecking if the given node is goal node
                if node_1==goal:
                    #if yes then add this explored node into cisited and print found node
                    visited_node([Node_index_i,Parent_Node_index_i,node_1])
                    # Assign FLag as false to exit the outer while loop
                    print("Found node")
                    Flag=False
                    #Exit the inner while loop
                    break
            #checking if there is sufficient column available to move right
            if zero_row>0: 
                node_1 = move_up(copy.deepcopy(nodes[2]),zero_row,zero_col)
                #Checking if this node is already present in the visited node list
                # print(node_1)
                if is_already_node(node_1)==False:
                    #if not then incrementing the index number and appending it to the node list
                    Node_index_i+=1
                    node_list.append([Node_index_i,Parent_Node_index_i,node_1])
                #Cecking if the given node is goal node
                if node_1==goal:
                    #if yes then add this explored node into cisited and print found node
                    visited_node([Node_index_i,Parent_Node_index_i,node_1])
                    print("Found node")
                    # Assign FLag as false to exit the outer while loop
                    Flag=False
                    #Exit the inner while loop
                    break
            #checking if there is sufficient column available to move right
            if zero_row<2: 
                node_1 = move_down(copy.deepcopy(nodes[2]),zero_row,zero_col)
                # print(node_1)
                #Checking if this node is already present in the visited node list
                if is_already_node(node_1)==False:
                    #if not then incrementing the index number and appending it to the node list
                    Node_index_i+=1
                    node_list.append([Node_index_i,Parent_Node_index_i,node_1])
                #Cecking if the given node is goal node
                if node_1==goal:
                    #if yes then add this explored node into cisited and print found node
                    visited_node([Node_index_i,Parent_Node_index_i,node_1])
                    print("Found node")
                    # Assign FLag as false to exit the outer while loop
                    Flag=False
                    #Exit the inner while loop
                    break
        #copying node list into unvisited node to keep exploring the nodes        
        unvisited_node=copy.deepcopy(node_list)
        #clearing the node list to add new nodes
        node_list.clear()  
    #Calling function to backtrack the goal node to initial node once the above two while loops exits and passing all visited node
    generated_backtracking_seq= Backtracking_node(visited_nodes)
    #returns list of backtracked nodes
    return generated_backtracking_seq 

#Bactracking the path from goal node to initial node using all visited nodes
def Backtracking_node(v_node):
    bk_track_seq=[]
    #As last node is the starting point hence we will be using last node to reach to its parent recurcively
    last_node=v_node.popitem()
    # initializing parent node index from the 
    parent_node=list(last_node[1].keys())
    # appending the node of the given 
    bk_track_seq.append(list(last_node[1].values()))
    
    #Running recurvisely untill parent node is equal to zero
    while parent_node[0]!=0:
        gett=v_node.get(parent_node[0])
        parent_node=list(gett.keys())
        bk_track_seq.append(list(gett.values()))

    return bk_track_seq

# Creating nodePath.txt file
def create_nodePath_txt(solution_nodes):
    #reversing the list which is initially from Goal to intial node  
    solution_nodes.reverse()
    #conveting the lists to Numpy array
    cvt_2_nparray=np.array(solution_nodes)
    #Removing additional dimention of the list by np.squeeze(Originally generated because of Appending)
    cvt_2_nparray=np.squeeze(cvt_2_nparray)
    #Creating new array of node which is transpose of original node 
    transpose_seq=cvt_2_nparray
    for k in range(len(cvt_2_nparray)):
        transpose_seq[k]=cvt_2_nparray[k].T
    # Opening and Closing a file "MyFile.txt"
    # for object name file1.
    file1 = open("nodePath.txt","w")
    #for each node in the transpose seq
    for each_node in transpose_seq:
        for i in range(3):
            for j in range(3):
                #Writing elements of the nodes with space
                file1.write(str(each_node[i][j]))
                file1.write(" ")
        file1.write("\n")        

    file1.close()

# Creating NodeInfo.txt file
def create_NodeInfo_txt(visited_nodes):
    file1 = open("NodeInfo.txt","w")
    L=[" Node_Index"," ","Parent_Node_Index", " ", "Node \n"]
    file1.writelines(L)
    for i in list(visited_nodes.keys()):
        val =visited_nodes.get(i)
        file1.write(str(i))
        file1.write("          ")
        file1.write(str(list(val.keys())[0]))
        file1.write("                ")
        j=list(val.values())
        for m in range(3):
            for n in range(3):
                file1.write(str(j[0][n][m]))
                file1.write(" ")
        file1.write("\n")
    file1.close()

# Creating Nodes.txt file
def create_Nodes_txt(visited_nodes):
    file1 = open("Nodes.txt","w")
    for i in list(visited_nodes.keys()):
        val =visited_nodes.get(i)
        j=list(val.values())
        for m in range(3):
            for n in range(3):
                file1.write(str(j[0][n][m]))
                file1.write(" ")
        file1.write("\n")
    file1.close()


if __name__=="__main__":
    # Input Node : User to put initial node here
    # input = ([[1,2,0],[4,5,3],[7,8,6]])
    input = ([[6,4,7],[8,5,0],[3,2,1]])
    # Goal node: User can define the definite goal node that need to be achieve here.
    goal=[[1,2,3],[4,5,6],[7,8,0]]
    #decalring variables
    unvisited_node=[]#nodes that are yet to be explored
    visited_nodes={}#Visited nodes that are checked if it matches with the goal node
    node_list=[] #list of nodes
    Node_index_i=1 #index of new node
    Parent_Node_index_i=0 #Parent node index
    '''
    Method: BFS-> 
    arg:goal node, input node, (optional)Node_index_i, (optional)Parent_Node_index_i
    return: Backtracked list of nodes from goal to initial node
    '''
    solution_nodes=BFS(goal,input) # Function that takes
    create_nodePath_txt(solution_nodes)# method to generate txt file
    create_NodeInfo_txt(visited_nodes)# method to generate txt file
    create_Nodes_txt(visited_nodes)# method to generate txt file
    print("Generated all text files")
