Steps
Attacker Machine(Preparation)
1. Choose an image and an exe file
2. Convert the exe file to binary format
3. Hide the binary code within the image


Deployment(Delivery)
1. sends the stego image to the victim using social engineering techniques.
- Via email, messaging apps, or other means

Victim Machine(Execution)
The attacker needs to find a way to autorun the script or trick the victim into running the script on their machine.
1. Extract the exe file from the stego image
2. Convert the extracted binary code back to the exe file
3. Execute the extracted exe file

Impact
- Stealing data, 
- Installing malware
- Creating backdoors.

NOTE: The script must be executed in an environment where Python is installed, and the victim has sufficient permissions to execute .exe files.

Mitigation
1. Avoid runnnig unknown scripts
2. Inspect code on any script before executing it.
3. Use antivirus software
4. Educate users to recognize and avoidsocial engineering attacks.

Ethical Considerations
- Steganography can be used for legitimate purposes (e.g., securely hiding files) or malicious purposes. 
