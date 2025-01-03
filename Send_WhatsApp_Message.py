import pyautogui
import time
import subprocess

# Open WhatsApp Desktop (assuming it's installed)
subprocess.run(["start", "whatsapp:"], shell=True)

# Wait for WhatsApp to open
time.sleep(5)  # Adjust the sleep time based on your system's speed

# Define contacts and message
contacts = ["9665272525", "9924193117", "9909610943","9510977277","9167280108","9099270254"]  # Replace with actual contact names
message = "IPO : Parmeshwar Metal"

# Function to send message
def send_message(contact, message):
    # Use search bar to find the contact
    pyautogui.hotkey('ctrl', 'f')  # Open search bar
    time.sleep(2)

    pyautogui.write(contact)  # Type the contact name
    time.sleep(2)  # Wait for the contact to appear

    pyautogui.press('down')  # This ensures that the first contact is selected
    time.sleep(1)

    pyautogui.press('enter')  # Open the chat with the contact
    time.sleep(2)

    # Type the message
    pyautogui.write(message)
    pyautogui.press('enter')  # Send the message

# Loop through the contacts and send the message
for contact in contacts:
    send_message(contact, message)
    time.sleep(2)  # Delay before sending the next message
    
