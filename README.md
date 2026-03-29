# Naukri Login Automation Script

## 🎯 What This Does

Automatically logs into Naukri, navigates to your profile, and uploads your resume.

With GitHub Actions, it runs **every 2 hours automatically** without needing your computer!

## ✨ Features

- ✅ **Anti-Bot Stealth Mode** - Looks like a real human
- ✅ **Automatic Scheduling** - Runs every 2 hours via GitHub Actions
- ✅ **Secure** - Credentials stored safely in GitHub Secrets
- ✅ **Error Handling** - Detailed error messages
- ✅ **No Manual Work** - Set it once, forget about it

## 📋 Quick Start

### Local Setup (5 minutes)

#### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 2. Set Environment Variables

**Windows (PowerShell):**
```powershell
$env:NAUKRI_EMAIL = "your-email@example.com"
$env:NAUKRI_PASSWORD = "your-password"
```

**Windows (CMD):**
```cmd
set NAUKRI_EMAIL=your-email@example.com
set NAUKRI_PASSWORD=your-password
```

**Linux/Mac:**
```bash
export NAUKRI_EMAIL="your-email@example.com"
export NAUKRI_PASSWORD="your-password"
```

#### 3. Run the Script
```bash
python naukri_login.py
```

### Using .env File (More Secure)

Create `.env` file in same folder as script:
```
NAUKRI_EMAIL=your-email@example.com
NAUKRI_PASSWORD=your-password
```

Then just run:
```bash
python naukri_login.py
```

## 🚀 GitHub Actions Setup (Automated Every 2 Hours)

For automatic scheduling every 2 hours without your computer running:

**👉 Follow the guide:** [QUICK-START.md](QUICK-START.md)

**Detailed guide:** [GITHUB-SETUP.md](GITHUB-SETUP.md)

## 📁 File Requirements

- `Resume.pdf` or `resume.pdf` in same folder as script
- Maximum size: 2 MB
- Supported formats: PDF, DOC, DOCX, RTF

## 🔒 Security

- ⚠️ **Never commit `.env` file** with real credentials to GitHub
- ✅ Use GitHub Secrets for production
- ✅ Keep repository Private
- ✅ Credentials are encrypted in GitHub

## 🛠️ File Structure

```
naukri-automation/
├── .github/
│   └── workflows/
│       └── naukri-automation.yml    # Runs every 2 hours
├── .env                              # Your credentials (local)
├── naukri_login.py                   # Main script
├── requirements.txt                  # Dependencies
├── README.md                         # This file
├── QUICK-START.md                    # 5-min GitHub setup
└── GITHUB-SETUP.md                   # Detailed guide
```

## ⏰ Automation Schedule

Runs automatically at (UTC):
- 00:00, 02:00, 04:00, 06:00, 08:00, 10:00, 12:00, 14:00, 16:00, 18:00, 20:00, 22:00

## 🐛 Troubleshooting

### Issue: "Resume file not found"
- Ensure `Resume.pdf` is in same folder as `naukri_login.py`
- Check file name spelling (case-sensitive on servers)

### Issue: "Login failed"
- Verify email and password are correct
- Try logging in manually first
- Check if Naukri has 2FA enabled (disable for automation)

### Issue: "GitHub Actions not running"
- Check if secrets are added correctly
- GitHub can be delayed up to 15 minutes
- Try manual run from Actions tab

## 📊 GitHub Actions Output

Successful run output:
```
✓ Stealth mode enabled
✓ Login successful!
✓ Found button
✓ Clicked button
✓ File uploaded!
✓ File upload completed
```

## 💡 Tips

- Resume gets priority boost on Naukri after each upload
- More frequent uploads = better visibility to recruiters
- Every 2 hours is a good balance
- Change schedule in `.github/workflows/naukri-automation.yml` if needed

## ⚖️ Disclaimer

- Use responsibly and check Naukri's Terms of Service
- This is for personal use only
- Not affiliated with Naukri.com
- Use at your own risk

## 🎓 Learn More

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Playwright Documentation](https://playwright.dev/python/)
- [Python-dotenv Documentation](https://python-dotenv.readthedocs.io/)

---

**Ready to get started?** → [QUICK-START.md](QUICK-START.md)
load_dotenv()
```

## ⚠️ Security Best Practices

- ✅ Never commit `.env` or credentials to version control
- ✅ Use environment variables or config files
- ✅ Add `.env` to `.gitignore`
- ✅ Consider using a password manager
- ❌ Never hardcode credentials in scripts

## Troubleshooting

- **"Element not found"**: Naukri website HTML may have changed. Check the element IDs
- **Login fails silently**: The website may require additional verification (OTP, CAPTCHA)
- **Headless mode issues**: Disable headless mode to see what's happening

## Note on Terms of Service

Check Naukri's ToS before automating. Some websites restrict automated access.
