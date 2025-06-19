import os

# 1- Project Root
# Specify in which file you store the project files locally in the project_root variable below!
project_root = r"{your_project_folder}"

# 2- Image index auto-updates after app-1
img_index = 37

# 3- Path and name of excel file
final_file_name = f"1_dataset_{img_index}.xlsx"
final_file_path = os.path.join(project_root, final_file_name)

# 4- Df name
df_name = "2_dataset"