# Psychology Use Case: Reaction Time Analysis by Stimulus Type
#
# This script simulates a simple experiment to measure reaction times
# to different types of stimuli (visual and auditory) and visualizes the results.
# It also performs a t-test to compare the means of the two groups.

# Pandas is a fast, powerful, flexible, and easy-to-use open-source data analysis and manipulation tool.
import pandas as pd

# NumPy is the fundamental package for scientific computing with Python.
# It contains among other things a powerful N-dimensional array object.
import numpy as np

# Seaborn is a Python data visualization library based on matplotlib.
# It provides a high-level interface for drawing attractive statistical graphics.
import seaborn as sns 

# Matplotlib is a plotting library for the Python programming language and its
# numerical mathematics extension NumPy.
import matplotlib.pyplot as plt

# Set plot style
sns.set_theme(style="whitegrid")

# Simulated data for 100 participants
np.random.seed(42)
n = 100  # Number of participants
data = pd.DataFrame({
    'ParticipantID': range(1, n + 1),
    'StimulusType': np.random.choice(['Visual', 'Auditory'], size=n),
    'ReactionTime_ms': np.concatenate([
        np.random.normal(loc=350, scale=20, size=n//2),  # Visual
        np.random.normal(loc=250, scale=20, size=n//2)   # Auditory
    ])
})

# Preview the data
print("Sample Data:\n", data.head())

# Summary statistics
summary = data.groupby('StimulusType')['ReactionTime_ms'].describe()
print("\nDescriptive Statistics:\n", summary)

# Boxplot
plt.figure(figsize=(8, 5))
sns.boxplot(x='StimulusType', y='ReactionTime_ms', hue='StimulusType', data=data, palette="pastel", legend=False)
plt.title("Reaction Time by Stimulus Type")
plt.ylabel("Reaction Time (ms)")
plt.show()

# Violin plot with individual data points
plt.figure(figsize=(8, 5))
sns.violinplot(x='StimulusType', y='ReactionTime_ms', hue='StimulusType', data=data, inner=None, palette="muted", legend=False)
sns.stripplot(x='StimulusType', y='ReactionTime_ms', data=data, color='k', alpha=0.5)
plt.title("Distribution of Reaction Times")
plt.ylabel("Reaction Time (ms)")
plt.show()

# T-test (optional, for statistical significance)
from scipy.stats import ttest_ind

visual_rt = data[data['StimulusType'] == 'Visual']['ReactionTime_ms']
auditory_rt = data[data['StimulusType'] == 'Auditory']['ReactionTime_ms']
t_stat, p_val = ttest_ind(visual_rt, auditory_rt)
print(f"\nT-test: t = {t_stat:.2f}, p = {p_val:.4f}")
