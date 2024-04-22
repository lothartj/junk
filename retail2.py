from playwright.sync_api import Playwright, sync_playwright
import time


def wait_for_selector_within_iframe(iframe, selector, timeout=10):
    start_time = time.time()
    while time.time() - start_time < timeout:
        if iframe.locator(selector).count() > 0:
            return True
        time.sleep(1)
    return False



def time5():
    time.sleep(5)

def time3():
    time.sleep(3)

# data_dict = {
#     "HEI0002213": ["PIES", "STEAK & KIDNEY", "PIONEER", "BIG J", "FROZENPI"],
#     "HEI0002976": ["PIES", "CHICKEN MUSHROOM", "PIONEER", "BIG J", "FROZENPI"],
#     "HEI0002978": ["PIES", "MUTTON CURRY", "PIONEER", "BIG J", "FROZENPI"],
#     "HEI0002979": ["PIES", "PEPPER STEAK", "PIONEER", "BIG J", "FROZENPI"],
#     "HEI0031104": ["PASTRY & DOUGH", "PUFF", "PIONEER", "HOUSE B", "FROZENPI"],
#     "HEI0031105": ["PIES", "SAUSAGE ROLL", "PIONEER", "RITE B", "FROZENPI"],
#     "HEI0031106": ["PIES", "SAUSAGE ROLL", "PIONEER", "HOUSE B", "FROZENPI"],
# }

data_dict = {
    "LAN0071794": [
        "SOFT CHEESE",
        "CHUNKY",
        "LANCEWOOD",
        "LW",
        "CHILLLW"],
 }

def get_attributes(identifier):
    return data_dict.get(identifier, [])

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("")
    page.get_by_label("User name:").click()
    page.get_by_label("User name:").fill("")
    page.get_by_label("User name:").press("Tab")
    page.get_by_label("Password:").fill("")
    page.get_by_label("Password:").press("Enter")
    time3()
    page.goto("")
    page.goto("")
    page.goto("")
    time3()
    page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("menuitem", name="Tall Tiles layout selected").click()
    time3()
    page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("menuitemradio", name="List").click()
    time3()
    iframe = page.frame_locator("iframe[title=\"Main Content\"]")

    for identifier, attributes in data_dict.items():
        print(f"Identifier: {identifier}")
        print(f"Attributes: {attributes}")

        time3()
        # identifier = identifier
        attribute0 = attributes[0]
        attribute1 = attributes[1]
        attribute2 = attributes[2]
        attribute3 = attributes[3]
        attribute4 = attributes[4]

        # for attribute in attributes:
        #     time3()
        #     identifier = identifier
        #     attribute0 = attributes[0]
        #     attribute1 = attributes[1]
        #     attribute2 = attributes[2]
        #     attribute3 = attributes[3]
        #     attribute4 = attributes[4]
        try:
    # Attempt to click the first button with the special character
                page.frame_locator("iframe[title=\"Main Content\"]").get_by_text("Search").click()
        except:
                try:
                    # If the first button is not available, attempt to click the second button
                    page.frame_locator("iframe[title=\"Main Content\"]").get_by_text("Search").click()
                except:
        # If neither button is available, handle the situation accordingly
                    print("Both buttons are not available or an error occurred.")


        page.frame_locator("iframe[title=\"Main Content\"]").get_by_placeholder("Search").press("Control+a")
            
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_placeholder("Search").fill(f"Z-{identifier}")
        time3()
        # if wait_for_selector_within_iframe(iframe, 'css=div > table > tbody > tr:nth-child(2) > td:nth-child(3) > a'):
        #     # Click the element within the iframe using XPath selector
        #         iframe.locator('css=div > table > tbody > tr:nth-child(2) > td:nth-child(3) > a').click()
        # Click the element within the iframe using the CSS selector directly
        # iframe.locator('css=div > table > tbody > tr:nth-child(2) > td:nth-child(3) > a').click()

        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("button", name=f"No., sorted in Ascending order Z-{identifier}").click()
        
        time3()
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("button", name="Item Attributes").click()
        time3()
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("menuitem", name="Edit").locator("div").nth(2).click()
        time5()
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("combobox", name="Attribute, sorted in Ascending order").click()
        time5()
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("button", name="Name 01-GROUP").click()
        time5()
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("combobox", name="Attribute, sorted in Ascending order").press("Tab")
        time5()
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("combobox", name="Value").fill(attribute0)
        time5()
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("combobox", name="Value").press("Tab")
        time5()
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("button", name="Choose a value for Attribute").click()
        time5()
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("button", name="Name 02-SUB GROUP").click()
        time5()
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("combobox", name="Attribute, sorted in Ascending order").press("Tab")
        time5()
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("combobox", name="Value").fill(attribute1)
        time5()
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("combobox", name="Value").press("Tab")
        time5()
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("button", name="Choose a value for Attribute").click()
        time5()
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("button", name="Name 03-SUPPLIER").click()
        time5()
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("combobox", name="Attribute, sorted in Ascending order").press("Tab")
        time5()
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("combobox", name="Value").fill(attribute2)
        time5()
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("combobox", name="Value").press("Tab")
        time5()
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("button", name="Choose a value for Attribute").click()
        time5()
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("button", name="Name 04-BRAND").click()
        time5()
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("combobox", name="Attribute, sorted in Ascending order").press("Tab")
        time5()
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("combobox", name="Value").fill(attribute3)
        time5()
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("combobox", name="Value").press("Tab")
        time5()
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("button", name="Choose a value for Attribute").click()
        time5()
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("button", name="Name 05-RETAIL SUMMARY").click()
        time5()
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("combobox", name="Attribute, sorted in Ascending order").press("Tab")
        time5()
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("combobox", name="Value").fill(attribute4)
        time5()
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("combobox", name="Value").press("Tab")
        time5()
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_text("OKCancel").click()
        time5()
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("button", name="OK").click()
        time5()
        page.frame_locator("iframe[title=\"Main Content\"]").get_by_role("button", name="Back").click()
        time5()
        page.goto("")
        time3()

    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
