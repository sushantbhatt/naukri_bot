# Troubleshooting Guide

## Common Errors & Solutions

### ❌ Error: "credentials not found"

**Problem**: Script can't find your email/password

**Solutions**:
1. Check GitHub Secrets are added:
   - Go to Settings → Secrets and variables → Actions
   - Verify `NAUKRI_EMAIL` exists
   - Verify `NAUKRI_PASSWORD` exists
2. For local testing, ensure `.env` file exists with correct values
3. Restart the workflow

---

### ❌ Error: "Resume file not found"

**Problem**: Script can't find your Resume.pdf

**Solutions**:
1. Check resume file is in repository root (same level as `naukri_login.py`)
2. File must be named exactly: `Resume.pdf`, `resume.pdf`, or `RESUME.pdf`
3. File size must be under 2 MB
4. Upload file via GitHub:
   - Click "Add file" → "Upload files"
   - Upload your Resume.pdf
   - Commit changes

---

### ❌ Error: "Login failed" or "Login may have failed"

**Problem**: Script can't log into Naukri

**Solutions**:
1. Verify credentials are 100% correct:
   - Go to Settings → Secrets
   - Check email spelling
   - Check password has no typos
2. Try logging in manually to Naukri first
3. Check if Naukri asks for 2FA (disable it temporarily for automation)
4. Check if Naukri has captcha (requires manual update)
5. Wait a few hours and retry (Naukri might have blocked automated logins)

---

### ❌ Error: "Could not find 'Update resume' button"

**Problem**: Script can't locate the upload button

**Solutions**:
1. Naukri website might have changed - script may need updating
2. You might not be logged in successfully (check previous error)
3. Naukri might have updated their UI
4. Try running manually from GitHub Actions to see full error

---

### ❌ Error: "No file input element found on page"

**Problem**: Script can't find the file upload dialog

**Solutions**:
1. Browser might not have fully loaded
2. Dialog might not be appearing
3. Naukri UI might have changed
4. Try increasing wait times in the script

---

### ❌ Workflow shows "No jobs ran"

**Problem**: Scheduled workflow isn't running

**Solutions**:
1. This is normal - GitHub Actions can be delayed up to 15 minutes
2. Try manual trigger:
   - Go to "Actions" tab
   - Click the workflow
   - Click "Run workflow"
3. Check if workflow file has syntax errors:
   - Go to `.github/workflows/naukri-automation.yml`
   - Verify YAML syntax (indentation matters!)

---

### ❌ Error: "ModuleNotFoundError: No module named 'playwright'"

**Problem**: Dependencies not installed

**Solutions**:
This should not happen on GitHub Actions, but if testing locally:
```bash
pip install -r requirements.txt
playwright install chromium
```

---

### ❌ Error: "Error during upload: input is not attached to a frame"

**Problem**: File input dialog disappeared before upload

**Solutions**:
1. This is a timing issue
2. Script waits too long or too short
3. Check Naukri website loading speed
4. Try re-running the workflow

---

## Debugging Steps

### Check GitHub Actions Logs

1. Go to your repository
2. Click "Actions" tab
3. Click the failed workflow run
4. Click the "Run" job
5. Expand each section to see detailed logs
6. Look for error messages

### Common Log Examples

**Successful Run:**
```
✓ Stealth mode enabled
✓ Login successful!
✓ Found button
✓ Clicked button
✓ File uploaded!
✓ File upload completed
```

**Failed Login:**
```
Navigating to Naukri login page...
✓ Stealth mode enabled
Entering email/username...
Entering password...
Clicking login button...
Waiting for login to complete...
Current URL: https://www.naukri.com/nlogin/login
✗ Login may have failed
✗ Login failed. Exiting.
```

**Missing File:**
```
✗ Error: No resume file found!
  Looked in: /home/runner/work/naukri-automation/naukri-automation
  Expected files: Resume.pdf, resume.pdf, RESUME.pdf
```

---

## Test Steps

### Local Testing Before GitHub Upload

1. Open PowerShell in your naukri folder
2. Activate virtual environment: `.\.venv\Scripts\Activate.ps1`
3. Set environment variables:
   ```powershell
   $env:NAUKRI_EMAIL = "your-email@example.com"
   $env:NAUKRI_PASSWORD = "your-password"
   ```
4. Run script: `python naukri_login.py`
5. Watch browser and terminal for errors

### GitHub Actions Manual Test

1. Go to "Actions" tab
2. Click "Naukri Resume Upload - Every 2 Hours"
3. Click blue "Run workflow" button
4. Choose "main" branch
5. Click "Run workflow"
6. Check logs within 5 minutes

---

## Performance Issues

### Workflow takes too long (>5 minutes)

**Possible causes**:
- Naukri website is slow
- Too many delay pauses in script
- Playwright browsers taking time to launch

**Solutions**:
- This is normal, can be up to 5-10 minutes
- If >15 minutes, something is wrong

### Workflow times out

**Problem**: Workflow takes >6 hours (GitHub limit)

**Solution**:
- Won't happen for this script
- Each run is 2-5 minutes

---

## When to Restart

You should restart the workflow if:
- ❌ First run failed (restart once)
- ❌ Got login error (update credentials, restart)
- ❌ Got "file not found" (add file, restart)
- ✅ Already retried once and still failing? Check error messages carefully

---

## Getting Help

If you still have issues:

1. Check all error messages carefully
2. Follow the debugging steps above
3. Verify all setup steps were completed
4. Try manual run from GitHub UI
5. Check if Naukri website is accessible
6. Ensure credentials are 100% correct

---

## Tips for Success

✅ Test locally first before GitHub  
✅ Verify credentials are correct  
✅ Ensure resume file is named correctly  
✅ Check GitHub Secrets are added  
✅ Keep repo Private for security  
✅ Monitor first few runs  
✅ Check workflow logs regularly  

---

## Common Questions

**Q: How long should each run take?**  
A: 2-5 minutes normally

**Q: Can it fail sometimes?**  
A: Yes, if Naukri blocks it or website is down

**Q: Is this against Naukri's terms?**  
A: Check their ToS, but basic automation is usually allowed

**Q: Will my account get banned?**  
A: Unlikely, but use responsibly (every 2 hours is reasonable)

**Q: Can I disable it?**  
A: Yes, delete the workflow file or pause the schedule

**Q: Can I change the schedule?**  
A: Yes, edit `.github/workflows/naukri-automation.yml`

---

Still stuck? Check that all these are true:
- ✅ Repository created on GitHub
- ✅ All files uploaded (naukri_login.py, requirements.txt, .github folder, Resume.pdf)
- ✅ GitHub Secrets added (NAUKRI_EMAIL, NAUKRI_PASSWORD)
- ✅ Credentials are 100% correct
- ✅ Resume.pdf is in repository root
- ✅ File named exactly "Resume.pdf" (case-sensitive on servers)

If all checked, run manual test from Actions tab!
