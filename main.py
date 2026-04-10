import logging
from leetcode_api import has_submitted_today

from email_service import send_reminder

# Setup simple logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

def check_user_status(username: str, email: str):
    """
    Core logic to check if a user has submitted today and send an email if not.
    """
    logging.info(f"Checking LeetCode status for user: {username} (Target Email: {email})")
    
    submitted_today = has_submitted_today(username)
    
    if submitted_today:
        logging.info(f"[{username}] PASS: User has already submitted a problem today. Excellent!")
    else:
        logging.warning(f"[{username}] FAIL: User HAS NOT submitted a problem today. Sending reminder...")
        
        # Send actual email
        success = send_reminder(email)
        
        if not success:
            # Fallback to mock print if email isn't configured
            print("\n" + "="*50)
            print(f"MOCK EMAIL (Config Missing) TO: {email}")
            print("SUBJECT: LeetCode Daily Accountability Reminder")
            print("BODY:")
            print("You haven't solved a LeetCode problem today. Stop being lazy and get it done.")
            print("="*50 + "\n")

if __name__ == "__main__":
    from dotenv import load_dotenv
    import os
    import sys
    import schedule
    import time
    
    load_dotenv()
    
    LEETCODE_USERNAME = os.environ.get("LEETCODE_USERNAME")
    TARGET_EMAIL = os.environ.get("TARGET_EMAIL")
    
    try:
        INTERVAL_SECONDS = int(os.environ.get("INTERVAL_SECONDS", 0))
        INTERVAL_HOURS = int(os.environ.get("INTERVAL_HOURS", 2))
    except ValueError:
        INTERVAL_SECONDS = 0
        INTERVAL_HOURS = 2
        
    if not LEETCODE_USERNAME or not TARGET_EMAIL:
        print("⚠️ ERROR: LEETCODE_USERNAME and TARGET_EMAIL must be set in .env")
        sys.exit(1)
        
    print("="*50)
    print(f"🚀 Starting LeetCode Accountability Scheduler")
    print(f"👤 Target User: {LEETCODE_USERNAME}")
    print(f"📧 Target Email: {TARGET_EMAIL}")
    
    if INTERVAL_SECONDS > 0:
        print(f"⏰ Interval: Every {INTERVAL_SECONDS} SECONDS (🔥 DEMO MODE)")
        schedule.every(INTERVAL_SECONDS).seconds.do(check_user_status, LEETCODE_USERNAME, TARGET_EMAIL)
    else:
        print(f"⏰ Interval: Every {INTERVAL_HOURS} hours")
        schedule.every(INTERVAL_HOURS).hours.do(check_user_status, LEETCODE_USERNAME, TARGET_EMAIL)
        
    print("="*50)
    
    # Run an initial check at boot
    check_user_status(LEETCODE_USERNAME, TARGET_EMAIL)

    # Continuous execution loop
    try:
        while True:
            schedule.run_pending()
            time.sleep(1) # check pending jobs every 1 second (essential for precise timing)
    except KeyboardInterrupt:
        print("\n⏳ Scheduler stopped manually.")
