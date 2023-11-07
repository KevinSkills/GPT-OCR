
OCR Utility Application
=======================

Overview
--------
This application provides an OCR (Optical Character Recognition) feature 
that allows users to capture text from images stored in the clipboard. It 
leverages the GPT-4 vision model for the OCR process.

Demonstration:
https://youtu.be/7b6P5XC0XP8

Prerequisites
-------------
Before using the application, ensure that you have Python installed on your 
system and the necessary libraries (pystray, PIL, keyboard, requests, pyperclip, 
and easygui) which can be installed using `pip`:

    pip install pystray pillow keyboard requests pyperclip easygui

Additionally, you must have an API key from OpenAI to use their OCR model. 
Set this key as an environment variable on your system.

Setting up the API Key
----------------------
1. Obtain an API key from OpenAI's platform.
2. Set the API key as an environment variable named `OPENAI_API_KEY`.

For Windows:
    setx OPENAI_API_KEY "Your-API-Key"

For macOS and Linux (I think it is like this, have not tested it):
    export OPENAI_API_KEY="Your-API-Key"

Remember to replace "Your-API-Key" with the actual API key provided by OpenAI.

Usage
-----
To run the application, simply navigate to the directory where the `GPT_OCR.pyw` 
file is located and double-click on the file.

This will start the application without opening a command-line window. Once started, 
the application will reside in the system tray. You can interact with it through the 
tray icon or by using the configured hotkey.

Hotkey
------
The default hotkey to trigger OCR is `Ctrl+Alt+O`. Press this combination anytime 
to perform OCR on the image currently in the clipboard. You can change this in the python script too


System Message
-----------
You can change the system message inside the python script. It was made fairly quickly so may be optimized.

System Tray
-----------
The application icon will appear in the system tray, and you can right-click it 
to access the menu options:

- `OCR`: Perform OCR on the clipboard image.
- `Exit`: Close the application.

Changing the Tray Icon
----------------------
I have used a default icon from the System32 folder. If you dont have this icon, the program wont work. To change the tray icon, replace the `ICON_PATH` in the script with the path to 
your new icon file. Ensure your icon file is in PNG format for the best compatibility.

Example:
    ICON_PATH = r"path\to\your\icon.png"

Error Handling
--------------
If the application throws an error related to the icon, ensure the `ICON_PATH` 
is correct and points to a valid PNG file. Also, check if the file is not corrupted 
and is accessible by the script.

Note
----
Remember to restart your system or the command line to apply the changes after 
setting up the environment variable for the API key. If the API key is updated or 
changed, you'll need to update the environment variable accordingly.
