import os

path = "notebooks/research.ipynb"

print(os.path.split(path)) # it shows we have two objects one folder and the other file

# we can use the directory as dir and create a file within the directory

dir,file=os.path.split(path)

os.makedirs(dir,exist_ok=True)

with open (path,"w") as f:
    pass
    