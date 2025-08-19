from google.genai import types
from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.run_python_file import run_python_file
from functions.write_file import write_file


def call_function(function_call_part, verbose=False):
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")

    function_name = function_call_part.name
    function_result = ""

    match function_name:
        case get_file_content.__name__:
            function_result = get_file_content(
                "./calculator", **function_call_part.args
            )
        case get_files_info.__name__:
            function_result = get_files_info("./calculator", **function_call_part.args)
        case run_python_file.__name__:
            function_result = run_python_file("./calculator", **function_call_part.args)
        case write_file.__name__:
            function_result = write_file("./calculator", **function_call_part.args)
        case _:
            return types.Content(
                role="tool",
                parts=[
                    types.Part.from_function_response(
                        name=function_name,
                        response={"error": f"Unknown function: {function_name}"},
                    )
                ],
            )

    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": function_result},
            )
        ],
    )
