def separate_students_by_gender(data_file):
    male_students = data_file[data_file['Gender'] == 'M']['Student Name'].tolist()
    female_students = data_file[data_file['Gender'] == 'F']['Student Name'].tolist()

    return male_students, female_students