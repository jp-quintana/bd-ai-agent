import os
import subprocess
from google import genai


def run_python_file(working_directory, file_path, args=[]):
    abs_working_directory = os.path.abspath(working_directory)
    target_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not target_file_path.startswith(abs_working_directory):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(target_file_path):
        return f'Error: File "{file_path}" not found.'

    if not target_file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    commands = ["python", target_file_path]

    if args:
        commands.extend(args)

    try:
        completed_process = subprocess.run(
            commands,
            timeout=30,
            cwd=abs_working_directory,
            capture_output=True,
            text=True,
        )
        stdout = completed_process.stdout
        stderr = completed_process.stderr
        output_parts = []

        if stdout:
            output_parts.append(f"STDOUT:\n{stdout.strip()}")
        if stderr:
            output_parts.append(f"STDERR:\n{stderr.strip()}")

        if completed_process.returncode != 0:
            output_parts.append(
                f"Process exited with code {completed_process.returncode}"
            )

        if not output_parts:
            return "No output produced."

        return "\n".join(output_parts)
    except Exception as e:
        return f"Error: executing Python file: {e}"


types = genai.types

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a Python file within the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the Python file to be executed, relative to the working directory. Must end with '.py'",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(type=types.Type.STRING),
                description="A list of command-line arguments to pass to the script.",
            ),
        },
        required=["file_path"],
    ),
)
