import json
from sklearn.model_selection import train_test_split

def load_data(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)
    python_code = [item["python_code"] for item in data]
    julia_code = [item["julia_code"] for item in data]
    return python_code, julia_code

def preprocess_data(python_code, julia_code):
    # Tokenize the code (simple split by space or use a library like Tokenizer)
    return python_code, julia_code

def prepare_data(file_path):
    python_code, julia_code = load_data(file_path)
    python_code, julia_code = preprocess_data(python_code, julia_code)
    return train_test_split(python_code, julia_code, test_size=0.2, random_state=42)

if __name__ == "__main__":
    train_input, test_input, train_output, test_output = prepare_data("../data/examples.json")
    print("Data loaded and split successfully.")
