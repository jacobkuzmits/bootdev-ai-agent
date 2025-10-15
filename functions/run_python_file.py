import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
	target_relative_path = os.path.join(working_directory, file_path)
	target_absolute_path = os.path.abspath(target_relative_path)
	current_absolute_path = os.path.abspath(working_directory)

	# prevent escaping the working_directory
	if not target_absolute_path.startswith(current_absolute_path):
		return f'    Error: Cannot execute "{file_path}" as it is outside the permitted working directory\n'
	
	# verify file_path exists
	if not os.path.isfile(target_relative_path):
		return f'    Error: File "{file_path}" not found.'
	
	# verify file_path is a python file
	if not file_path.endswith(".py"):
		return f'    Error: "{file_path}" is not a Python file.'
	
	try:
		result = subprocess.run(['uv', 'run', target_absolute_path] + args, timeout=30, cwd=working_directory, capture_output=True)
		result_string = f"STDOUT: {result.stdout}\n"
		result_string += f"STDERR: {result.stderr}\n"
		if result.returncode != 0:
			result_string += f"Process exited with code {result.returncode}"
		return result_string
	except Exception as e:
		return f"Error: executing Python file: {e}"