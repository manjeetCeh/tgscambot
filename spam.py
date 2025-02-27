import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Telegram Support URL
support_url = "https://telegram.org/support"

# ⚠️ Enter scammer's details manually
scammer_username = "scammer123"  # Change this to the actual scammer's username
scammer_channel = "https://t.me/scammerchannel"  # Change this to the actual channel link

# Scam Description Function
def generate_scam_description():
    return f"""
This user (@{scammer_username}) is running a **carding scam** and tricking people into sending money by promising illegal credit card details, bank logs, and other fraudulent services. Many victims have already been scammed.

He is using Telegram to promote his illegal activities and scam people under false promises. His Telegram channel is actively spreading fraudulent content and misleading users.

🚨 Scammer's Telegram Channel: {scammer_channel}

Please take immediate action and ban this user and his channel before more people fall victim.
"""

# Function to generate a random name
def generate_random_name():
    first_names = ["John", "Mike", "Alice", "Sarah", "David", "Emma", "Robert", "Olivia"]
    last_names = ["Smith", "Johnson", "Brown", "Taylor", "Anderson", "Thomas", "Harris"]
    return f"{random.choice(first_names)} {random.choice(last_names)}"

# Function to generate a random email
def generate_random_email():
    domains = ["gmail.com", "yahoo.com", "outlook.com", "protonmail.com"]
    email_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return f"{email_name}@{random.choice(domains)}"

# Function to generate a random phone number
def generate_random_phone():
    return f"+{random.randint(100, 999)}{random.randint(1000000000, 9999999999)}"

# Infinite Loop for Continuous Reporting
try:
    while True:
        # Generate new random values
        random_name = generate_random_name()
        random_email = generate_random_email()
        random_phone = generate_random_phone()
        scam_description = generate_scam_description()

        # Set up Selenium WebDriver
        driver = webdriver.Chrome()  # Ensure you have ChromeDriver installed
        driver.get(support_url)

        time.sleep(2)  # Let the page load

        try:
            # Step 1: Fill in the description
            desc_field = driver.find_element(By.NAME, "message")
            desc_field.send_keys(scam_description)

            # Step 2: Enter random full name
            name_field = driver.find_element(By.NAME, "name")
            name_field.send_keys(random_name)

            # Step 3: Enter random email address
            email_field = driver.find_element(By.NAME, "email")
            email_field.send_keys(random_email)

            # Step 4: Enter random phone number
            phone_field = driver.find_element(By.NAME, "phone")
            phone_field.send_keys(random_phone)

            # Step 5: Submit the form
            submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
            submit_button.click()

            print(f"✅ Report Submitted! \n👤 Name: {random_name}\n📧 Email: {random_email}\n📱 Phone: {random_phone}\n🚨 Reported Username: @{scammer_username}\n📢 Channel: {scammer_channel}")

        except Exception as e:
            print("❌ Error:", str(e))

        # Close the browser
        time.sleep(5)
        driver.quit()

        # Wait before next report (to avoid detection)
        time.sleep(10)  # Adjust this delay if needed

except KeyboardInterrupt:
    print("\n❌ Script Stopped by User!")
