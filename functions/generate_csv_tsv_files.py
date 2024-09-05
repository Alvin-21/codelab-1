import pandas as pd

def save_list_as_csv(data_list, csv_file_path):
    # Convert list of dictionaries to a DataFrame
    data_file = pd.DataFrame(data_list)

    # Save DataFrame as CSV
    data_file.to_csv(csv_file_path, index=False)

def save_list_as_tsv(data_list, tsv_file_path):
    # Convert list of dictionaries to a DataFrame
    data_file = pd.DataFrame(data_list)

    # Save DataFrame as CSV
    data_file.to_csv(tsv_file_path, sep='\t', index=False)