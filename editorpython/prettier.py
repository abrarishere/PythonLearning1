# prettier.py
import autopep8
import jsbeautifier
import black
import yapf
import sqlparse
import yapf
import subprocess
def format_python_code(code):
    """
    Format Python code using autopep8.
    """
    return autopep8.fix_code(code)

def format_javascript_code(code):
    """
    Format JavaScript code using jsbeautifier.
    """
    return jsbeautifier.beautify(code)

def format_java_code(code, file_name):
    """
    Format Java code using google-java-format.
    """
    # Write the code to a temporary file
    with open(file_name, 'w') as f:
        f.write(code)

    # Run google-java-format-diff.py with the --replace option
    subprocess.run(["python", "google-java-format-diff.py", "--replace", file_name])

    # Read the formatted code from the file
    with open(file_name, 'r') as f:
        formatted_code = f.read()

    return formatted_code


def format_go_code(code):
    """
    Format Go code using gofmt.
    """
    return yapf.format(code)


def format_sql_code(code):
    """
    Format SQL code using sqlparse.
    """
    return sqlparse.format(code, reindent=True)

def format_code(code, language):
    """
    Format code based on the specified language.
    """
    language = language.lower()

    if language == "python":
        return format_python_code(code)
    elif language == "javascript" or language == "js":
        return format_javascript_code(code)
    elif language == "java":
        return format_java_code(code)
    elif language == "go":
        return format_go_code(code)
    elif language == "sql":
        return format_sql_code(code)
    else:
        # Add more conditions for other languages as needed.
        return code

if __name__ == "__main__":
    # Example usage:
    python_code = """
    def   example_function   (   x  )  :
        print (x )
    """
    formatted_python_code = format_code(python_code, "python")
    print("Formatted Python Code:")
    print(formatted_python_code)

    javascript_code = "const example = (x) => { console.log(x); };"
    formatted_javascript_code = format_code(javascript_code, "javascript")
    print("Formatted JavaScript Code:")
    print(formatted_javascript_code)

    sql_code = "SELECT * FROM table WHERE condition;"
    formatted_sql_code = format_code(sql_code, "sql")
    print("Formatted SQL Code:")
    print(formatted_sql_code)
