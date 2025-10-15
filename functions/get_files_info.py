import os
from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

def get_files_info(working_directory, directory="."):
	directory_label = 'current' if directory == "." else f"'{directory}'"
	result = f"Result for {directory_label} directory:\n"

	target_relative_path = os.path.join(working_directory, directory)
	target_absolute_path = os.path.abspath(target_relative_path)
	current_absolute_path = os.path.abspath(working_directory)

	# prevent escaping the working_directory
	if not target_absolute_path.startswith(current_absolute_path):
		return result + f'    Error: Cannot list "{directory}" as it is outside the permitted working directory\n'

	# validate the directory exists
	if not os.path.isdir(target_relative_path):
		return result + f'    Error: "{directory}" is not a directory\n'

	contents = os.listdir(target_relative_path)
	# verify directory has contents
	if len(contents) == 0:
		return result + f'    Error: "{directory}" is empty\n'
	
	# display file data
	for c in contents:
		file_path = os.path.join(target_relative_path, c)
		is_dir = not os.path.isfile(file_path)
		size = os.path.getsize(file_path)
		result += f" - {c}: file_size={size} bytes, is_dir={is_dir}\n"
		
	return result
