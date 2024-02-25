# version 1
# from game_gui import GameGUI
# from game import Game

# if __name__ == '__main__':
#     n = int(input('Enter the size of the board: '))
#     c = int(input('Enter the number of cops: '))
#     game = Game(n, c)
#     game.run_game()

#     #gui = GameGUI()
#     #gui.run()

# version 2
import os
import random
from graph import Graph
import node
import pickle

BOARD_SIZE = 4
file_name = "graph_new.pkl"

# Check if the graph file exists
if os.path.exists(file_name):
    # Load the graph from the file
    with open(file_name, "rb") as f:
        my_graph = pickle.load(f)
else:
    # Create the graph using the create_graph function from graph.py
    my_graph = Graph()
    my_graph.create_graph(BOARD_SIZE)

    # Save the graph to a file
    with open(file_name, "wb") as f:
        pickle.dump(my_graph, f)

# press enter to continue
print("Graph created!")
input("Press enter to continue...")

# Create an initial node with random positions for the robber and the policemen
robber = (random.randint(0, BOARD_SIZE - 1), random.randint(0, BOARD_SIZE - 1))
police1 = (random.randint(0, BOARD_SIZE - 1), random.randint(0, BOARD_SIZE - 1))
while police1 == robber:
    police1 = (random.randint(0, BOARD_SIZE - 1), random.randint(0, BOARD_SIZE - 1))
police2 = (random.randint(0, BOARD_SIZE - 1), random.randint(0, BOARD_SIZE - 1))
while police2 == robber or police2 == police1:
    police2 = (random.randint(0, BOARD_SIZE - 1), random.randint(0, BOARD_SIZE - 1))
initial_node = node.Node(robber, police1, police2, 0)

# test states:
robber = (0, 0)
police1 = (0, 3)
police2 = (3, 3)
initial_node = node.Node(robber, police1, police2, 0)
current_node = initial_node

# Print the initial node
print(f"Robber: {current_node.robber}")
print(f"Police1: {current_node.police1}")
print(f"Police2: {current_node.police2}")

# Print node's neighbors
print("Neighbors of the initial node:")
for neighbor in my_graph.get_neighbors(current_node):
    print(neighbor)


game_over = False
my_graph.print_grid(current_node, BOARD_SIZE)
# Run the game until the robber is caught or escapes
while not game_over:
    # Call the reverse_bfs function to find the path from the current node to a goal node
    #
    # my_graph.print_grid(current_node, BOARD_SIZE)

    path = my_graph.reverse_bfs(current_node)
    print(path)
    # Check if there is a solution
    if path == "No solution":
        print("The robber escaped! (no path)")
        game_over = True
    else:
        # Print the length of the path as the number of moves the robber has left. count only the robber moves
        #print(f"The robber has {len(path) - 1} moves left.")

        # ask the user to enter the next move
        direction = input("Enter the next move (w, a, s, d): ")

        if direction not in ['w', 'a', 's', 'd']:
            print("Invalid input!")
            continue
        
        # Calculate the new position of the robber
        if direction == 'w':
            new_robber = (current_node.robber[0] - 1, current_node.robber[1])  
        elif direction == 'a':
            new_robber = (current_node.robber[0], current_node.robber[1] - 1)
        elif direction == 's':
            new_robber = (current_node.robber[0] + 1, current_node.robber[1])
        else:
            new_robber = (current_node.robber[0], current_node.robber[1] + 1)


        # Check if the new position of the robber is valid
        if new_robber[0] < 0 or new_robber[0] >= BOARD_SIZE or new_robber[1] < 0 or new_robber[1] >= BOARD_SIZE:
            print("Invalid move! (out of bounds)")
            continue

        # Create a new node with the new position of the robber and the same positions of the policemen
        new_node = node.Node(new_robber, current_node.police1, current_node.police2, 1)

        # Check if the new node is a neighbor of the current node
        # if not my_graph.are_neighbors(current_node, new_node):
        #     print("Invalid move! (not a neighbor)")
        #     continue

        # Set the current node to be the new node
        current_node = new_node

        print(f"Robber moved to {current_node.robber}")

        # Check if the robber is caught
        if my_graph.is_goal(current_node):
            print("The robber is caught! (robber moved)")
            game_over = True
        else:
            # Call the best_move function to find the best move for the policemen
            first_move = my_graph.best_move(current_node)

            # Check if there is a move
            # check if first_move is a string
            if isinstance(first_move, str):
                print("The robber escaped! (no cop move)")
                game_over = True
            else:
                # Set the current node as the first move
                current_node = first_move

                print(f"Police1 moved to {current_node.police1}")
                print(f"Police2 moved to {current_node.police2}")

                # Check if the robber is caught
                if my_graph.is_goal(current_node):
                    print("The robber is caught! (cop moved)")
                    game_over = True


    print("is equal y", current_node.robber[0] == new_robber[0])
    print("is equal x", current_node.robber[1] == new_robber[1])
    print("turn", current_node.turn)
    my_graph.print_grid(current_node, BOARD_SIZE)