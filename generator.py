import os
import datetime

# TODO: Grab from terminal
AUTHOR = "William Hass"
PROJECT_NAME = "Guidebook"
MODULE_NAME = "Survey"

AUTHOR = raw_input("Author full name: ")
PROJECT_NAME = raw_input("Project name: ")
MODULE_NAME = raw_input("Module name: ")

ARE_YOU_READY = raw_input("Are you ready to generate the module? (y/n): ")
if ARE_YOU_READY != "y":
    print "Operation canceled: Nothing was created"
    exit()

today = datetime.datetime.today()
today_string = datetime.datetime.strftime(today, "%d-%m-%Y_%H:%M:%S")
today_date_string = datetime.datetime.strftime(today, "%Y-%m-%d")

# Constants
FILE_MODULE_PLACEHOLDER = "__"
PROJECT_NAME_PLACEHOLDER = "$_PROJECT_NAME"
AUTHOR_NAME_PLACEHOLDER = "$_AUTHOR"
FILE_CREATION_DATE_PLACEHOLDER = "$_DATE"

FILES_REPLACEMENT = {
    FILE_MODULE_PLACEHOLDER: MODULE_NAME,
    PROJECT_NAME_PLACEHOLDER: PROJECT_NAME,
    AUTHOR_NAME_PLACEHOLDER: AUTHOR,
    FILE_CREATION_DATE_PLACEHOLDER: today_date_string
}

# Folders
CURRENT_MODULE_FOLDER = today_string
CONCRETE_CLASSES_FOLDER_NAME = "concrete_classes"
PROTOCOLS_FOLDER_NAME = "protocols"
OUTPUT_FOLDER_NAME = "output"

# Paths
CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
CONCRETE_CLASSES_PATH = os.path.join(
                                CURRENT_DIRECTORY,
                                CONCRETE_CLASSES_FOLDER_NAME)
PROTOCOLS_PATH = os.path.join(CURRENT_DIRECTORY, PROTOCOLS_FOLDER_NAME)
OUTPUT_PATH = os.path.join(CURRENT_DIRECTORY, OUTPUT_FOLDER_NAME)
CURRENT_MODULE_PATH = os.path.join(OUTPUT_PATH, CURRENT_MODULE_FOLDER)
CURRENT_MODULE_PROTOCOLS_PATH = os.path.join(
                                        CURRENT_MODULE_PATH,
                                        PROTOCOLS_FOLDER_NAME)
CURRENT_MODULE_CONCRETE_CLASSES_PATH = os.path.join(
                                                CURRENT_MODULE_PATH,
                                                CONCRETE_CLASSES_FOLDER_NAME)

# Create dirs
if not os.path.exists(CURRENT_MODULE_PROTOCOLS_PATH):
    os.makedirs(CURRENT_MODULE_PROTOCOLS_PATH)

if not os.path.exists(CURRENT_MODULE_CONCRETE_CLASSES_PATH):
    os.makedirs(CURRENT_MODULE_CONCRETE_CLASSES_PATH)


def generate(
            from_path,
            to_path,
            module_name,
            code_placeholder_replacement,
            file_name_placeholder_replacement):
    # Create protocols
    files_names = os.listdir(from_path)
    for file_name in files_names:
        full_path = os.path.join(from_path, file_name)
        if os.path.isdir(full_path):
            continue

        # Open file and copy content
        file = open(full_path, "r")
        file_content = file.read()
        file.close()
        for key in code_placeholder_replacement:
            value = code_placeholder_replacement[key]
            file_content = file_content.replace(key, value)

        # Create output file
        new_file_name = file_name.replace(
                                        file_name_placeholder_replacement,
                                        module_name)
        new_path = os.path.join(to_path, new_file_name)
        new_file = open(new_path, "a+")
        new_file.write(file_content)
        new_file.close()
        print "Created: " + str(new_path)


generate(
    from_path=PROTOCOLS_PATH,
    to_path=CURRENT_MODULE_PROTOCOLS_PATH,
    module_name=MODULE_NAME,
    code_placeholder_replacement=FILES_REPLACEMENT,
    file_name_placeholder_replacement=FILE_MODULE_PLACEHOLDER)

generate(
    from_path=CONCRETE_CLASSES_PATH,
    to_path=CURRENT_MODULE_CONCRETE_CLASSES_PATH,
    module_name=MODULE_NAME,
    code_placeholder_replacement=FILES_REPLACEMENT,
    file_name_placeholder_replacement=FILE_MODULE_PLACEHOLDER)
