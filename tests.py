from functions.run_python_file import run_python_file


def test():
    print('\n--- Test 1: run_python_file("calculator", "main.py") ---')
    result = run_python_file("calculator", "main.py")
    print(result)

    print('\n--- Test 2: run_python_file("calculator", "main.py", ["3 + 5"]) ---')
    result = run_python_file("calculator", "main.py", ["3 + 5"])
    print(result)

    print('\n--- Test 3: run_python_file("calculator", "tests.py") ---')
    result = run_python_file("calculator", "tests.py")
    print(result)

    print('\n--- Test 4: run_python_file("calculator", "../main.py") ---')
    result = run_python_file("calculator", "../main.py")
    print(result)

    print('\n--- Test 5: run_python_file("calculator", "nonexistent.py") ---')
    result = run_python_file("calculator", "nonexistent.py")
    print(result)


if __name__ == "__main__":
    test()
