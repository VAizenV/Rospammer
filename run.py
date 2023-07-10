from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
from pystyle import *
import os
import ctypes
from colorama import Fore, Style
    

chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options)


def set_console_title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)
set_console_title("Roblox Code Spammer | Juz0")    
os.system('cls' if os.name == 'nt' else 'clear')
print('')
print('')
Write.Print("              /$$$$$                      /$$$$$$ \n", Colors.red_to_yellow)
Write.Print("             |__  $$                     /$$$_  $$\n", Colors.red_to_yellow)
Write.Print("                | $$ /$$   /$$ /$$$$$$$$| $$$$\ $$\n", Colors.red_to_yellow)
Write.Print("                | $$| $$  | $$|____ /$$/| $$ $$ $$\n", Colors.red_to_yellow)
Write.Print("           /$$  | $$| $$  | $$   /$$$$/ | $$\ $$$$\n", Colors.red_to_yellow)
Write.Print("          | $$  | $$| $$  | $$  /$$__/  | $$ \ $$$\n", Colors.red_to_yellow)
Write.Print("          |  $$$$$$/|  $$$$$$/ /$$$$$$$$|  $$$$$$/\n", Colors.red_to_yellow)
Write.Print("           \______/  \______/ |________/ \______/ \n", Colors.red_to_yellow)
print('')
Write.Print("> [Roblox code spammer]                           \n", Colors.red_to_yellow)
print('')
print('══════════════════════════════════════════════')
print('')  

driver.get("https://www.roblox.com/login")


wait = WebDriverWait(driver, 10)
button_cookie1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-cta-lg.cookie-btn.btn-primary-md.btn-min-width")))
button_cookie1.click()


username = input("Username : ")
password = input("Password : ")


username_input = wait.until(EC.visibility_of_element_located((By.ID, "login-username")))
username_input.send_keys(username)


password_input = wait.until(EC.visibility_of_element_located((By.ID, "login-password")))
password_input.send_keys(password)


login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button#login-button")))
login_button.click()


code_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#two-step-verification-code-input")))
verification_code = input("2FA Code : ")
code_input.send_keys(verification_code)
remember_device_checkbox = wait.until(EC.element_to_be_clickable((By.ID, "remember-device")))
remember_device_checkbox.click()
verify_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-cta-md.modal-modern-footer-button[aria-label='Vérifier']")))
verify_button.click()

button_cookie2 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-cta-lg.cookie-btn.btn-primary-md.btn-min-width")))
button_cookie2.click()


driver.get("https://www.roblox.com/redeem")
print(Fore.GREEN + "Logged as", username + Style.RESET_ALL)


code_input = wait.until(EC.visibility_of_element_located((By.ID, "code-input")))

print('')
print('══════════════════════════════════════════════')
print('')

while True:
    code = ''.join(random.choices('0123456789', k=12))

    code_input.clear()
    code_input.send_keys(code)

    redeem_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.redeem-btn.btn-primary-lg.btn-full-width")))

    redeem_button.click()

    print('Le code', code,'a été utilisé')