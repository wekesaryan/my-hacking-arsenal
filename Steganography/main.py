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

def hide_binary_in_image(binary_data_path, image_path, output_path):
    with open(image_path, 'rb') as f:
        image_data = f.read()
    
    with open(binary_data_path, 'rb') as f:
        binary_data = f.read()
    
    # Append a delimiter and the binary data to the image
    stego_data = image_data + b'\x00\x00\x00\x00\x00\x00\x00\x00' + binary_data
    
    with open(output_path, 'wb') as f:
        f.write(stego_data)

def convert_to_binary(file_path):
    with open(file_path, 'rb') as f:
        binary_data = f.read()
    return binary_data

def save_binary_to_file(binary_data, output_path):
    with open(output_path, 'wb') as f:
        f.write(binary_data)

def execute_exe(file_path):
    # Execute the extracted exe file
    subprocess.run(file_path, shell=True)

if __name__ == "__main__":
    # Step 1: Choose an image and an exe file
    image_path = input("Enter the path to the image file: ")
    exe_path = input("Enter the path to the exe file: ")
    stego_image_path = "stego_image.png"
    extracted_exe_path = "extracted.exe"

    # Step 2: Convert the exe file to binary format
    binary_data = convert_to_binary(exe_path)

    # Step 3: Hide the binary code within the image
    hide_binary_in_image(exe_path, image_path, stego_image_path)
    print(f"Binary data hidden in image and saved as {stego_image_path}")

    # Step 4: Extract the exe file from the stego image
    extract_binary_from_image(stego_image_path, extracted_exe_path)
    print(f"Binary data extracted from image and saved as {extracted_exe_path}")

    # Step 5: Execute the extracted exe file
    execute_exe(extracted_exe_path)
