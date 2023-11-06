import os
import base64
import requests
from io import BytesIO
from PIL import ImageGrab, Image
import pyperclip
import pystray
import keyboard
import easygui

# Retrieve OpenAI API Key from environment variables
API_KEY = os.getenv("OPENAI_API_KEY")

# Constants
OCR_HOTKEY = 'ctrl+alt+o'
ICON_PATH = r"C:\Windows\System32\DefaultAccountTile.png"
SYSTEM_MESSAGE = r"You are an OCR machine. Your job is to output the text/code only. If it is math, the output should be in ASCIIMath (not latex) format like this: a^2 + 5 = 2*sqrt(5). Never describe what you see, just output the text."


def show_popup(message, title):
    easygui.msgbox(message, title)

def encode_image_from_clipboard():
    image = ImageGrab.grabclipboard()
    if image:
        buffered = BytesIO()
        image.save(buffered, format="PNG")
        return base64.b64encode(buffered.getvalue()).decode('utf-8')
    else:
        print("No image in clipboard!")
        return None



def ocr():
    base64_image = encode_image_from_clipboard()
    if not base64_image:
        print("No clipboard image found.")
        return

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    payload = {
        "model": "gpt-4-vision-preview", 
        "messages": [
            {"role": "system", "content": f"{SYSTEM_MESSAGE}" },
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Please OCR this image for me"},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
                ]
            }
        ],
        "max_tokens": 300
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    if response.status_code == 200:
        response_message = response.json()['choices'][0]['message']['content']
        print(response_message)
        pyperclip.copy(response_message)
        show_popup(response_message, "OCR Result - (Copied to clipboard)")
    else:
        error_message = f"Failed to get a successful response. Status Code: {response.status_code}, Response Text: {response.text}"
        print(error_message)
        show_popup(error_message, "OCR Error")
    


def exit_tray(icon, item):
    show_popup("Exiting the application.", "Exiting")
    icon.stop()


def ocr_tray(icon, item):
    ocr()


def setup_tray_icon():
    image = Image.open(ICON_PATH)
    icon = pystray.Icon("OCR Application", image, menu=pystray.Menu(
        pystray.MenuItem("OCR", ocr_tray),
        pystray.MenuItem("Exit", exit_tray)
    ))
    icon.run()


def main():
    keyboard.add_hotkey(OCR_HOTKEY, ocr)
    setup_tray_icon()


if __name__ == "__main__":
    main()
