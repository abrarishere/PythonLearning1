# plugins.py
from prettier import format_code
from autotyper import autotype

# Example usage
code_to_format = "def example_function(x): print(x)"
formatted_code = format_code(code_to_format, "python")
print("Formatted Code:")
print(formatted_code)

# Example autotyping
text_to_type = "Hello, World!"
autotype(text_to_type)
