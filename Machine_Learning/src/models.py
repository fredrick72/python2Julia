import torch
from torch import nn
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

class CodeTranslator:
    def __init__(self, model_name="t5-small"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    def train(self, train_data, test_data, epochs=3, batch_size=8, learning_rate=5e-5):
        optimizer = torch.optim.AdamW(self.model.parameters(), lr=learning_rate)
        loss_fn = nn.CrossEntropyLoss()

        for epoch in range(epochs):
            self.model.train()
            for i, (input_text, target_text) in enumerate(train_data):
                inputs = self.tokenizer(input_text, return_tensors="pt", padding=True, truncation=True)
                labels = self.tokenizer(target_text, return_tensors="pt", padding=True, truncation=True).input_ids
                outputs = self.model(**inputs, labels=labels)
                loss = outputs.loss

                optimizer.zero_grad()
                loss.backward()
                optimizer.step()

                if i % 10 == 0:
                    print(f"Epoch {epoch+1}, Step {i}, Loss: {loss.item()}")

    def predict(self, code_snippet):
        self.model.eval()
        inputs = self.tokenizer(code_snippet, return_tensors="pt", padding=True, truncation=True)
        outputs = self.model.generate(**inputs)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
