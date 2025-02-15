# Image Steganography Tool

Overview

This project is a simple steganography tool built using Python and Tkinter. It allows users to hide and reveal messages within image files using Least Significant Bit (LSB) steganography. Additionally, users can set and update a password for message encryption and decryption.

Features

Open and display an image

Hide a secret message inside an image

Reveal the hidden message from an image

Save the modified image containing the hidden message

Set and update a password to protect the hidden message

Prerequisites

Ensure you have the following installed:

Python 3.x

Required Python libraries:

pip install pillow stegano tkinter

How to Use

1. Run the Application

Execute the following command in your terminal or command prompt:

python main.py

2. Open an Image

Click the Open Image button and select an image (PNG or JPG format) to load it into the application.

3. Hide a Message

Enter a secret message in the text box.

Provide the correct secret key (password) in the input field.

Click the Hide Data button to embed the message inside the selected image.

A success message will appear once the process is complete.

4. Save the Image

Click the Save Image button.

Choose a destination folder and filename to save the modified image containing the hidden message.

5. Reveal a Hidden Message

Open an image with a hidden message.

Enter the correct secret key (password).

Click the Show Data button to extract and display the hidden message.

6. Change Password

Enter a new password in the "Set New Password" field.

Click the Set Password button to update the password.

File Structure

├── main.py        # Main application file
├── password.txt   # Stores the user-defined password
├── README.md      # Detailed instructions

Password Management

The application stores the password in a password.txt file.

If the file does not exist, it creates one with a default password (1234).

Users can update the password through the UI.

Dependencies

This project uses the following Python libraries:

tkinter - For GUI components

PIL (Pillow) - For image processing

stegano.lsb - For encoding and decoding hidden messages in images

Notes

The tool works best with .png images as they support lossless compression.

Ensure the password is remembered; otherwise, the hidden message cannot be retrieved.

License

This project is free to use and modify.

Author

Ganesh Kanojiya (Zeref)MMM
