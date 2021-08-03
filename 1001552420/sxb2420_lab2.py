#
# Name: Sugam Banskota
# ID: 1001552420
#
import time
# from datetime import datetime

prev_router_cost = [] # cost of previously updated routers
neighbor_distance = [] # neighbor distance value
router_cost = [] # cost of the routers

def distance_vector_routing():
    filename = input("enter the text filename: ") # open file
    document = open(filename)
    # document = open('data.txt') (hardcoded, maybe I can change that later on)

    hanga = [] # branches
    jodne = [] # joints

    for tukra in document:
        # removing new line from the document
        tukra = tukra.replace('\n', '')
        # appending the replaced newline
        jodne.append(tukra)

        # Values obtained for link, route, and cost is tokenized
        connect = tukra.split(' ')

        # if the branch doesnot contain the router, we need to add that
        if not hanga.__contains__(int(connect[0])):
            hanga.append(int(connect[0]))

        # similar as the first step for the second part
        if not hanga.__contains__(int(connect[1])):
            hanga.append(int(connect[1]))
            
    hanga=sorted(hanga)
    # number of nodes in the graph
    nodes_num = len(hanga)

    # calculating the router, previous router, and neighbor distance based on the number of nodes
    global router_cost, prev_router_cost, neighbor_distance
    # calculating the previously updated router cost
    prev_router_cost = [[0 for i in range(nodes_num)] for j in range(nodes_num)]
    # calculating the values for the distance of neighbor
    neighbor_distance = [[0 for i in range(nodes_num)] for j in range(nodes_num)]

    # calculating the router cost
    router_cost = [[0 for i in range(nodes_num)] for j in range(nodes_num)]
    # router cost needs to be updated based on different condition
    for i in range(0, nodes_num):
        for j in range(0,nodes_num):
            if i == j:
                router_cost[i][j] = 0  # router cost is 0 if it is going to itself
            else:
                router_cost[i][j] = 16  # 16 is considerd infinity in this assignment

    #router costs are updated here
    for i in range(0, len(jodne)):
        tukra = jodne[i]
        connect = tukra.split(" ")
        bablu = hanga.index(int(connect[0]))
        guddu = hanga.index(int(connect[1]))
        router_cost[bablu][guddu] = int(connect[2])
        router_cost[guddu][bablu] = int(connect[2])


    # asking the user to choose which simulation they want
    print()
    print("Please enter 1 or 2 for the following options:")
    print("1. Simulation with step-by-step tables")
    print("2. Simulation with no intervention")
    print()
    choice = int(input())

    # setting up the boolean for the user choice
    intervention = False # default is false so no intervention


    if choice==1:
        intervention = True # boolean set to true for intervention
    elif choice==2:
        intervention = False # boolean set to false(default) for no intervention
    else:
        print("Invalid Choice. Program terminated. \n") # choice must be 1 or 2
        exit(0)

    # functions for their particular tasks
    table_formation(nodes_num) # formation of the table
    # vector calculation based on the nodes, branch, and choice
    vect_calculate(nodes_num, hanga, intervention)

    print("Distance Vector Table \n")

    table_display(nodes_num, hanga) # display the table in the command line

    # User can adjust the cost of any link in the network
    while True:
        print()
        Beena2 = input("Press any key to continue or Type exit to exit: ")
        if Beena2 == 'exit':
            print("\nProgram terminated\n")
            exit(0)
        # print("STABLE CONDITION ACHIEVED !!!!!")
        print()
        # user enters the node number that they want to change the link cost of
        node_num_change = int(input("Enter the node number: "))
        # user enters the destination node
        destination_change = int(input("Enter the destination: "))
        # user enters the new cost. 16 is mentioned as infinity in the pdf
        new_link_cost = int(input("Enter the new cost ['16' = Infinity/Failure] :"))

        # if cost is infinite, the loop breaks
        if new_link_cost == 16:
            print("Failure due to infinity value")
            break

        # if the link cost is not infinite, new updates occur
        # based on the new values, the tables are updated and calculations are performed
        else:
            # getting the index of the node that needs to be updated
            Akhandanand = hanga.index(node_num_change)
            # getting the index of the destination that needs to be updated
            Satyanand = hanga.index(destination_change)
            # link is updated in bi-directional format
            router_cost[Akhandanand][Satyanand] = new_link_cost # updating the cost in one way
            router_cost[Satyanand][Akhandanand] = new_link_cost # updating the cost in another way

            # formation of the table
            table_formation(nodes_num)
            # vector calculation based on the nodes, branch, and choice
            vect_calculate(nodes_num, hanga, intervention)
            # display the table in the command line
            table_display(nodes_num, hanga)

            print("\nAdjust nodes and cost again ?")
            Beena = input("Press any key to continue or Type exit to exit: ")
            if Beena == 'exit':
                print("\nProgram terminated\n")
                exit(0)


# function for the table display based on the nodes and the branches
def table_display(nodes_num, hanga):
    print('\t')
    for choice in range(len(hanga)):
        print(hanga[choice], "\t\t", end=" ")

    print('')
    for choice in range(0, nodes_num):
        print(hanga[choice], '\t\t', end=" ")
        for guddu in range(0, nodes_num):
            print("Distance : ", prev_router_cost[choice][guddu], "   ", end=" ")
        print('')

# function for the table fomation based on the nodes and the branches
def table_formation(nodes_num):
    for i in range(0, nodes_num):
        for j in range(0, nodes_num):
            if i == j:
                prev_router_cost[i][j] = 0  # router cost is 0 if it is going to itself
                neighbor_distance[i][j] = i
            else:
                prev_router_cost[i][j] = 16 # 16 is considerd infinity in this assignment
                neighbor_distance[i][j] = 100 # setting a random value for neighbour distance




def vect_calculate(nodes_num, hanga, intervention):
    # initializing the clock timer

    # samaya = 0

    # timer starts only in No intervention method
    if intervention is not True:
        begin= time.time()
        # init_time = datetime.now()
        # samaya = int(round(time.time() *1000))

    node_num_change = 0 # at first the changed node is set to 0
    Gajgamini = 0 # initializing the iteration cycle
    stable_checker = 0 # initializing the counter for stable condition
    table_display(nodes_num, hanga) # function for the table display based on the nodes and the branches

    # this loop is for table as well as the stable condition
    for i in range(0,(4*nodes_num)):
        Phoolchand = dv_table(nodes_num, node_num_change)
        if Phoolchand:
            stable_checker+=1 # updating the counter for stable condtion
            if stable_checker==2: # value of 2 means that the table is in stable condition
                print()
                print("STABLE CONDITION ACHIEVED !!!!!\n")
                break

        print("\nUpdating the table ") #new table iteration is being calculated
        table_display(nodes_num, hanga)
        Gajgamini += 1 # iteration is updated
        node_num_change += 1

        if node_num_change == nodes_num:
            node_num_change = 0
        if intervention:
            input("\nPress Enter button to go to next iteration ")
            print()

        if intervention is not True:
            end=time.time()
            # fin_time = datetime.now()
            # khattam = int(round(time.time() * 1000))
            # biteko = (fin_time-init_time)
            elapsed = end-begin
            print("Total time spent is ", elapsed, " seconds.\n")

        print("Number of iteration = ", Gajgamini) #


# stable state must be checked and updated with the iteration
def dv_table(nodes_num, node_num_change):
    # setting the boolean to true as default
    Phoolchand = True
    for i in range(0, nodes_num):
        # cost calculation is done if the cost is not infinity
        if router_cost[node_num_change][i] != 16:
            new_link_cost = router_cost[node_num_change][i]
            for k in range(0, nodes_num):
                tripathi = prev_router_cost[i][k]
                if neighbor_distance[i][k] == node_num_change:
                    tripathi = 16 # cost is set to infinite
                if (new_link_cost + tripathi) < prev_router_cost[node_num_change][k]:
                    prev_router_cost[node_num_change][k] = new_link_cost + tripathi
                    neighbor_distance[node_num_change][k] = i
                    # Unstable state so boolean is updated
                    Phoolchand = False

    return Phoolchand


# Main Function
if __name__ == '__main__':
    distance_vector_routing()

# Book: James F Kurose Keith W Ross
# https://stackoverflow.com/questions/6415728/junit-testing-with-simulated-user-input
# https://www.geeksforgeeks.org/distance-vector-routing-dvr-protocol/
# https://www.geeksforgeeks.org/bellman-ford-algorithm-dp-23/
# https://stackoverflow.com/questions/37083381/accessing-nested-for-loop-indexes
# https://www.codespeedy.com/calculate-the-execution-time-of-a-small-python-program/
# https://www.geeksforgeeks.org/python-measure-time-taken-by-program-to-execute/
# https://www.guru99.com/reading-and-writing-files-in-python.html
