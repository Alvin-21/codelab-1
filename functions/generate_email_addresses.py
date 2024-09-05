import re

def generate_email(name):
    # Clean the name by removing special characters
    clean_name = re.sub(r"[^a-zA-Z\s]", "", name)
    parts = clean_name.split(" ")
    email = f"{parts[0][0].lower()}{parts[-1].lower()}@gmail.com"
    return email

# df['Email'] = df['Student Name'].apply(generate_email)