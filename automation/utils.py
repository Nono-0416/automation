from datetime import datetime
import os

def save_screenshot(driver, name, folder="screenshots"):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    os.makedirs(folder, exist_ok=True)
    path = f"{folder}/{name}_{timestamp}.png"
    driver.save_screenshot(path)