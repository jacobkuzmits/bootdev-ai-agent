import os

def write_file(working_directory, file_path, content):
	target_relative_path = os.path.join(working_directory, file_path)
	target_absolute_path = os.path.abspath(target_relative_path)
	current_absolute_path = os.path.abspath(working_directory)

	# prevent escaping the working_directory
	if not target_absolute_path.startswith(current_absolute_path):
		return f'    Error: Cannot write to "{file_path}" as it is outside the permitted working directory\n'

	# create file if it doesn't exist
	# if not os.path.exists(target_relative_path):
		# os.makedirs()

	with open(target_relative_path, "w") as f:
		f.write(content)
		return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'