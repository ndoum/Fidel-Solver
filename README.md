# Fidel-Solver

Fidel Dungeon Rescue is a puzzle game where you are guiding a dog named Fidel along a simple path in a grid-like environment where in each cell there might be coins, special enemies, health packs, and more. The goal of the game is to make sure that Fidel can be led to the end cell of each level safely, ideally maximizing experience points earned, coins collected, etc. When Fidel walks along the grid an uncrossable leash is left behind, making stepping on a square again impossible and the game challenging, especially when you must also consider a limited health capacity, enemies that need to be attacked in a certain order/ direction, and possible extra experience points from defeating foes 3 in a row.

The goal of this project is to find the optimal path for Fidel to take in order to maximize experience for any layout of the environment.

We decided to solve each level by creating connections between states, where each state knows the layout of the level, experience points earned, health remaining etc. A connection exists between two states if Fidel can move one tile to reach the next state. We implemented it using a priority queue.

An undirected edge or connection exists between two nodes if in the environment you can reach square B from A. 
For example, if in the environment square B is above square A and these squares are not corner or edge squares, then there are connections from A-N, A-S, A-E, A-W to B-N, and connections from B-N, B-S, B-E, B-W to A-S.
Directioms are important to have because some enemies may be pointing in any direction but can only be killed when approached from behind.

Each square in the enviromnent may have an immovable object on it, an enemy, spikes, items, and more, so each tile knows what object is on it and any descriptors, how much experience points Fidel has earned !!TODO how many in a row killed

Depending on the enemy, Fidel may lose health when attacking. This is okay, as long as Fidel's health does not go in the negatives. This means that a simple Dijkstra's algorithm that maximizes XP ????will not????? always lead to the best path, since hurting yourself earlier on in the path may get you XP earlier on but might stop you from earning even more later on since Fidel does not have enough health to attack 
