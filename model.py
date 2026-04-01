import torch
import torch.nn as nn

class HeartModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(13, 16)
        self.fc2 = nn.Linear(16, 1)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.sigmoid(self.fc2(x))
        return x