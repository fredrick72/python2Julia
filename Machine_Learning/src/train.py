from data_preprocessing import prepare_data
from model import CodeTranslator

if __name__ == "__main__":
    file_path = "../data/examples.json"
    train_input, test_input, train_output, test_output = prepare_data(file_path)

    train_data = list(zip(train_input, train_output))
    test_data = list(zip(test_input, test_output))

    model = CodeTranslator()
    model.train(train_data, test_data)
    print("Training complete. Save the model for future use.")
