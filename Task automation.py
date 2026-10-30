
import os
import shutil

def organize_jpg_files(source_folder, destination_folder):

    # Check whether source folder exists
    if not os.path.exists(source_folder):
        print("Source folder does not exist!")
        return

    # Create destination folder if it doesn't exist
    os.makedirs(destination_folder, exist_ok=True)

    count = 0

    # Read all files from source folder
    for filename in os.listdir(source_folder):

        # Check for JPG files
        if filename.lower().endswith(".jpg"):

            source_path = os.path.join(source_folder, filename)
            destination_path = os.path.join(
                destination_folder, filename
            )

            # Avoid overwriting existing files
            if os.path.exists(destination_path):
                name, extension = os.path.splitext(filename)
                number = 1

                while os.path.exists(destination_path):
                    new_filename = f"{name}_{number}{extension}"
                    destination_path = os.path.join(
                        destination_folder, new_filename
                    )
                    number += 1

            # Move the file
            shutil.move(source_path, destination_path)

            print(f"Moved: {filename}")
            count += 1

    print("\nAutomation Completed Successfully!")
    print("Total JPG files moved:", count)


# Main program
print("===================================")
print("     CODEALPHA TASK AUTOMATION")
print("===================================")

source = input("Enter source folder path: ")
destination = input("Enter destination folder path: ")

try:
    organize_jpg_files(source, destination)
except Exception as error:
    print("Error:", error)
