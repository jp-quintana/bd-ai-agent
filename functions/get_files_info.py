import os
from google import genai


def get_files_info(
    working_directory,
    directory=".",
):
    abs_working_directory = os.path.abspath(working_directory)
    target_dir = os.path.abspath(os.path.join(working_directory, directory))

    if not target_dir.startswith(abs_working_directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'

    try:
        res = ""

        for item in os.listdir(target_dir):
            curr = f"- {item}:"
            target = os.path.join(target_dir, item)
            curr += f" file_size: {os.path.getsize(target)} bytes,"
            curr += f" is_dir={os.path.isdir(target)}"
            res += curr + "\n"

        return res[:-1]
    except Exception as e:
        return f"Error listing files: {e}"


types = genai.types

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
