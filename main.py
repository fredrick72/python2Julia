import re

class PythonToJuliaConverter:
    def __init__(self):
        # Initialize with basic translations
        self.translation_rules = [
            (r"def\s+(\w+)\((.*?)\):", r"function \1(\2)"),  # Functions
            (r"if\s+(.*):", r"if \1"),                     # If statements
            (r"elif\s+(.*):", r"elseif \1"),               # Elif to elseif
            (r"else:", r"else"),                           # Else statements
            (r"for\s+(\w+)\s+in\s+range\((.*)\):", r"for \1 in 0:(\2-1)"),  # For loops with range
            (r"for\s+(\w+)\s+in\s+(.*):", r"for \1 in \2"), # General for loops
            (r"while\s+(.*):", r"while \1"),               # While loops
            (r"print\((.*)\)", r'println(\1)'),            # Print statements
            (r"True", r"true"),                            # Boolean True
            (r"False", r"false"),                          # Boolean False
            (r"None", r"nothing"),                         # None to nothing
            (r"(\w+)\.append\((.*)\)", r"push!(\1, \2)"),  # List append
        ]
        self.custom_handlers = []

    def add_translation_rule(self, pattern, replacement):
        """Add a new basic translation rule."""
        self.translation_rules.append((pattern, replacement))

    def add_custom_handler(self, handler):
        """Add a custom handler for complex conversions."""
        self.custom_handlers.append(handler)

    def convert(self, python_code):
        """Perform the conversion."""
        julia_code = python_code
        
        # Apply basic translation rules
        for pattern, replacement in self.translation_rules:
            julia_code = re.sub(pattern, replacement, julia_code)
        
        # Apply custom handlers
        for handler in self.custom_handlers:
            julia_code = handler(julia_code)
        
        return julia_code

# Example of a custom handler for f-strings
def convert_f_strings(code):
    """Convert Python f-strings to Julia string interpolation."""
    pattern = r'f"(.*?)"'
    def replacer(match):
        content = match.group(1)
        # Replace Python-style placeholders with Julia-style
        julia_content = re.sub(r'\{(.*?)\}', r'$\1', content)
        return f'"{julia_content}"'
    return re.sub(pattern, replacer, code)

# Usage
converter = PythonToJuliaConverter()

# Add a custom handler for f-strings
converter.add_custom_handler(convert_f_strings)

# Add a new translation rule for list slicing
converter.add_translation_rule(r"(\w+)\[(\d+):(\d+)\]", r"\1[\2+1:\3]")

python_code = """
# Example Python code
def greet(name):
    print(f"Hello, {name}!")

if True:
    print("This is true")
else:
    print("This is false")

for i in range(5):
    print(i)

my_list = [1, 2, 3]
my_list.append(4)
print(my_list[1:3])
"""

julia_code = converter.convert(python_code)
print("Converted Julia Code:")
print(julia_code)
