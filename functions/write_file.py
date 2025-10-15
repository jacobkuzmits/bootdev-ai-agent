import os
from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes to a specified file. Creates the file if it doesn't exist, or overwrites it if it does. Constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The relative path of the file to write. Constrained to the working directory.",
            ),
			"content": types.Schema(
				type=types.Type.OBJECT,
				description="The file content to write."
			)
        },
    ),
)

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