def separate_students_by_gender(data_file):
    male_students = data_file[data_file['Gender'] == 'M']['Student Name'].tolist()
    female_students = data_file[data_file['Gender'] == 'F']['Student Name'].tolist()

    # Logging the number of male and female students
    print(f"Number of male students: {len(male_students)}")
    print(f"Number of female students: {len(female_students)}")
    
    return male_students, female_students
