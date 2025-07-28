# Rock Paper Scissors with Machine Learning 

This is a python based game of Rock Paper Scissors that will learn and adapt to the player's decision using machine learning.

# Tools
  - Python 3
  - Scikit-learn
  - Docker and Dev Containers
  - Git and Github

# Features
- Classic Rock Paper Scissors gameplay
- Machine Learning (Naive Bayes) to predict the player's next decision
- Learns from player history
- Smart AI selects the counter move
- Clean separation of branches and versions
  - 'main' : basic Rock Paper Scissors game
  - 'ml-pattern-tracking' : enhanced ML version

# How the AI works
- Tracks your move history
- Trains a Naive Bayes model using 'scikit-learn'
- Predicts what your next choice will be based on your previous choices
- Chooses an option that will beat your choice based on the information

# Development process
- Started as a basic CLI game
- Added Machine Learning logic in a new git branch
- The code was tested, checked and merged through a pull request
- Version control is used to preserve the original game

# How to run
- Option 1: Using Dev Container
  - Open the project in Visual Studio Code
  - The 'Dev Containers extension' needs to be installed
  - When prompted, reopen the folder in the container
  - Run the game:  python3 rps_ml_game.py

- Option 2: Run locally
  - pip install scikit-learn
  - python3 rps_ml_game.py

# Files
- rps_ml_gameplay.py - main game script
- README.md - project description and how to use
- .devcontainer/ - container setup to package dependencies for a consistent environment 
- requirements.txt - python dependencies
