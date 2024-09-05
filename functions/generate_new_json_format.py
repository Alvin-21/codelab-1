import json

def transform_to_custom_json(data_file, special_char_names):
    # List to store the transformed data
    data_list = []

    for index, row in data_file.iterrows():
        student_data = {
            "id": str(index), 
            "student_number": row['Student Number'],
            "additional_details": [
                {
                    "dob": row['DoB'].strftime("%Y-%m-%d"),
                    "gender": row['Gender'].lower(),
                    "special_character": "['yes']" if row['Student Name'] in special_char_names else "['no']"
                }
            ]
        }
        data_list.append(student_data)

    # Convert list to JSON format
    json_data = json.dumps(data_list, indent=4)

    return json_data

def save_to_json_file(json_data, file_path):
    with open(file_path, 'w') as file:
        file.write(json_data)