import matplotlib.pyplot as plt

print("🚀 Starting graph generation...")

# Data
rounds = [1, 2, 3]
accuracy = [0.75, 0.82, 0.86]

# Plot
plt.figure()
plt.plot(rounds, accuracy, marker='o')
plt.title("Federated Learning Accuracy per Round")
plt.xlabel("Rounds")
plt.ylabel("Accuracy")
plt.grid()

# Save graph
plt.savefig("accuracy_graph.png")

print("✅ Graph saved as accuracy_graph.png")

# Show graph
plt.show()

print("✅ Done")