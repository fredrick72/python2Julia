from model import CodeTranslator
from data_preprocessing import prepare_data

def evaluate_model(model, test_data):
    correct = 0
    for python_code, julia_code in test_data:
        prediction = model.predict(python_code)
        if prediction.strip() == julia_code.strip():
            correct += 1
    accuracy = correct / len(test_data)
    return accuracy

if __name__ == "__main__":
    file_path = "../data/examples.json"
    _, test_input, _, test_output = prepare_data(file_path)
    test_data = list(zip(test_input, test_output))

    model = CodeTranslator()
    accuracy = evaluate_model(model, test_data)
    print(f"Model accuracy: {accuracy * 100:.2f}%")
