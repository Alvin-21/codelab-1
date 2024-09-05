import logging

# Configure the logging settings
logging.basicConfig(filename='system_logs.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def separate_students_by_gender(data_file):
    male_students = data_file[data_file['Gender'] == 'M']['Student Name'].tolist()
    female_students = data_file[data_file['Gender'] == 'F']['Student Name'].tolist()

   # Log the number of male and female students
    logging.info(f"Number of male students: {len(male_students)}")
    logging.info(f"Number of female students: {len(female_students)}")
    
    return male_students, female_students
