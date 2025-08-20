# Interactive Data Analysis with Marimo
# Author: 23f3004267@ds.study.iitm.ac.in
# This notebook demonstrates variable dependencies, interactive widgets,
# and dynamic markdown output.

import marimo as mo

# --- Cell 1: Define dataset and initial parameters ---
# This cell initializes the dataset and sets up core variables.
data = [i for i in range(1, 51)]  # Simple dataset: 1 through 50

# --- Cell 2: Interactive slider to control analysis window size ---
# The slider value will be used in subsequent cells to compute results.
window_size = mo.ui.slider(1, 20, label="Window Size")
window_size

# --- Cell 3: Dependent calculation ---
# This cell depends on both `data` and the slider `window_size`.
# It computes a rolling mean based on the current slider value.
import numpy as np

rolling_mean = [
    np.mean(data[i:i+window_size.value])
    for i in range(len(data) - window_size.value + 1)
]
rolling_mean

# --- Cell 4: Dynamic markdown output ---
# This cell demonstrates self-documenting interactivity.
mo.md(f"## Rolling Mean Analysis\n\n"
      f"Using a window size of **{window_size.value}**, "
      f"the rolling mean has {len(rolling_mean)} values.\n\n"
      f"Example values: {rolling_mean[:5]} ...")
