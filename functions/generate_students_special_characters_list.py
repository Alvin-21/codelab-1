import re

def find_special_char_names(data_file):
    # Regular expression to find names with special characters
    special_char_regex = re.compile(r"[^\w\s,]")
    
    # Filter names with special characters
    special_names = data_file[data_file['Student Name'].apply(lambda name: bool(special_char_regex.search(name)))]
    
    # Return the list of names with special characters
    return special_names['Student Name'].tolist()