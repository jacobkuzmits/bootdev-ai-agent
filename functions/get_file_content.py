import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):

	target_relative_path = os.path.join(working_directory, file_path)
	target_absolute_path = os.path.abspath(target_relative_path)
	current_absolute_path = os.path.abspath(working_directory)

	# prevent escaping the working_directory
	if not target_absolute_path.startswith(current_absolute_path):
		return f'    Error: Cannot read "{file_path}" as it is outside the permitted working directory\n'

	# validate the file exists
	if not os.path.isfile(target_relative_path):
		return f'    Error: File not found or is not a regular file: "{file_path}"'
	
	# get file contents
	with open(target_relative_path, "r") as f:
		file_content_string = f.read(MAX_CHARS)
		if len(file_content_string) == 10000:
			file_content_string += f'[...File "{file_path}" truncated at 10000 characters]'
		return file_content_string + "\n"
	