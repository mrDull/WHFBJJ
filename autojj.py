import customtkinter as ctk
import inflect
import pyautogui as pg
import pydirectinput as pd
import time
from CTkMessagebox import CTkMessagebox
from pynput.keyboard import Listener, Key
import threading
import webbrowser  # To open the URL when clicked

# Initialize inflect engine
p = inflect.engine()

# Global flag for stopping the script
should_stop = False

# Create UI
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.geometry("400x605")
app.title("Roblox JJ Automator by dreamsrotting")

# --- Widgets ---
label_title = ctk.CTkLabel(app, text="USME JJ Script <3", font=("Arial", 22))
label_title.pack(pady=10)

entry_num = ctk.CTkEntry(app, placeholder_text="How many JJs?", width=200)
entry_num.pack(pady=10)

mode_dropdown = ctk.CTkOptionMenu(app, values=["Regular JJs", "Hell JJs", "Grammar JJs"])
mode_dropdown.set("Regular JJs")
mode_dropdown.pack(pady=10)



entry_custom = ctk.CTkEntry(app, placeholder_text="Hell JJs prefix", width=200)
entry_custom.pack(pady=10)

# Option checkboxes
exclam_var = ctk.BooleanVar()
exclam_check = ctk.CTkCheckBox(app, text="Add exclamation (!)", variable=exclam_var)
exclam_check.pack(pady=(5, 2))

# Spacer
spacer = ctk.CTkLabel(app, text="")
spacer.pack(pady=(0, 2))

case_var = ctk.BooleanVar()
case_check = ctk.CTkCheckBox(app, text="Use lowercase", variable=case_var)
case_check.pack(pady=(2, 5))

# Spacer
spacer = ctk.CTkLabel(app, text="")
spacer.pack(pady=(0, 2))



# Label 
delay_value_label = ctk.CTkLabel(app, text="1.0s") # start value
delay_value_label.pack()

ctk.CTkLabel(app, text="delay per msg (sec)").pack()

def update_label(value):
	delay_value_label.configure(text=f"{float(value):.1f}s")

# Delay slider
delay_slider = ctk.CTkSlider(app, from_=0.1, to=5, number_of_steps=40, width=200, command=update_label)
delay_slider.set(1)
delay_slider.pack(pady=10)
ctk.CTkLabel(app, text="Delay per message (seconds)").pack()





# --- Script ---
def start_script():
    global should_stop
    should_stop = False  # Reset the stop flag before starting

    try:
        # Validate input for number of jacks
        count = entry_num.get()
        if not count.isdigit() or int(count) <= 0:
            CTkMessagebox(title="Invalid Input", message="Please enter a valid number greater than 0.", icon="cancel")
            return
        
        count = int(count)
        
        mode = mode_dropdown.get()
        prefix = entry_custom.get().strip()
        use_lower = case_var.get()
        use_exclam = exclam_var.get()
        delay = delay_slider.get()

       

        for i in range(1, count + 1):
            if should_stop:
                print("Script stopped.")
                return  # Stop the script if the flag is set

            word = p.number_to_words(i)

            # Convert case
            word = word.lower() if use_lower else word.upper()

            # Add exclamation if selected
            if use_exclam:
                word += "!"

            if mode == "Regular JJs":
                time.sleep(delay)
                pd.press('/')
                pg.typewrite(word)
                pd.press('enter')
                pd.press('space')

            elif mode == "Hell JJs":
                # Remove non-alphabetic characters
                cleaned_word = ''.join(c for c in word if c.isalpha())
                for letter in cleaned_word:
                    if should_stop:
                        print("Script stopped.")
                        return  # Stop the script if the flag is set

                    msg = f"{prefix} {letter}" if prefix else letter
                    time.sleep(delay)
                    pd.press('/')
                    pg.typewrite(msg)
                    pd.press('enter')
                    pd.press('space')
                    
                if should_stop:
                    print("script stopped")
                    return
                
                full_word_msg = f"{prefix} {cleaned_word}" if prefix else cleaned_word
                time.sleep(delay)
                pd.press('/')
                pg.typewrite(full_word_msg)
                pd.press('enter')
                pd.press('space')
            
            elif mode == "Grammar JJs":
                word = p.number_to_words(i)  # like "one"
                word = word.lower().capitalize() + "."  # "One."

                msg = f"{prefix}{word}" if prefix else word
                time.sleep(delay)
                pd.press('/')
                pg.typewrite(msg)
                pd.press('enter')
                pd.press('space')
        

        CTkMessagebox(title="Done", message="JJ script finished!", icon="check")

    except Exception as e:
        CTkMessagebox(title="Error", message=f"Something went wrong:\n{e}", icon="cancel")

# Start Button
def handle_start():
    msgbox = CTkMessagebox(
        title="Ready?",
        message="Switch to Roblox and click Begin.",
        icon="info",
        option_1="Begin",
        option_2="Cancel"
    )
    if msgbox.get() == "Begin":
        threading.Thread(target=start_script).start()

start_btn = ctk.CTkButton(app, text="Start", command=handle_start)
start_btn.pack(pady=30)

# --- Keybinding Logic ---
def on_press(key):
    global should_stop
    try:
        if key == Key.f5:  # Start the script when 'J' is pressed
            print("Starting script...")
            handle_start() # Start the script in a new thread

        elif key == Key.f6:  # Stop the script when 'N' is pressed
            should_stop = True  # Set the stop flag
            print("Stopping script...")
											 CTkMessagebox(title="Done", message="JJ script cut short!", icon="check")
    except AttributeError:
        pass  # Handle special keys like shift, etc.

# Start listening for key events in a non-blocking way
listener = Listener(on_press=on_press)
listener.start()

# --- URL Label ---
def open_url(event):
	print("not using:3")   

url_label = ctk.CTkLabel(app, text="for we hate fat bitches", font=("Arial", 23, "underline"), fg_color="transparent")
url_label.pack(pady=20)

url_label2 = ctk.CTkLabel(app, text="made w/ love by dreamsrotting", font=("Arial", 10, "underline"), fg_color="transparent")
url_label2.pack(pady=1)


app.mainloop()
