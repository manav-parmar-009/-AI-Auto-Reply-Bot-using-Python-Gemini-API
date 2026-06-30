import pyautogui
import time
import pyperclip
from client import ask_gemini


def is_last_message_from_user(chat_history, user_name="Manav Parmar"):
    lines = [line.strip() for line in chat_history.splitlines() if line.strip()]
    if not lines:
        return False
    return user_name in lines[-1]



pyautogui.click(1259, 1041)
time.sleep(2)

while True:
    time.sleep(5)


    pyautogui.moveTo(732, 331)
    pyautogui.mouseDown()
    pyautogui.moveTo(918, 936, duration=1)
    pyautogui.mouseUp()
 
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)

    pyautogui.click(1580, 925)
    chat_history = pyperclip.paste()

    print("\nCHAT HISTORY:\n", chat_history)


    lines = [line.strip() for line in chat_history.splitlines() if line.strip()]
    if not lines:
        continue

    last_message = lines[-1]

    if "Manav Parmar:" in last_message:
        continue

    
    response = ask_gemini(
        chat_history +
        "\n\nReply naturally in Hinglish like a helpful AI assistant."
    )

    
    pyperclip.copy(response)

    pyautogui.click(1082, 975)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.press('enter')

    
    if "bye" in last_message.lower():
        break