from functions import generate_email_addresses, generate_separate_lists, generate_students_special_characters_list, generate_new_json_format, generate_csv_tsv_files
import pandas as pd


if __name__ == "__main__":
    # File A

    # Read the xlsx file to manipulate it
    file_a = pd.read_excel("./input_files/Test_Files.xlsx", sheet_name="File_A")

    # Generate the email addresses for the students
    file_a['Email Address'] = file_a['Student Name'].apply(generate_email_addresses.generate_email)

    # Generate list of male and female students of File_A
    male_students, female_students = generate_separate_lists.separate_students_by_gender(file_a)
    generate_csv_tsv_files.save_list_as_tsv(male_students, "./output_files/file_a_male_students.tsv")
    generate_csv_tsv_files.save_list_as_csv(female_students, "./output_files/file_a_female_students.csv")

    # Find names with special characters of File_A
    special_names = generate_students_special_characters_list.find_special_char_names(file_a)
    generate_csv_tsv_files.save_list_as_csv(special_names, "./output_files/file_a_special_names.csv")

    # Shuffle the names of File_A and save them in a json file
    fila_a_shuffled = file_a.sample(frac=1)
    fila_a_shuffled.to_json("./output_files/file_a.json", orient='records')

    # Save the file in a custom json format
    json_data = generate_new_json_format.transform_to_custom_json(file_a, special_names)
    generate_new_json_format.save_to_json_file(json_data, "./output_files/file_a_new_format.json")


    # File B

    # Read the xlsx file to manipulate it
    file_b = pd.read_excel("./input_files/Test_Files.xlsx", sheet_name="File_B")

    # Generate the email addresses for the students
    file_b['Email Address'] = file_b['Student Name'].apply(generate_email_addresses.generate_email)

    # Generate list of male and female students of File_B
    male_students, female_students = generate_separate_lists.separate_students_by_gender(file_b)
    generate_csv_tsv_files.save_list_as_tsv(male_students, "./output_files/file_b_male_students.tsv")
    generate_csv_tsv_files.save_list_as_csv(female_students, "./output_files/file_b_female_students.csv")

    # Find names with special characters of File_B
    special_names = generate_students_special_characters_list.find_special_char_names(file_b)
    generate_csv_tsv_files.save_list_as_csv(special_names, "./output_files/file_b_special_names.csv")

    # Shuffle the names of File_B and save them in a json file
    fila_b_shuffled = file_b.sample(frac=1)
    fila_b_shuffled.to_json("./output_files/file_b.json", orient='records')

    # Save the file in a custom json format
    json_data = generate_new_json_format.transform_to_custom_json(file_b, special_names)
    generate_new_json_format.save_to_json_file(json_data, "./output_files/file_b_new_format.json")