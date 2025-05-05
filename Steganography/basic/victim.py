import os
import subprocess

def extract_binary_from_image(stego_image_path, output_binary_path):
    with open(stego_image_path, 'rb') as f:
        stego_image_data = f.read()
    
    # Extract the binary data from the end of the image
    binary_data_start = stego_image_data.rfind(b'\x00\x00\x00\x00\x00\x00\x00\x00') + 8
    binary_data = stego_image_data[binary_data_start:]
    
    # Write the extracted binary data to a file
    with open(output_binary_path, 'wb') as f:
        f.write(binary_data)

def execute_exe(file_path):
    # Execute the extracted exe file
    subprocess.run(file_path, shell=True)

if __name__ == "__main__":
    # Step 1: Provide the stego image path
    stego_image_path = input("Enter the path to the stego image file: ")
    extracted_exe_path = "extracted.exe"

    # Step 2: Extract the exe file from the stego image
    extract_binary_from_image(stego_image_path, extracted_exe_path)
    print(f"Binary data extracted from image and saved as {extracted_exe_path}")

    # Step 3: Execute the extracted exe file
    execute_exe(extracted_exe_path)
