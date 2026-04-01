import flwr as fl
import torch
import pandas as pd
from model import HeartModel

# Load data
df = pd.read_csv("heart_clean.csv")

X = df.drop("target", axis=1).values
y = df["target"].values

X = torch.tensor(X, dtype=torch.float32)
y = torch.tensor(y, dtype=torch.float32).view(-1, 1)

model = HeartModel()

def train():
    optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
    loss_fn = torch.nn.BCELoss()

    for _ in range(3):
        optimizer.zero_grad()
        output = model(X)
        loss = loss_fn(output, y)
        loss.backward()
        optimizer.step()

class Client(fl.client.NumPyClient):
    def get_parameters(self, config):
        return [val.detach().numpy() for val in model.parameters()]

    def set_parameters(self, parameters):
        for param, val in zip(model.parameters(), parameters):
            param.data = torch.tensor(val)

    def fit(self, parameters, config):
        self.set_parameters(parameters)
        train()
        return self.get_parameters(config), len(X), {}

    def evaluate(self, parameters, config):
        self.set_parameters(parameters)

        with torch.no_grad():
            output = model(X)
            preds = (output > 0.5).float()
            accuracy = (preds.eq(y).sum().item()) / len(y)

        return 0.0, len(X), {"accuracy": accuracy}

fl.client.start_numpy_client(server_address="localhost:8080", client=Client())