from scraper import run_job
import schedule
import time

def get_job_def():
    return {
        "profile_id": "mark",
    }

def get_user_credentials():
    return {
    "username": "kepet69205@procowork.com",
    "password": "*****",
    }

def save(result):
    print("Saving result")
    print(result)

def run_scraper():
    print("Running scraper")
    job_def = get_job_def()
    user_credentials = get_user_credentials()
    try:
        result = run_job(job_def, user_credentials)
        save(result)
    except Exception as e:
        print("Error: {}".format(e))

# After every 5 to 10mins in between run scraper
schedule.every(5).to(10).seconds.do(run_scraper)

if __name__ == '__main__':
    while True:
        schedule.run_pending()
        time.sleep(1)