# # Communications Use Case: media influence may want to understand how different post types perform
# on social media in terms of likes, comments, and shares.
#
# This script analyzes social media engagement data, calculates total engagement,
# and visualizes the results using bar plots and heatmaps.

# Pandas is a fast, powerful, flexible, and easy-to-use open-source data analysis and manipulation tool.
import pandas as pd

# Matplotlib is a plotting library for the Python programming language and its
# numerical mathematics extension NumPy.
import matplotlib.pyplot as plt

# Seaborn is a Python data visualization library based on matplotlib.
# It provides a high-level interface for drawing attractive statistical graphics.
import seaborn as sns

# Load the dataset
df = pd.read_csv("Live.csv")

# Display the first few rows of the unprocessed DataFrame
print(df.head())

# Combine one-hot encoded columns into a single 'Post_Type' column
status_type_columns = ['status_type_link', 'status_type_photo', 'status_type_status', 'status_type_video']

# The decode_post_type function checks each one-hot encoded column and
# returns the corresponding post type.
def decode_post_type(row):
    for col in status_type_columns:
        if row[col] == 1:
            return col.replace("status_type_", "").capitalize()
    return "Unknown"

# The decode_post_type function checks each one-hot encoded column and returns the corresponding post type.
df['Post_Type'] = df.apply(decode_post_type, axis=1)

# Optional: Drop the original one-hot encoded columns
df.drop(columns=status_type_columns, inplace=True)

# Calculate total engagement (sum of all reaction types)
reaction_cols = ['num_reactions', 'num_comments', 'num_shares']
df['Total_Engagement'] = df[reaction_cols].sum(axis=1)

 # Display the first few rows of the DataFrame
print(df.head())

# Summary statistics
print("Summary Statistics:")
print(df.describe())

# Average engagement by post type
avg_engagement = df.groupby('Post_Type')['Total_Engagement'].mean().sort_values(ascending=False)
print("\nAverage Engagement by Post Type:")
print(avg_engagement)

# Plot average engagement by post type
plt.figure(figsize=(8, 6))
sns.barplot(x=avg_engagement.index, y=avg_engagement.values, palette="viridis")
plt.title("Average Total Engagement by Post Type")
plt.xlabel("Post Type")
plt.ylabel("Avg Total Engagement")
plt.tight_layout()
plt.show()

# Correlation heatmap of engagement metrics
# How much one variable increases or decreases when another variable changes.
# The correlation coefficient is a statistical measure that describes the strength
# and direction of a relationship between two variables.
#
# It ranges from -1 to 1:
#
# +1 → perfect positive correlation (both go up together)
# 0 → no correlation
# -1 → perfect negative correlation (one goes up, the other goes down)
#
plt.figure(figsize=(8, 6))
sns.heatmap(df[reaction_cols + ['Total_Engagement']].corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Between Engagement Metrics")
plt.tight_layout()
plt.show()