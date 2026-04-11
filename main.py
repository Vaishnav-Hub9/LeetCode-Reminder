import logging
import sys
import os
from dotenv import load_dotenv
from leetcode_api import has_submitted_today
from email_service import send_reminder

# Setup simple logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

def check_user_status(username: str, email: str):
    """
    Core logic to check if a user has submitted today and send an email if not.
    Wrapped in a try-except block to prevent the workflow from crashing ungracefully.
    """
    logging.info(f"Checking LeetCode status for user: {username} (Target Email: {email})")
    
    try:
        submitted_today = has_submitted_today(username)
        
        if submitted_today:
            logging.info(f"[{username}] PASS: User has already submitted a problem today. Excellent!")
        else:
            logging.warning(f"[{username}] FAIL: User HAS NOT submitted a problem today. Sending reminder...")
            
            # Send actual email
            success = send_reminder(email)
            
            if not success:
                # Fallback to mock print if email isn't configured properly
                print("\n" + "="*50)
                print(f"MOCK EMAIL (Config Missing) TO: {email}")
                print("SUBJECT: LeetCode Daily Accountability Reminder")
                print("BODY:")
                print("You haven't solved a LeetCode problem today. Stop being lazy and get it done.")
                print("="*50 + "\n")
                
    except Exception as e:
        logging.error(f"❌ Error during status check or email dispatch for {username}: {str(e)}")
        # We catch the exception here so the script can finish logging rather than exploding.

if __name__ == "__main__":
    try:
        # Load environment variables (from .env locally, or GitHub Secrets in the cloud)
        load_dotenv()
        
        LEETCODE_USERNAME = os.environ.get("LEETCODE_USERNAME")
        TARGET_EMAIL = os.environ.get("TARGET_EMAIL")
        
        if not LEETCODE_USERNAME or not TARGET_EMAIL:
            logging.critical("⚠️ ERROR: LEETCODE_USERNAME and TARGET_EMAIL must be set in .env or GitHub Secrets.")
            sys.exit(1)
            
        print("="*50)
        print(f"🚀 Running Automated LeetCode Check")
        print(f"👤 Target User: {LEETCODE_USERNAME}")
        print(f"📧 Target Email: {TARGET_EMAIL}")
        print("="*50)
        
        # Run EXACTLY ONE check, then the script finishes
        check_user_status(LEETCODE_USERNAME, TARGET_EMAIL)

        print("="*50)
        print("✅ Execution completed.")
        
    except Exception as e:
        logging.critical(f"🔥 CRITICAL FAILURE in main execution: {str(e)}")
        sys.exit(1)