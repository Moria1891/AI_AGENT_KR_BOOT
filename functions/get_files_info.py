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

    full_path = os.path.join(working_directory, directory)
    abs_full_path = os.path.abspath(full_path)
    abs_working_directory = os.path.abspath(working_directory)
    
    if not abs_full_path.startswith(abs_working_directory):
        return(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
    
    elif not os.path.isdir(abs_full_path):
        return (f'Error: "{directory}" is not a directory')
    
    else:
        try:
            output = []
            # if directory == ".":
            #    header = "Result for current directory:\n"
            # else:
            #    header = f"Result for '{directory}' directory:\n"
            for file in os.listdir(abs_full_path):
                if file != "__pycache__":
                    item_path = os.path.join(abs_full_path, file)
                    size = os.path.getsize(item_path)
                    is_dir = os.path.isdir(item_path)
                    output.append(f"- {file}: file_size={size} bytes, is_dir={is_dir}")
            return "\n".join(output)
        except Exception as e:
            return f"Error: {e}"