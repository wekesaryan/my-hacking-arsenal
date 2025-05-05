import os


def hide_binary_in_image(binary_data_path, image_path, output_path):
    with open(image_path, 'rb') as f:
        image_data = f.read()

    with open(binary_data_path, 'rb') as f:
        binary_data = f.read()

    # Append a delimiter and the binary data to the image
    #This will be flagged by an AV/EDR
    stego_data = image_data + b'\x00\x00\x00\x00\x00\x00\x00\x00' + binary_data

    with open(output_path, 'wb') as f:
        f.write(stego_data)


def convert_to_binary(file_path):
    with open(file_path, 'rb') as f:
        binary_data = f.read()
    return binary_data


if __name__ == "__main__":
    # Step 1: Choose an image and an exe file
    image_path = input("Enter the path to the image file: ")
    exe_path = input("Enter the path to the exe file: ")
    stego_image_path = "stego_image.png"

    # Step 2: Convert the exe file to binary format
    binary_data = convert_to_binary(exe_path)

    # Step 3: Hide the binary code within the image
    hide_binary_in_image(exe_path, image_path, stego_image_path)
    print(f"Binary data hidden in image and saved as {stego_image_path}")
