import os
import shutil

def move_and_rename_images(base_folder):
    image_counter = 1
    test_folder = os.path.join(base_folder, 'test')

    # Create the 'test' folder if it doesn't exist
    if not os.path.exists(test_folder):
        os.makedirs(test_folder)

    # Walk through all subdirectories in the base folder
    for root, dirs, files in os.walk(base_folder):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg')):
                source_path = os.path.join(root, file)
                new_filename = f"{image_counter}.jpg"
                destination_path = os.path.join(test_folder, new_filename)

                # Move and rename the file
                shutil.move(source_path, destination_path)
                image_counter += 1

if __name__ == "__main__":
    base_folder = 'test'  # Replace with the path to your base folder
    move_and_rename_images(base_folder)
