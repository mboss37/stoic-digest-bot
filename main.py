import os
from datetime import datetime
import time  # Added for the sleep functionality
from summary_generator import generate_summary

source_folder = 'letters_to_process'
processed_folder = 'processed_letters'
summary_folder = 'summary'

def move_file_to_processed(filename):
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    new_filename = f"{filename.split('.')[0]}_{timestamp}.txt"
    os.rename(os.path.join(source_folder, filename), os.path.join(processed_folder, new_filename))

def save_summary_to_file(filename, summary):
    summary_filename = f"{filename.split('.')[0]}_summary.txt"
    with open(os.path.join(summary_folder, summary_filename), 'w') as file:
        file.write(summary)

def main():
    while True:  # Initiating an infinite loop
        files_processed_in_this_iteration = 0
        for filename in os.listdir(source_folder):
            if filename.endswith('.txt'):
                print(f"Processing {filename}...")  # Logging the start of processing
                with open(os.path.join(source_folder, filename), 'r') as file:
                    content = file.read()
                    summary = generate_summary(content)
                    save_summary_to_file(filename, summary)
                    move_file_to_processed(filename)
                print(f"End of processing {filename}.")  # Logging the end of processing
                files_processed_in_this_iteration += 1
        
        # If no files were processed in this cycle, we wait for a bit before checking again.
        if files_processed_in_this_iteration == 0:
            time.sleep(10)  # Sleep for 10 seconds. Adjust this value as needed.

if __name__ == '__main__':
    main()
