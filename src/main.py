import threading
import customtkinter as tk
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


def main():

    tk.set_appearance_mode("dark")
    tk.set_default_color_theme("green")

    root = tk.CTk()
    root.geometry("500x350")

    frame = tk.CTkFrame(root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)

    label = tk.CTkLabel(frame, text="NTU Course Bot", font=("Arial", 24))
    label.pack(pady=10, padx=10)

    username = tk.CTkEntry(frame, placeholder_text="Username", fg_color="white", text_color="black")
    username.pack(pady=10, padx=10)

    password = tk.CTkEntry(frame, placeholder_text="Password", fg_color="white", text_color="black")
    password.pack(pady=10, padx=10)

    time = tk.CTkEntry(frame, placeholder_text="24HR Time (HH:MM:SS)", width=250, fg_color="white", text_color="black")
    time.pack(pady=10, padx=10)

    student_type = tk.CTkComboBox(
        frame,
        values=["STUDENT", "NIESTUDENT"],
        state="readonly",
        fg_color="white",
        text_color="black",
    )

    student_type.set("STUDENT")
    student_type.pack(pady=10, padx=10)

    button = tk.CTkButton(
        frame,
        text="Start",
        command=lambda: load_program(
            username.get(), password.get(), student_type.get(), time.get()
        )
        if username.get() != "" and password.get() != "" and time.get() != ""
        else None,
    )
    button.pack(pady=10, padx=10)

    root.mainloop()


def load_program(username, password, student_type, time):
    driver = webdriver.Firefox()
    driver.get(
        "https://wish.wis.ntu.edu.sg/pls/webexe/ldap_login.login?w_url=https://wish.wis.ntu.edu.sg/pls/webexe/aus_stars_planner.main"
    )
    # Set for all webpages
    driver.implicitly_wait(5)

    username_input = driver.find_element(By.ID, "UID")
    username_input.send_keys(f"{username}")

    select = Select(driver.find_element(By.ID, "DOMAIN"))
    select.select_by_value(f"{student_type}")

    username_input.send_keys(Keys.ENTER)

    pwd_input = driver.find_element(By.ID, "PW")
    pwd_input.send_keys(f"{password}")
    pwd_input.send_keys(Keys.ENTER)

    add_course = driver.find_element(
        By.XPATH, '//input[@value="Add (Register) Selected Course(s)"]'
    )
    now = datetime.now()
    delay = (
        datetime.strptime(
            f"{now.year}-{now.month}-{now.day} {time}", "%Y-%m-%d %H:%M:%S"
        )
        - datetime.now()
    ).total_seconds()
    threading.Timer(delay, lambda: add_course.click()).start()


if __name__ == "__main__":
    main()
