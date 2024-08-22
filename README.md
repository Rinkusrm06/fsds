# This is my end to end project

# first initialize the git
git init

# to add a file to staging
git add abc.txt

# to add all files to staging
git add .

# to commit

git commint -m "<Message>"

# create a .gitignore file on Github and you can choose the python template. This will not push unnecessary changes.

# create a LICENSE file. It is not mandatory but is useful in case you are building a product for commercial or open source use.There are different types of licenses you can check the terms of usage and limitations and decide on the type of license.

# create init_setup file to install all the requirements regarding the setup. Its a shell script to run all the basic setup commnads at one go.To execute the file use bash init_setup.sh.

# Data ingestion
# EDA
# FE
# model building
# evaluation
# logger - to log the different steps in run time
# exception - to record the exception
# util - To store some of the files or code which is not part of the actual code but is useful
# setup.py - to run the code
# Requirements.txt - to store the requirements of the project

# CI/CD, which stands for continuous integration and continuous delivery/deployment, aims to streamline and accelerate the software

# Project structure  

# 1. .github >> workflows >> yaml files (Will .gitkeep files initially)
# 2. Notebooks >> research.ipynb
# 3. src >> DiamondPricePrediction >> src >> component >> 1. Data ingestion.py 2. Preprocessing.py 3. Model training.py
#                                  >> pipeline >> 1. training.py 2. prediction.py
#                                  >> exceptions.py
#                                  >> logger.py
#                                  >> exceptions.py
#                                  >> utils.py
# 4. Requirements.txt
# 5. Setup.py


# A . gitkeep file tells github to do the opposite of its default behaviour, which is to ignore empty folders. If you want to track an empty folder, or a folder with untracked files, create a 0kb file with the . gitkeep file extension in that folder.
