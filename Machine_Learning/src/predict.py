from model import CodeTranslator

if __name__ == "__main__":
    code_snippet = """
    def greet(name):
        print(f"Hello, {name}!")
    """
    model = CodeTranslator()
    prediction = model.predict(code_snippet)
    print("Generated Julia Code:")
    print(prediction)
