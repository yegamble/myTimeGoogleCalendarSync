import pyotp

# Global Variables
EMPLOYEE_ID = 00000000
PASSWORD = "myPassword"
API_KEY = "eb2551e4accc14f38cc42d32fbc2b2ea"
PUSHOVER_APP_API_KEY = ""
PUSHOVER_USER_API_KEY = ""
# you can change this but the default one should work
headless = False
totp = pyotp.TOTP("")
# MFA code here.

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0",
    "Upgrade-Insecure-Requests": "1",
    "DNT": "1",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
}


def get_mfa_code():
    return totp.now()
