# Python-to-Julia Code Converter

This project provides a Python-to-Julia code converter that helps in transforming Python scripts into equivalent Julia code. It uses syntax-based translation rules and customizable handlers for more complex scenarios. This document outlines the key syntax differences between Python and Julia, along with descriptions of potential handlers for conversion.

## Syntax Differences and Handlers

### 1. Functions
- **Python**: `def function_name(args):`
- **Julia**: `function function_name(args)`

**Handler**: Replace `def` with `function` and ensure indentation is adjusted to match Julia's style.

---

### 2. End Keyword
- **Python**: No explicit block termination (`:` is used).
- **Julia**: Explicit block termination with `end`.

**Handler**: Insert `end` at the correct locations for functions, loops, and conditional blocks.

---

### 3. Print Statements
- **Python**: `print("text")`
- **Julia**: `println("text")`

**Handler**: Replace `print` with `println`.

---

### 4. Comments
- **Python**: `# Comment`
- **Julia**: `# Comment` (identical, no handler required unless Python’s multiline comments are used).

---

### 5. String Interpolation
- **Python**: `f"Hello, {name}!"`
- **Julia**: `"Hello, $name!"`

**Handler**: Convert `f"{...}"` syntax into Julia's `$`-based interpolation.

---

### 6. Boolean Values
- **Python**: `True`, `False`
- **Julia**: `true`, `false`

**Handler**: Replace `True` with `true` and `False` with `false`.

---

### 7. None vs. Nothing
- **Python**: `None`
- **Julia**: `nothing`

**Handler**: Replace `None` with `nothing`.

---

### 8. Loops
#### For Loops
- **Python**: `for i in range(5):`
- **Julia**: `for i in 0:4` (Julia ranges are inclusive).

**Handler**: Convert `range(start, stop)` or `range(stop)` to Julia's `start:stop-1` or `0:stop-1`.

#### While Loops
- **Python**: `while condition:`
- **Julia**: `while condition`

**Handler**: Remove the trailing `:` and ensure `end` is added after the loop body.

---

### 9. Conditionals
- **Python**: `if condition:`, `elif condition:`, `else:`
- **Julia**: `if condition`, `elseif condition`, `else`

**Handler**: Remove the trailing `:` and replace `elif` with `elseif`.

---

### 10. List Comprehensions
- **Python**: `[x**2 for x in range(10)]`
- **Julia**: `[x^2 for x in 0:9]`

**Handler**: Adjust range syntax and replace Python's `**` operator with Julia's `^`.

---

### 11. Indexing
- **Python**: `list[0]` (0-based indexing)
- **Julia**: `list[1]` (1-based indexing)

**Handler**: Add 1 to all indices in Julia code.

---

### 12. Slicing
- **Python**: `list[start:stop]`
- **Julia**: `list[start+1:stop]`

**Handler**: Adjust slicing ranges by incrementing the start index by 1.

---

### 13. List Methods
#### Append
- **Python**: `list.append(item)`
- **Julia**: `push!(list, item)`

#### Pop
- **Python**: `list.pop()`, `list.pop(index)`
- **Julia**: `pop!(list)`, `deleteat!(list, index)`

#### Remove
- **Python**: `list.remove(value)`
- **Julia**: `deleteat!(list, findfirst(x -> x == value, list))`

**Handler**: Replace list method calls with Julia equivalents.

---

### 14. Tuples
- **Python**: `my_tuple = (1, 2, 3)`
- **Julia**: `my_tuple = (1, 2, 3)`

**Handler**: Generally no changes are required unless advanced tuple operations are performed.

---

### 15. Dictionaries
- **Python**: `my_dict = {"key": value}`
- **Julia**: `my_dict = Dict("key" => value)`

**Handler**: Replace `{key: value}` syntax with `Dict(key => value)`.

---

### 16. Classes
- **Python**:
    ```python
    class MyClass:
        def method(self):
            pass
    ```
- **Julia**:
    ```julia
    struct MyClass
        # Fields here
    end
    ```

**Handler**: Complex. Python's classes need to be converted to Julia's `struct` or `mutable struct`, with methods converted to standalone functions or Julia methods.

---

### 17. Import Statements
- **Python**: `import module`
- **Julia**: `using Module`

**Handler**: Replace `import` with `using`.

---

### 18. External Libraries
#### NumPy
- **Python**: `import numpy as np`
- **Julia**: `using LinearAlgebra` or `using Statistics` (and direct array operations).

**Handler**: Translate NumPy array operations to Julia equivalents.

#### Pandas
- **Python**: `import pandas as pd`
- **Julia**: `using DataFrames`

**Handler**: Map Pandas operations (`df['col']`, `.iloc`, etc.) to Julia's `DataFrame` operations.

---

### 19. Exception Handling
- **Python**:
    ```python
    try:
        pass
    except Exception as e:
        pass
    ```
- **Julia**:
    ```julia
    try
        # code
    catch e
        # handle error
    end
    ```

**Handler**: Replace `try:`, `except:` with Julia's `try`, `catch`, and ensure `end` is added.

---

### 20. Functions with Variable Arguments
- **Python**: `def func(*args, **kwargs):`
- **Julia**: `function func(args...; kwargs...)`

**Handler**: Replace `*args` with `args...` and `**kwargs` with `kwargs...`.

---

## Summary of Handlers

| **Feature**               | **Handler Description**                                                                 |
|---------------------------|-----------------------------------------------------------------------------------------|
| Block Termination         | Add `end` for functions, loops, and conditionals.                                       |
| Function Syntax           | Replace `def` with `function`.                                                         |
| Ranges and Loops          | Adjust `range` and loop ranges to Julia's inclusive syntax.                            |
| Indexing and Slicing      | Adjust to 1-based indexing and slice ranges.                                           |
| List Methods              | Replace Python list methods (`append`, `pop`, etc.) with Julia equivalents.            |
| String Interpolation      | Convert Python f-strings to Julia `$`-based interpolation.                             |
| Exception Handling        | Translate Python's `try/except` blocks to Julia's `try/catch`.                         |
| Libraries                 | Map NumPy/Pandas operations to Julia equivalents (e.g., `DataFrames`, `LinearAlgebra`).|
| Class Definitions         | Translate Python's `class` to Julia's `struct` or `mutable struct`.                    |

---

## Next Steps

- Extend handlers to cover more advanced Python and Julia features.
- Implement unit tests to validate conversions.
- Optimize for context-aware conversions, such as comprehensions or library-specific translations.

Feel free to contribute or suggest improvements!
