# 📡 Internet Speed Complaint Bot

**A Python automation bot** that checks your internet speed using **Speedtest.net**  
and automatically tweets a complaint to your **Internet Service Provider (ISP)**  
if the speed is below a promised threshold.

---

## 🚀 Features
- ✅ **Monitors download and upload speeds** using Speedtest
- 🐦 **Tweets a complaint** to your ISP on Twitter when speeds are below your expected plan
- 🤖 **Automates browser interaction** using Selenium WebDriver
- 🔐 **Handles login flows** for Twitter (email-first or username-first)
- 📄 **Uses XPath selectors** to interact with dynamic web elements

---

## 🛠 Tech Stack
- **Python**
- **Selenium WebDriver**

---

## 📦 Installation
```bash
git clone https://github.com/ritodevops2003/Internet-Speed-Complaint-Bot.git
cd Internet-Speed-Complaint-Bot
pip install -r requirements.txt


 ⚙️ Environment Variables
Create a .env file in the project root:
TWITTER_EMAIL=your_email
TWITTER_PASSWORD=your_password
SPEED_THRESHOLD_DOWNLOAD=your_download_speed
SPEED_THRESHOLD_UPLOAD=your_upload_speed

▶️ Usage
python main.py
