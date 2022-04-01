import json
from facebook_scraper import *

# credentials = {
#     "username": "kepet69205@procowork.com",
#     "password": "*****",
# }

# fs = FacebookScraper()
# # fs.set_user_agent("Mozilla/5.0 (Android 4.4; Mobile; rv:41.0) Gecko/41.0 Firefox/41.0")
# fs.login(credentials["username"], credentials["password"])

# profile = fs.get_profile("WillSmith", friends=False, followers=False, following=False)
# print(json.dumps(profile))

def run_job(job_def, user_credentials):
    fs = FacebookScraper()
    set_user_agent(
    "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")
    fs.login(user_credentials["username"], user_credentials["password"])
    return fs.get_profile(job_def["profile_id"], friends=False, followers=False, following=False)