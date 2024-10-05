3D_Game_of_Life

Introduction

This project implements the simulation and visualization of a three-dimensional Game of Life. The Game of Life was originally proposed by British mathematician John Conway in 1970. It is a zero-player cellular automaton that simulates the complex process of life evolution through simple survival and reproduction rules. Compared to the traditional two-dimensional Game of Life, the three-dimensional version can display richer and more complex dynamic behaviors, providing a more intuitive and in-depth exploration of life patterns.

Main Features:

High Performance: Efficient numerical computation using NumPy and Numba to accelerate the simulation process.
Diverse Initial Configurations: Supports various initial configurations of live cells, including random distribution, spherical, spiral, multiple cubes, and honeycomb structures.
Interactive Visualization: Generates interactive 3D animations using Plotly, making it easy to observe the dynamics of life evolution.
Flexible Parameter Adjustment: Users can adjust grid size, initial number of live cells, number of generations, and survival and birth rules as needed.
Software Architecture

This project adopts a modular design, mainly divided into the following parts:

Initial Configuration Generation Module

Function: Generates initial configurations of live cells in different shapes and distributions, including random distribution, spherical, spiral, multiple cubes, and honeycomb structures.
Implementation: Achieved through a series of functions (e.g., generate_random_active_cells, generate_spherical_active_cells, etc.) to generate diverse initial configurations.
Simulation Evolution Module

Function: Evolves cell states according to the rules of the Game of Life, generating the grid state for each generation.
Implementation: Uses Numba’s @njit decorator and parallelization techniques (prange) to accelerate key computation parts, including neighbor counting and state updating.
Visualization Module

Function: Generates 3D animations from the simulation history and provides an interactive visualization interface.
Implementation: Uses Plotly’s Scatter3d object to create 3D scatter plots and frame animations to display the life evolution process. Supports saving as an HTML file and automatically opening it in a browser.
Main Control Module

Function: Coordinates the workflow of each module, including initializing the grid, running the simulation, and generating visualization results.
Implementation: The overall process control is implemented through the main() function, where users can set parameters and start the simulation.
Installation Guide

Clone the Repository First, clone this project to your local machine:
git clone https://gitee.com/your_username/3D_Game_of_Life.git
cd 3D_Game_of_Life

Create a Virtual Environment (Optional) It is recommended to install dependencies in a virtual environment to avoid conflicts with other projects:
python -m venv venv
source venv/bin/activate  # For Windows users, use `venv\Scripts\activate`

Install Dependencies Run the following command in the project directory to install the required Python libraries:
pip install numpy numba plotly

Dependencies:
NumPy: For efficient numerical computation and array operations.
Numba: Accelerates key computation parts through JIT compilation, improving simulation performance.
Plotly: For generating interactive 3D visualizations.
Usage Instructions

Configure Initial Parameters Open the 3D_Game_of_Life.py file, find the main() function, and adjust the following parameters as needed:
Grid Size:
Python

size = (100, 100, 100)  # Double the length, width, and height, increasing the volume eightfold
Initial Number of Live Cells:
Python

num_random_cells = 25340  # Set the initial number of random live cells to 25,340
Number of Generations:
Python

generations = 100  # Adjust as needed
Run the Simulation Navigate to the script directory in the terminal or command prompt and run:
python 3D_Game_of_Life.py

Process:
Initialization: The script will generate the specified number of unique live cells and initialize the 3D grid.
Simulation Evolution: Evolves cell states generation by generation according to the set number of generations, printing the number of live cells in each generation.
Generate Visualization: After the simulation is complete, the script will generate an HTML file and automatically open it in the default browser, displaying the 3D Game of Life animation.
Example Output:
Initial number of live cells: 25340
Generation 1 completed. Live cells: 25000
Generation 2 completed. Live cells: 24500
...
Generation 100 completed. Live cells: 8000
Visualization saved to 3D_Game_of_Life_25340.html
Simulation complete. Press Enter to exit the program and close the script.

Interactive Visualization In the HTML file opened in the browser, you can:
Play Animation: Click the “Play” button to start the animation.
Pause Animation: Click the “Pause” button to stop the animation.
Rotate View: Drag the mouse to rotate the 3D view and observe the life evolution from different angles.
Contributing

We welcome contributions of code and ideas to this project! Here is the contribution guide:

Fork the Repository Click the “Fork” button on Gitee to clone this repository to your account.
Create a Feat_xxx Branch In your local repository, create a new feature branch based on the main branch:
git checkout -b feat_add_new_feature

Submit Code Make modifications, add new features or fix issues on the feature branch, and commit the changes:
git add .
git commit -m "Add new feature: description"

Push the Branch Push the feature branch to the remote repository:
git push origin feat_add_new_feature

Create a Pull Request Submit a Pull Request on Gitee, describing your changes and contributions. The project maintainers will review and merge your contributions. Special Tips:
Follow Code Standards: Ensure consistent code style and follow PEP 8 standards.
Write Clear Commit Messages: Each commit should have a clear description for easy review and traceability.
Provide Detailed Documentation: If adding new features, update the documentation and usage instructions accordingly.
