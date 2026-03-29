"""
Naukri.com Login & Resume Upload Automation Script using Playwright
Anti-bot stealth mode enabled - looks like a real user
"""

import os
import asyncio
import random
from playwright.async_api import async_playwright
from pathlib import Path
from dotenv import load_dotenv

async def setup_stealth(page):
    """Hide automation indicators from anti-bot detection"""
    await page.add_init_script("""
    Object.defineProperty(navigator, 'webdriver', {
        get: () => false,
    });
    
    window.chrome = {
        runtime: {}
    };
    
    Object.defineProperty(navigator, 'plugins', {
        get: () => [1, 2, 3, 4, 5],
    });
    
    Object.defineProperty(navigator, 'languages', {
        get: () => ['en-US', 'en'],
    });
    """)
    print("✓ Stealth mode enabled")

async def random_delay(min_ms=500, max_ms=2500):
    """Add human-like random delay"""
    delay = random.uniform(min_ms, max_ms) / 1000
    await asyncio.sleep(delay)

async def type_like_human(input_element, text, delay_ms=100):
    """Type text slowly like a human"""
    for char in text:
        await input_element.type(char)
        await asyncio.sleep(random.uniform(50, delay_ms) / 1000)

async def login_naukri(page, email, password):
    """Automate Naukri login with human-like behavior"""
    print("Navigating to Naukri login page...")
    await page.goto("https://www.naukri.com/nlogin/login", wait_until="domcontentloaded")
    
    await setup_stealth(page)
    await random_delay(1000, 2000)
    
    print("Entering email/username...")
    await page.wait_for_selector("#usernameField", timeout=10000)
    await random_delay(800, 1500)
    
    email_field = await page.query_selector("#usernameField")
    await email_field.click()
    await random_delay(300, 800)
    await type_like_human(email_field, email, delay_ms=80)
    
    await random_delay(500, 1500)
    
    print("Entering password...")
    password_field = await page.query_selector("#passwordField")
    await password_field.click()
    await random_delay(300, 700)
    await type_like_human(password_field, password, delay_ms=100)
    
    await random_delay(800, 1500)
    
    print("Clicking login button...")
    await page.click("button:has-text('Login')")
    
    print("Waiting for login to complete...")
    try:
        await page.wait_for_load_state("load", timeout=10000)
    except:
        print("⚠️ Load state timeout, but continuing...")
    
    await random_delay(2000, 4000)
    
    current_url = page.url
    print(f"Current URL: {current_url}")
    
    if "nlogin" not in current_url:
        print("✓ Login successful!")
        return True
    else:
        try:
            error_text = await page.inner_text("body")
            if any(word in error_text.lower() for word in ["invalid", "incorrect", "error"]):
                print("✗ Login error detected")
                return False
        except:
            pass
        print("✗ Login may have failed")
        return False

async def upload_resume(page, resume_path):
    """Navigate and upload resume with human-like behavior"""
    print("\n" + "="*50)
    print("Uploading Resume...")
    print("="*50)
    
    if not os.path.exists(resume_path):
        print(f"✗ Error: Resume file not found at {resume_path}")
        script_dir = os.path.dirname(os.path.abspath(resume_path))
        print(f"   Files in {script_dir}:")
        for f in os.listdir(script_dir):
            if f.lower().endswith(('.pdf', '.doc', '.docx')):
                print(f"     - {f}")
        return False
    
    print(f"✓ Resume file found: {os.path.abspath(resume_path)}")
    
    print("\nStep 1: Navigating to homepage...")
    try:
        await page.goto("https://www.naukri.com/mnjuser/homepage", wait_until="load", timeout=20000)
    except:
        print("⚠️ Homepage timeout, but continuing...")
    
    await random_delay(2000, 4000)
    print(f"✓ Homepage: {page.url}")
    
    print("\nStep 2: Navigating to profile page...")
    try:
        await page.goto("https://www.naukri.com/mnjuser/profile?id=&altresid", wait_until="load", timeout=20000)
    except:
        try:
            await page.goto("https://www.naukri.com/mnjuser/profile?id=&altresid", wait_until="domcontentloaded", timeout=20000)
        except:
            print("⚠️ Profile load timeout, but continuing...")
    
    print(f"✓ Profile page: {page.url}")
    await random_delay(3000, 5000)
    
    print("\nStep 3: Looking for Resume section...")
    
    for _ in range(3):
        await page.evaluate("window.scrollBy(0, 300)")
        await random_delay(500, 1000)
    
    try:
        print("Looking for 'Update resume' or 'Upload resume' button...")
        
        selectors = [
            "text='Update resume'",
            "text=/update resume/i",
            "text='Upload resume'",
            "text=/upload resume/i",
            "text='Update'",
            "text=/Update/i",
            "button:has-text('Update')",
            "button:has-text('Upload')",
            "a:has-text('Update resume')",
            "a:has-text('Upload resume')",
            "a:has-text('Update')",
        ]
        
        upload_btn = None
        for selector in selectors:
            try:
                count = await page.locator(selector).count()
                if count > 0:
                    print(f"✓ Found with selector: {selector}")
                    upload_btn = page.locator(selector).first
                    break
            except:
                continue
        
        if not upload_btn:
            print("✗ Could not find 'Update/Upload resume' button")
            print("Available text on page:")
            body_text = await page.inner_text("body")
            if "update" in body_text.lower():
                print("  - Found 'update' text on page")
            if "upload" in body_text.lower():
                print("  - Found 'upload' text on page")
            if "resume" in body_text.lower():
                print("  - Found 'resume' text on page")
            return False
        
        await upload_btn.scroll_into_view_if_needed()
        await random_delay(500, 1000)
        
        print("✓ Found button")
        print("Clicking button...")
        await random_delay(300, 800)
        
        # Try clicking multiple times if needed
        try:
            await upload_btn.click()
        except:
            print("  First click failed, trying force click...")
            await upload_btn.click(force=True)
        
        print("✓ Clicked button")
        
        # Wait longer for file input modal/dialog to appear
        await random_delay(2000, 3000)
        
    except Exception as e:
        print(f"✗ Error finding/clicking button: {str(e)}")
        import traceback
        traceback.print_exc()
        return False
    
    try:
        print(f"\nUploading file: {os.path.basename(resume_path)}")
        abs_path = os.path.abspath(resume_path)
        print(f"File path: {abs_path}")
        print(f"File exists: {os.path.exists(abs_path)}")
        
        # Wait a bit more for modal to fully render
        await random_delay(1500, 2500)
        
        # Try to find and use file input
        print("Looking for file input element...")
        
        # Try multiple wait strategies
        file_input = None
        try:
            await page.wait_for_selector('input[type="file"]', timeout=8000)
            print("✓ File input found after wait")
            file_input = page.locator('input[type="file"]').first
        except:
            print("⚠️ File input wait timeout, searching alternatives...")
            
            # Try to find any file input immediately
            all_file_inputs = page.locator('input[type="file"]')
            count = await all_file_inputs.count()
            print(f"  Found {count} file input(s) on page")
            
            if count > 0:
                file_input = all_file_inputs.first
            else:
                # Try to find by attribute
                print("  Trying alternative selectors...")
                alt_selectors = [
                    'input[accept*="pdf"]',
                    'input[accept*="document"]',
                    'input[accept*="application"]',
                    'input[accept*="msword"]',
                    'input[accept*="pdf"]',
                    'input[name*="resume"]',
                    'input[name*="file"]',
                    'input[name*="upload"]',
                    'input[id*="file"]',
                    'input[id*="upload"]',
                    'input[id*="resume"]'
                ]
                
                for alt_sel in alt_selectors:
                    count = await page.locator(alt_sel).count()
                    if count > 0:
                        print(f"  ✓ Found with selector: {alt_sel}")
                        file_input = page.locator(alt_sel).first
                        break
        
        if not file_input:
            print("✗ Could not find any file input on page")
            return False
        
        print("✓ File input found!")
        print(f"Uploading: {os.path.basename(resume_path)}")
        
        await random_delay(500, 1000)
        
        # Set the file
        try:
            await file_input.set_input_files(abs_path)
            print("✓ File uploaded!")
        except Exception as e:
            print(f"✗ Error uploading file: {e}")
            return False
        
        # Wait for upload to complete
        print("Waiting for upload to process...")
        await random_delay(5000, 8000)
        
        # Check for success
        try:
            page_text = await page.inner_text("body")
            if any(word in page_text.lower() for word in ["success", "uploaded", "updated", "confirmation", "saved"]):
                print("✓ Upload successful!")
                return True
        except:
            pass
        
        print("✓ File upload completed")
        return True
            
    except Exception as e:
        print(f"✗ Error during upload: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

async def main_automation(email, password, resume_path):
    """Main automation function"""
    
    async with async_playwright() as p:
        try:
            browser = await p.edge.launch(
                headless=False,
                args=[
                    "--disable-dev-shm-usage",
                    "--disable-extensions",
                    "--disable-sync",
                ]
            )
            print("Launching Microsoft Edge with stealth mode...")
        except:
            print("Launching Chromium with stealth mode...")
            browser = await p.chromium.launch(
                headless=False,
                args=[
                    "--disable-dev-shm-usage",
                    "--disable-extensions",
                    "--disable-sync",
                ]
            )
        
        try:
            context = await browser.new_context(
                viewport={"width": 1920, "height": 1080},
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            )
            page = await context.new_page()
            
            print("\n" + "="*50)
            print("STEP 1: LOGIN")
            print("="*50)
            login_success = await login_naukri(page, email, password)
            
            if not login_success:
                print("✗ Login failed. Exiting.")
                await context.close()
                await browser.close()
                return False
            
            await random_delay(3000, 5000)
            
            upload_success = await upload_resume(page, resume_path)
            
            print("\n" + "="*50)
            print("Process Complete!")
            print("="*50)
            print("Browser will close in 10 seconds...")
            await asyncio.sleep(10)
            
            await context.close()
            await browser.close()
            
            return upload_success
            
        except Exception as e:
            await browser.close()
            print(f"Error: {str(e)}")
            return False

def main():
    """Main function"""
    load_dotenv()
    
    email = os.getenv('NAUKRI_EMAIL', '')
    password = os.getenv('NAUKRI_PASSWORD', '')
    
    if not email or not password:
        print("\n✗ Error: Credentials not found!")
        print("Please set NAUKRI_EMAIL and NAUKRI_PASSWORD in .env file")
        return
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    resume_candidates = ['Resume.pdf', 'resume.pdf', 'RESUME.pdf']
    
    resume_path = None
    for filename in resume_candidates:
        candidate_path = os.path.join(script_dir, filename)
        if os.path.exists(candidate_path):
            resume_path = candidate_path
            print(f"✓ Found resume: {filename}")
            break
    
    if not resume_path:
        print("✗ Error: No resume file found!")
        print(f"  Looked in: {script_dir}")
        print(f"  Expected files: {', '.join(resume_candidates)}")
        return
    
    print("\n" + "="*60)
    print("NAUKRI AUTOMATION - LOGIN & RESUME UPLOAD")
    print("Anti-Bot Stealth Mode: ENABLED ✓")
    print("="*60)
    print(f"Email: {email}")
    print(f"Resume: {os.path.basename(resume_path)}")
    print("="*60 + "\n")
    
    asyncio.run(main_automation(email, password, resume_path))

if __name__ == "__main__":
    main()
