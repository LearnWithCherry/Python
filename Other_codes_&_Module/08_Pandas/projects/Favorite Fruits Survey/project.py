import pandas as pd

# Step 1: Create a dataset
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Favorite Fruit": ["Apple", "Banana", "Apple", "Mango", "Banana"]
}

# Step 2: Convert it to a DataFrame
df = pd.DataFrame(data)

# Step 3: Count how many people like each fruit
fruit_counts = df["Favorite Fruit"].value_counts()

# Step 4: Show the results
print("Fruit Counts:")
print(fruit_counts)
