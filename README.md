
# Comprehensive Electricity Generation Capacity Database for the UAE

## Overview

This repository contains scripts and data to analyze the electricity generation capacity by various authorities in the UAE. The dataset is updated to include recent years, providing a comprehensive view of the energy landscape and enabling stakeholders to make informed decisions.

## Dataset

The dataset includes the following columns:
- `Year`: The year of data entry.
- `Authority`: The energy authority (e.g., Abu Dhabi, Dubai).
- `Capacity (MW)`: The electricity generation capacity in megawatts.
- `Energy Type`: The type of energy source (e.g., solar, wind, fossil fuel).

## Requirements

- Python 3.x
- Pandas
- Matplotlib

You can install the required Python packages via pip:

bash
pip install pandas matplotlib


## Usage

1. Clone the repository:

bash
git clone https://github.com/yourusername/uae-electricity-capacity.git
cd uae-electricity-capacity


2. Load and analyze the dataset:

python
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('updated_uae_electricity_capacity.csv')

# Analyze the dataset
from analysis_script import dataset_summary, total_capacity_by_authority, plot_capacity_changes

dataset_summary(data)
total_capacity_by_authority(data)
plot_capacity_changes(data)


## Contribution

Contributions to improve the dataset and scripts are welcome. Please fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License.
