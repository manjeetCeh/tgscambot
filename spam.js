const { Builder, By } = require("selenium-webdriver");
const faker = require("faker");
const { execSync } = require("child_process");
const os = require("os");

// 🔥 Step 1: Auto-install Chrome & ChromeDriver (For Codespaces/VPS)
function installChrome() {
    try {
        console.log("🚀 Checking & Installing Chrome + ChromeDriver...");
        execSync("sudo apt update && sudo apt install -y wget curl unzip", { stdio: "inherit" });
        execSync("wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb", { stdio: "inherit" });
        execSync("sudo dpkg -i google-chrome-stable_current_amd64.deb || sudo apt --fix-broken install -y", { stdio: "inherit" });
        execSync("wget https://chromedriver.storage.googleapis.com/$(curl -sS https://chromedriver.storage.googleapis.com/LATEST_RELEASE)/chromedriver_linux64.zip", { stdio: "inherit" });
        execSync("unzip chromedriver_linux64.zip", { stdio: "inherit" });
        execSync("sudo mv chromedriver /usr/local/bin/", { stdio: "inherit" });
        execSync("sudo chmod +x /usr/local/bin/chromedriver", { stdio: "inherit" });
        console.log("✅ Chrome & ChromeDriver Installed Successfully!");
    } catch (err) {
        console.error("❌ Error installing Chrome/ChromeDriver:", err);
    }
}

// Install Chrome if missing (For Codespaces/VPS)
if (os.platform() !== "win32") {
    installChrome();
}

// 🔥 Step 2: Define Scammer Info & Telegram Support URL
const scammerUsername = "scammer123";  // Change to real scammer username
const scammerChannel = "https://t.me/scammerchannel";  // Change to real scammer channel
const telegramSupportURL = "https://telegram.org/support";

// 🔄 Step 3: Infinite Loop for Continuous Reporting
(async function spamReportLoop() {
    try {
        while (true) {
            let driver = await new Builder().forBrowser("chrome").build();

            try {
                console.log("🚀 Opening Telegram Support Page...");
                await driver.get(telegramSupportURL);

                // Generate Random Details
                let randomName = faker.name.findName();
                let randomEmail = faker.internet.email();
                let randomPhone = `+${faker.random.number({ min: 100, max: 999 })}${faker.random.number({ min: 1000000000, max: 9999999999 })}`;
                let scamDescription = `
This user (@${scammerUsername}) is running a **carding scam** and tricking people into sending money by promising illegal credit card details, bank logs, and other fraudulent services. Many victims have already been scammed.

He is using Telegram to promote his illegal activities and scam people under false promises. His Telegram channel is actively spreading fraudulent content and misleading users.

🚨 Scammer's Telegram Channel: ${scammerChannel}

Please take immediate action and ban this user and his channel before more people fall victim.
                `;

                console.log(`👤 Name: ${randomName}`);
                console.log(`📧 Email: ${randomEmail}`);
                console.log(`📱 Phone: ${randomPhone}`);
                console.log(`🚨 Reporting: @${scammerUsername}`);

                // Fill Description
                await driver.findElement(By.name("message")).sendKeys(scamDescription);
                // Fill Name
                await driver.findElement(By.name("name")).sendKeys(randomName);
                // Fill Email
                await driver.findElement(By.name("email")).sendKeys(randomEmail);
                // Fill Phone
                await driver.findElement(By.name("phone")).sendKeys(randomPhone);
                // Click Submit
                await driver.findElement(By.css("button[type='submit']")).click();

                console.log("✅ Report Submitted!");

            } catch (err) {
                console.error("❌ Error:", err);
            }

            // Close the browser
            await driver.quit();

            // Wait before next report (to avoid detection)
            await new Promise(resolve => setTimeout(resolve, 10000)); // 10 seconds delay
        }
    } catch (err) {
        console.error("❌ Fatal Error:", err);
    }
})();
