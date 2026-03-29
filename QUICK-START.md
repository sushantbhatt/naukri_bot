# QUICK GITHUB SETUP GUIDE - Follow These Steps

## 🚀 Quick Start (5 Minutes)

### Step 1: Create GitHub Account (if you don't have one)
- Go to https://github.com/signup
- Sign up with email

### Step 2: Create New Repository
- Go to https://github.com/new
- Repository name: `naukri-automation`
- Description: "Automated Naukri resume upload"
- Choose "Private" (recommended for security)
- Click "Create repository"

### Step 3: Upload Your Files to GitHub

**Using Command Line (Easy):**

Open PowerShell in your naukri folder and run:

```powershell
# Go to your project folder
cd c:\Users\sushant\Desktop\naukri

# Initialize git
git init

# Add all files
git add .

# Create first commit
git commit -m "Initial commit"

# Connect to your GitHub repository
git remote add origin https://github.com/YOUR_USERNAME/naukri-automation.git

# Upload everything
git branch -M main
git push -u origin main
```

💡 **Replace `YOUR_USERNAME` with your actual GitHub username**

### Step 4: Add Your Credentials (IMPORTANT!)

Go to: https://github.com/YOUR_USERNAME/naukri-automation

1. Click "Settings" (top menu)
2. Click "Secrets and variables" on left
3. Click "Actions" 
4. Click green "New repository secret" button
5. Add FIRST secret:
   - Name: `NAUKRI_EMAIL`
   - Value: your-email@example.com
   - Click "Add secret"

6. Repeat for SECOND secret:
   - Name: `NAUKRI_PASSWORD`
   - Value: your-password
   - Click "Add secret"

✅ **Credentials are now secure and hidden!**

### Step 5: Test the Automation

1. Go to "Actions" tab (top menu of your repo)
2. Click "Naukri Resume Upload - Every 2 Hours"
3. Click blue "Run workflow" button
4. Choose "main" branch
5. Click "Run workflow"
6. Wait 2-5 minutes and watch it run!

### Step 6: Verify It Works

1. Go back to Actions tab
2. Click the workflow run
3. Click "Run" job
4. Scroll down and read the output
5. You should see ✓ marks indicating success

---

## ✅ Your automation is now ACTIVE!

**It will automatically run every 2 hours!**

Running schedule (UTC):
- 00:00, 02:00, 04:00, 06:00, 08:00, 10:00, 12:00, 14:00, 16:00, 18:00, 20:00, 22:00

---

## ⚠️ Important Reminders

- **Never share your repo URL publicly** if it's public (resume inside!)
- **Keep repo PRIVATE** for security
- Your credentials are encrypted in GitHub
- Free GitHub has 2000 minutes/month (plenty for this)

---

## 🔧 Troubleshooting

### If it doesn't run:
1. Check if credentials are correct in Settings → Secrets
2. Check if Resume.pdf file is in the repository
3. Try manual run from Actions tab

### If you see errors:
1. Go to Actions tab
2. Click the failed run
3. Click "Run" job
4. Read the error message
5. Fix the issue (usually missing credentials)

---

## 📝 File Checklist

Make sure these files are in your GitHub repository:
- ✅ naukri_login.py
- ✅ requirements.txt
- ✅ .github/workflows/naukri-automation.yml
- ✅ Resume.pdf (or resume.pdf)
- ✅ .gitignore
- ✅ .env (local only - NOT on GitHub)

---

## 🎉 That's it!

Your resume will now upload automatically every 2 hours!

Any questions? Check GITHUB-SETUP.md for detailed instructions.
