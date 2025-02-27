import os
import time
import random
import string
import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# ✅ Step 1: Auto-install Chrome & ChromeDriver (For Codespaces/VPS)
def install_chrome():
    try:
        print("🚀 Installing Chrome & ChromeDriver...")
        os.system("sudo apt update && sudo apt install -y wget curl unzip")
        os.system("wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb")
        os.system("sudo dpkg -i google-chrome-stable_current_amd64.deb || sudo apt --fix-broken install -y")
        print("✅ Chrome Installed Successfully!")
    except Exception as e:
        print(f"❌ Error installing Chrome: {e}")

# ✅ Step 2: Auto-Update ChromeDriver (Fixes Version Mismatch)
def update_chromedriver():
    try:
        print("🚀 Updating ChromeDriver to match Chrome version...")
        os.system("sudo rm -rf /usr/local/bin/chromedriver")
        latest_driver = subprocess.getoutput("curl -sS https://googlechromelabs.github.io/chrome-for-testing/LATEST_RELEASE_STABLE").strip()
        os.system(f"wget -q https://storage.googleapis.com/chrome-for-testing-public/{latest_driver}/linux64/chromedriver-linux64.zip")
        os.system("unzip -o chromedriver-linux64.zip -d chromedriver-linux64/")
        os.system("sudo mv chromedriver-linux64/chromedriver /usr/local/bin/chromedriver")
        os.system("sudo chmod +x /usr/local/bin/chromedriver")
        print("✅ ChromeDriver Updated Successfully!")
    except Exception as e:
        print(f"❌ Error updating ChromeDriver: {e}")

# Install Chrome & ChromeDriver (Only if not on Windows)
if os.name != "nt":
    install_chrome()
    update_chromedriver()

# ✅ Step 3: Define Scammer Info & Telegram Support URL
scammer_username = "scammer123"  # Change to real scammer username
scammer_channel = "https://t.me/scammerchannel"  # Change to real scammer channel
telegram_support_url = "https://telegram.org/support"

# ✅ Step 4: Configure Chrome for Headless Mode (Fixes "DevToolsActivePort" & Other Issues)
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run without GUI
chrome_options.add_argument("--no-sandbox")  # Required for Codespaces
chrome_options.add_argument("--disable-dev-shm-usage")  # Fix memory issues
chrome_options.add_argument("--remote-debugging-port=9222")  # Debugging fix
chrome_options.add_argument("--disable-gpu")  # Fix GPU issues
chrome_options.add_argument("--disable-software-rasterizer")

# ✅ Step 5: Function to Generate Random Data
def generate_random_name():
    first_names = ["John", "Mike", "Alice", "Sarah", "David", "Emma", "Robert", "Olivia"]
    last_names = ["Smith", "Johnson", "Brown", "Taylor", "Anderson", "Thomas", "Harris"]
    return f"{random.choice(first_names)} {random.choice(last_names)}"

def generate_random_email():
    domains = ["gmail.com", "yahoo.com", "outlook.com", "protonmail.com"]
    email_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return f"{email_name}@{random.choice(domains)}"

def generate_random_phone():
    return f"+{random.randint(100, 999)}{random.randint(1000000000, 9999999999)}"

# ✅ Step 6: Loop for Continuous Reporting
try:
    while True:
        # Start WebDriver (Headless Mode)
        service = Service("/usr/local/bin/chromedriver")
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.get(telegram_support_url)

        time.sleep(2)  # Let the page load

        try:
            # Generate Random Details
            random_name = generate_random_name()
            random_email = generate_random_email()
            random_phone = generate_random_phone()
            scam_description = f"""
This user (@{scammer_username}) is running a **carding scam** and tricking people into sending money by promising illegal credit card details, bank logs, and other fraudulent services. Many victims have already been scammed.

He is using Telegram to promote his illegal activities and scam people under false promises. His Telegram channel is actively spreading fraudulent content and misleading users.

🚨 Scammer's Telegram Channel: {scammer_channel}

Please take immediate action and ban this user and his channel before more people fall victim.
            """

            print(f"👤 Name: {random_name}")
            print(f"📧 Email: {random_email}")
            print(f"📱 Phone: {random_phone}")
            print(f"🚨 Reporting: @{scammer_username}")

            # Fill Description
            driver.find_element(By.NAME, "message").send_keys(scam_description)
            # Fill Name
            driver.find_element(By.NAME, "name").send_keys(random_name)
            # Fill Email
            driver.find_element(By.NAME, "email").send_keys(random_email)
            # Fill Phone
            driver.find_element(By.NAME, "phone").send_keys(random_phone)
            # Click Submit
            driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

            print("✅ Report Submitted!")

        except Exception as e:
            print("❌ Error:", str(e))

        # Close the browser
        driver.quit()

        # Wait before next report (to avoid detection)
        time.sleep(10)  # Adjust delay if needed

except KeyboardInterrupt:
    print("\n❌ Script Stopped by User!")
