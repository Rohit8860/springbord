from playwright.sync_api import sync_playwright
import time
from loguru import logger
import tempfile


class browser_launch():
    def __init__(self):
        logger.info("Start Bot ...............")
        self.launch_browser()

    def launch_browser(self):
        with sync_playwright() as p:
            temp_dir = tempfile.mkdtemp()
            try:
                firefox = p.firefox.launch_persistent_context(
                    temp_dir,headless=False, 
                    # proxy={
                    #     'server': f'http://{self.host}:{self.port}',
                    #     'username': self.proxy_user,
                    #     'password': self.proxy_password
                    # }, 
                args=["--private"],
                viewport={'width': 700, 'height': 800},
                device_scale_factor=3,
                is_mobile=True,
                has_touch=True,
                # permissions=[],
                # geolocation=None,
                # extra_http_headers=headers,
                # locale=r"en-US,en;q=0.9",
                # storage_state={cookies: [{}]
                user_agent='Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36'

                )
                
                self.page = firefox.pages[0]

                self.page.goto("https://www.google.com/",wait_until='load', timeout=50000)

                try:
                    self.page.wait_for_selector("#onetrust-button-group #onetrust-accept-btn-handler", timeout=10000)
                    self.page.click("#onetrust-button-group #onetrust-accept-btn-handler")
                except:
                    print("Consent button not found, skipping...")

                time.sleep(2000)

            except Exception as E:
                logger.error(f"Browser Launch Failed : {E}" )
