This project contains a collection of Artificial Intelligence laboratory programs implemented using Python. These programs demonstrate fundamental AI concepts such as search algorithms, human verification systems, and intelligent behavior simulation.

The main objective of these programs is to understand how Artificial Intelligence techniques can be used for problem solving, decision making, and distinguishing between human and machine behavior.

---

### Turing Test Simulation

This program demonstrates a simple simulation of the Turing Test, originally proposed by Alan Turing. In this simulation, a judge communicates with both a human and a machine through a text interface. The identities of the participants are hidden, and the judge must decide which participant is the human based on the responses received.

Key Concepts

-> Intelligent behavior simulation
-> Human vs machine interaction
-> Decision evaluation

---

### CAPTCHA Authentication System

This program implements a simple CAPTCHA authentication mechanism. The system generates a random CAPTCHA consisting of letters and numbers, and the user must correctly enter the CAPTCHA to verify that they are a human user.

Key Concepts

-> Random string generation
-> Human verification techniques
-> Basic security implementation

---

### Breadth First Search (BFS)

This program implements the Breadth First Search algorithm to explore nodes level by level until the goal state is found.

Key Concepts

-> Graph searching
-> Queue data structure
-> Systematic node exploration

---

### Depth First Search (DFS)

This program demonstrates the Depth First Search algorithm, where the search explores one path deeply before backtracking to explore alternative paths.

Key Concepts

-> Graph traversal methods
-> Stack-based implementation
-> Backtracking strategy

---

### Depth Limited Search (DLS)

Depth Limited Search is a variation of DFS where the search depth is restricted to a specified limit to prevent infinite exploration in large or cyclic graphs.

Key Concepts

-> Controlled depth searching
-> Recursive algorithms
-> Graph exploration

---

### Iterative Deepening Depth First Search (IDDFS)

This algorithm combines the advantages of BFS and DFS. It repeatedly performs Depth Limited Search while gradually increasing the depth limit until the goal state is found.

Key Concepts

-> Iterative searching approach
-> Depth expansion strategy
-> Memory-efficient searching

---

### Tic Tac Toe Game (O and X)

This program implements the classic Tic-Tac-Toe game using the symbols O and X. Two players take turns placing their symbols on a 3×3 grid. The objective of the game is to form a straight line of three identical symbols either horizontally, vertically, or diagonally.
The program checks the board after every move to determine whether a player has won or if the game results in a draw.
Key Concepts
-> Game state representation
-> Turn-based decision making
-> Win condition checking and game logic### Air Quality Monitoring Agent: 

This program implements the classic Tic-Tac-Toe game using the symbols O and X. Two players take turns placing their symbols on a 3×3 grid. The objective of the game is to form a straight line of three identical symbols either horizontally, vertically, or diagonally.

The program checks the board after every move to determine whether a player has won or if the game results in a draw.
___
### Project Overview:

This project demonstrates a Rule-Based Simple Reflex Agent that evaluates the Air Quality Index (AQI) using environmental pollutant readings. The program reads pollutant concentrations from the user and determines the corresponding air quality condition.

In Artificial Intelligence, a Simple Reflex Agent makes decisions only based on the current percept (input) and applies predefined condition–action rules. It does not store previous states or perform learning.

In this project, pollutant values act as sensor inputs, and the agent immediately maps these inputs to an AQI classification using rule conditions.


### Pollutants Considered:

The system analyzes four major pollutants that influence air quality: PM2.5 – Fine particulate matter smaller than 2.5 micrometers PM10 – Particulate matter smaller than 10 micrometers NO₂ – Nitrogen dioxide gas from combustion sources CO – Carbon monoxide released from vehicles and burning fuels

These pollutants are combined to estimate the overall AQI value.

### Air Quality Classification:

0 – 50 Clean Air
51 – 100 Acceptable
101 – 150 Sensitive Groups Risk
151 – 200 Poor
Above 200 Very Dangerous

### Sample Execution:

---- Air Quality Monitoring System ----

Enter PM2.5 concentration: 70
Enter PM10 concentration: 110
Enter NO2 concentration: 55
Enter CO concentration: 1.2

Calculated AQI: 77.4 Air Condition: Acceptable

### Artificial Intelligence Concept Demonstrated:

This project illustrates the Simple Reflex Agent model.

Agent Components: Sensors: Collect pollutant levels (PM2.5, PM10, NO₂, CO) Rules: Condition-based AQI classification Actuator/Output: Displays AQI value and air quality category

The agent operates using the rule: IF AQI value falls in a specific range THEN assign corresponding air quality condition

Because the decision depends only on the current input, the system represents a Simple Reflex Agent in Artificial Intelligence.
