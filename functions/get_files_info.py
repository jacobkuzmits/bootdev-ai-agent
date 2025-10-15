import os

def get_files_info(working_directory, directory="."):
	directory_label = 'current' if directory == "." else f"'{directory}'"
	result = f"Result for {directory_label} directory:\n"

	# prevent escaping the working_directory
	if directory.startswith("..") or directory.startswith("/"):
		return result + f'    Error: Cannot list "{directory}" as it is outside the permitted working directory\n'

	# validate the directory exists
	dir = os.path.join(working_directory, directory)
	if not os.path.isdir(dir):
		return result + f'    Error: "{directory}" is not a directory\n'

	contents = os.listdir(dir)
	# verify directory has contents
	if len(contents) == 0:
		return result + f'    Error: "{directory}" is empty\n'
	
	# display file data
	for c in contents:
		file_path = os.path.join(dir, c)
		is_dir = not os.path.isfile(file_path)
		size = os.path.getsize(file_path)
		result += f" - {c}: file_size={size} bytes, is_dir={is_dir}\n"
		
	return result
