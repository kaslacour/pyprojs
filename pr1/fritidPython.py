import os

#elever i pr2
#pr2 =5

pr1 = ["Adam", "Andrea", "August",
      "Cornelius", "Ena", "Frederik", "Frida", "Ida", "Jonas G.", "Jonas S.",
      "Jonathan","Karoline","Kasper","Laurits","Michael","Milo","Nina","Oskar",
      "Rasmus","Sebastian", "Sophie", "Tobias", "Zara"]
 
#alias = "pr1_alias"

# if os.path.exists(alias):
#     real_path = os.path.realpath(alias)
#     for name in pr1:         
#         path = os.path.realpath(real_path+"/"+name)
#         
#         os.makedirs(path, exist_ok = True)
#         print(f"Directory '{dir_path}' created successfully.")
# 


dir_path = os.path.join(os.getcwd(), "temp")


for name in pr1:
    path = os.path.join(dir_path,name)
    os.makedirs(path, exist_ok=True)
