
python
import pandas as pd

# Load the dataset
url = 'https://example.com/updated_uae_electricity_capacity.csv'
data = pd.read_csv(url)

# Display basic information about the dataset
def dataset_summary(df):
    print("Data Summary:")
    print(f"Number of rows: {df.shape[0]}")
    print(f"Number of columns: {df.shape[1]}")
    print("Column Names:", df.columns.tolist())

# Function to calculate total capacity by authority
def total_capacity_by_authority(df):
    total_capacity = df.groupby('Authority')['Capacity (MW)'].sum()
    print("\nTotal Electricity Generation Capacity by Authority:")
    print(total_capacity)

# Function to visualize capacity changes over the years
def plot_capacity_changes(df):
    import matplotlib.pyplot as plt
    df.groupby(['Year', 'Authority'])['Capacity (MW)'].sum().unstack().plot(kind='bar', stacked=True)
    plt.title('Electricity Generation Capacity Changes Over the Years')
    plt.ylabel('Capacity (MW)')
    plt.xlabel('Year')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Example usage
dataset_summary(data)
total_capacity_by_authority(data)
plot_capacity_changes(data)

