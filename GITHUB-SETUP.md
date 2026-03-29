# Naukri Resume Upload Automation with GitHub Actions

Automated script to upload your resume to Naukri.com every 2 hours using GitHub Actions.

## Features

✓ **Automated Resume Upload** - Every 2 hours automatically  
✓ **Anti-Bot Stealth Mode** - Looks like a real user  
✓ **Human-like Behavior** - Slow typing, random delays  
✓ **Error Handling** - Comprehensive error messages  
✓ **GitHub Actions** - No local machine needed  
✓ **Secure** - Credentials stored as GitHub secrets  

## Prerequisites

- GitHub Account (free)
- Naukri.com login credentials
- Resume file (PDF, DOC, or DOCX)

## Step-by-Step Setup

### Step 1: Create a GitHub Repository

1. Go to https://github.com/new
2. Create repository name: `naukri-automation`
3. Choose "Public" or "Private" (Private recommended for security)
4. Click "Create repository"

### Step 2: Clone and Upload Files to GitHub

#### Option A: Using Git (Recommended)

```bash
# Open PowerShell/Terminal in your naukri folder
cd c:\Users\sushant\Desktop\naukri

# Initialize git
git init
git add .
git commit -m "Initial commit: Naukri automation with GitHub Actions"

# Add your GitHub repository
git remote add origin https://github.com/YOUR_USERNAME/naukri-automation.git

# Push to GitHub
git branch -M main
git push -u origin main
```

#### Option B: Upload via GitHub Web Interface

1. Go to your repository: https://github.com/YOUR_USERNAME/naukri-automation
2. Click "Add file" → "Upload files"
3. Select these files:
   - `naukri_login.py`
   - `requirements.txt`
   - `.github/workflows/naukri-automation.yml`
   - `.gitignore`
   - `README.md`
4. Click "Commit changes"

### Step 3: Add GitHub Secrets (IMPORTANT!)

1. Go to your repository on GitHub
2. Click "Settings" → "Secrets and variables" → "Actions"
3. Click "New repository secret"
4. Add two secrets:

**Secret 1:**
- Name: `NAUKRI_EMAIL`
- Value: your-email@example.com
- Click "Add secret"

**Secret 2:**
- Name: `NAUKRI_PASSWORD`
- Value: your-password
- Click "Add secret"

**Screenshot Guide for Secrets:**
```
Settings → Secrets and variables → Actions → New repository secret
┌─────────────────────────────┐
│ Name: NAUKRI_EMAIL          │
│ Value: bhattsushant4@...    │
│ [Add secret button]         │
└─────────────────────────────┘
```

### Step 4: Verify Workflow Setup

1. Go to "Actions" tab on GitHub
2. You should see "Naukri Resume Upload - Every 2 Hours"
3. Click on it to verify

### Step 5: First Manual Test Run

1. Go to "Actions" tab
2. Click "Naukri Resume Upload - Every 2 Hours"
3. Click "Run workflow" → "Run workflow"
4. Wait for the job to complete (should take 2-5 mins)
5. Check the logs to see output

## Schedule Explanation

The workflow runs automatically at:
- **00:00 UTC** (8:00 AM IST)
- **02:00 UTC** (10:00 AM IST)
- **04:00 UTC** (12:00 PM IST)
- **06:00 UTC** (2:00 PM IST)
- **08:00 UTC** (4:00 PM IST)
- **10:00 UTC** (6:00 PM IST)
- **12:00 UTC** (8:00 PM IST)
- **14:00 UTC** (10:00 PM IST)
- **16:00 UTC** (12:00 AM IST)
- **18:00 UTC** (2:00 AM IST)
- **20:00 UTC** (4:00 AM IST)
- **22:00 UTC** (6:00 AM IST)

### Customize Schedule (Optional)

To change the schedule, edit `.github/workflows/naukri-automation.yml`:

```yaml
on:
  schedule:
    - cron: '0 */3 * * *'  # Run every 3 hours instead
```

Common cron patterns:
- Every hour: `0 * * * *`
- Every 2 hours: `0 */2 * * *`
- Every 6 hours: `0 */6 * * *`
- Every day at 9 AM: `0 9 * * *`

## File Structure

```
naukri-automation/
├── .github/
│   └── workflows/
│       └── naukri-automation.yml    # GitHub Actions workflow
├── .gitignore                        # Files to ignore
├── .env                              # Your credentials (local only)
├── naukri_login.py                   # Main automation script
├── requirements.txt                  # Python dependencies
└── README.md                         # This file
```

## Local Testing (Optional)

Before committing to GitHub, test locally:

```bash
# Navigate to project folder
cd c:\Users\sushant\Desktop\naukri

# Activate virtual environment
.\.venv\Scripts\Activate.ps1

# Run the script
python naukri_login.py
```

## Troubleshooting

### Issue: GitHub Actions not running at scheduled time

- **Solution**: GitHub Actions can have delays of up to 15 minutes. This is normal.

### Issue: Workflow shows "Failed"

1. Go to "Actions" tab
2. Click the failed workflow
3. Click "Run" job
4. Check the logs for error messages
5. Common errors:
   - Wrong credentials in secrets
   - Resume file not found
   - Naukri website structure changed

### Issue: "No resume file found"

- Ensure `Resume.pdf` is in the repository root
- Check file naming (case-sensitive)

### Issue: "Login failed"

- Verify credentials in GitHub Secrets are correct
- Check no special characters in password
- Try logging in manually to Naukri first

## Important Notes

⚠️ **Security:**
- Never commit `.env` file with real credentials
- Use GitHub Secrets for storing sensitive data
- Repository should be Private if possible

⚠️ **Limitations:**
- GitHub Actions has limited free runtime (2,000 minutes/month)
- Each job should complete in 2-3 minutes
- Enough for ~600 runs per month

⚠️ **Terms of Service:**
- Make sure you're not violating Naukri's Terms of Service
- Use responsibly

## GitHub Actions Output Example

```
NAUKRI AUTOMATION - LOGIN & RESUME UPLOAD
Anti-Bot Stealth Mode: ENABLED ✓
============================================================
Email: bhattsushant4@gmail.com
Resume: Resume.pdf
============================================================

==================================================
STEP 1: LOGIN
==================================================
Navigating to Naukri login page...
✓ Stealth mode enabled
Entering email/username...
Entering password...
Clicking login button...
Waiting for login to complete...
Current URL: https://www.naukri.com/mnjuser/homepage
✓ Login successful!

Step 1: Navigating to homepage...
✓ Homepage: https://www.naukri.com/mnjuser/homepage

Step 2: Navigating to profile page...
✓ Profile page: https://www.naukri.com/mnjuser/profile?id=&altresid

Step 3: Looking for Resume section...
Looking for 'Update resume' or 'Upload resume' button...
✓ Found with selector: text=/Update/i
✓ Found button
Clicking button...
✓ Clicked button

Uploading file: Resume.pdf
File path: /home/runner/work/naukri-automation/naukri-automation/Resume.pdf
File exists: True
Looking for file input element...
✓ File input found after wait
✓ File uploaded!
Waiting for upload to process...
✓ File upload completed

==================================================
Process Complete!
==================================================
Browser will close in 10 seconds...
```

## What Happens Each Run

1. **Login** - Uses credentials from GitHub Secrets
2. **Navigate** - Goes to Naukri profile page
3. **Find Button** - Locates Update/Upload resume button
4. **Upload** - Uploads your resume from repository
5. **Verify** - Checks if upload was successful
6. **Done** - Browser closes automatically

## Maintenance

### Update Resume File

1. Go to your repository
2. Click "Resume.pdf"
3. Click edit (pencil icon) or delete and re-upload
4. Next scheduled run will use new file

### Disable Automation (Temporarily)

Go to `.github/workflows/naukri-automation.yml` and comment out the schedule:

```yaml
on:
  # schedule:
  #   - cron: '0 */2 * * *'
  workflow_dispatch:
```

## Support

If you encounter issues:

1. Check GitHub Actions logs (Actions tab → Workflow → Latest run)
2. Try manual test run from GitHub UI
3. Verify credentials are correct
4. Check Naukri website is accessible
5. Ensure Resume.pdf is in repository

## License

MIT License - Feel free to modify and use

---

**Created**: March 2026  
**Last Updated**: March 2026
