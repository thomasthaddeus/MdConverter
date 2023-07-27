#!/bin/bash

# Ask for the repository name
echo "Enter the name of the repository:"
read repo_name

# Create a directory for the repository
mkdir $repo_name
cd $repo_name

# Initialize a new Git repository
git init

# Create directories for a typical Python project
mkdir src
mkdir tests
mkdir docs

# Create a .gitignore file for Python
echo "*.pyc" > .gitignore
echo "__pycache__/" >> .gitignore

# Create an initial README.md file
echo "# $repo_name" > README.md

# Create an initial Python script and test script
touch src/main.py
touch tests/test_main.py

# Stage and commit the initial project structure
git add .
git commit -m "Initial commit"

# Rename the default branch to main
git branch -M main

# Create a new GitHub repository and push the initial project structure to it
# This requires the GitHub CLI tool `gh`. If you don't have it, you can comment out these lines.
gh repo create $repo_name --public --confirm
git push -u origin main
