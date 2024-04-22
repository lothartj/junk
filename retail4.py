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

    "MCC0001567": [
        "FROZEN VEG",
        "CORN",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0001572": [
        "FROZEN VEG",
        "BUTTERNUT",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0001703": [
        "FROZEN POTATO",
        "CHIPS & FRIES",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0001707": [
        "FROZEN POTATO",
        "CHIPS & FRIES",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0001753": [
        "FROZEN VEG",
        "MIXED VEG",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0002034": [
        "FROZEN VEG",
        "PEAS",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0002035": [
        "FROZEN VEG",
        "MIXED VEG",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0002036": [
        "FROZEN VEG",
        "STIR FRY",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0002037": [
        "FROZEN VEG",
        "STIR FRY",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0002040": [
        "FROZEN VEG",
        "CARROTS",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0002041": [
        "FROZEN VEG",
        "GREEN BEAN",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0002042": [
        "FROZEN VEG",
        "CORN",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0002043": [
        "FROZEN VEG",
        "MIXED VEG",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0002202": [
        "FROZEN POTATO",
        "POTATO",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0002204": [
        "FROZEN POTATO",
        "CHIPS & FRIES",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0002205": [
        "FROZEN POTATO",
        "POTATO",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0002220": [
        "FROZEN POTATO",
        "CHIPS & FRIES",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0002221": [
        "FROZEN POTATO",
        "CHIPS & FRIES",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0002344": [
        "FROZEN POTATO",
        "CHIPS & FRIES",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0002345": [
        "FROZEN POTATO",
        "CHIPS & FRIES",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0002645": [
        "FROZEN POTATO",
        "POTATO",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0002946": [
        "FROZEN POTATO",
        "CHIPS & FRIES",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0002948": [
        "FROZEN POTATO",
        "CHIPS & FRIES",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0002949": [
        "FROZEN POTATO",
        "CHIPS & FRIES",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0003032": [
        "FROZEN VEG",
        "MIXED VEG",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0003033": [
        "FROZEN VEG",
        "BROCCOLI",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0003085": [
        "FROZEN POTATO",
        "CHIPS & FRIES",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0003088": [
        "FROZEN POTATO",
        "CHIPS & FRIES",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0004279": [
        "FROZEN POTATO",
        "CHIPS & FRIES",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0004947": [
        "FROZEN POTATO",
        "POTATO",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0005832": [
        "FROZEN VEG",
        "CHAKALAKA",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0007722": [
        "FROZEN VEG",
        "MIXED VEG",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0007778": [
        "FROZEN VEG",
        "STIR FRY",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0007779": [
        "FROZEN VEG",
        "STIR FRY",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0007781": [
        "FROZEN VEG",
        "STIR FRY",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0007782": [
        "FROZEN VEG",
        "CARROTS",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0007783": [
        "FROZEN VEG",
        "PEAS",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0007784": [
        "FROZEN VEG",
        "CAULIFLOWER",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0007785": [
        "FROZEN VEG",
        "PUMPKIN",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0007786": [
        "FROZEN VEG",
        "GREEN BEAN",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0007787": [
        "FROZEN VEG",
        "SWEET POTATO",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0007788": [
        "FROZEN VEG",
        "SWEET POTATO",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0007789": [
        "FROZEN VEG",
        "SWEET POTATO",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0007790": [
        "FROZEN VEG",
        "MIXED VEG",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0007791": [
        "FROZEN VEG",
        "CARROTS",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0007802": [
        "FROZEN VEG",
        "CORN",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0007803": [
        "FROZEN VEG",
        "CARROTS",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0007804": [
        "FROZEN VEG",
        "MIXED VEG",
        "MCCAIN",
        "HARVESTIME",
        "FROZENMC"
    ],
    "MCC0007805": [
        "FROZEN VEG",
        "MIXED VEG",
        "MCCAIN",
        "HARVESTIME",
        "FROZENMC"
    ],
    "MCC0007809": [
        "FROZEN VEG",
        "MIXED VEG",
        "MCCAIN",
        "HARVESTIME",
        "FROZENMC"
    ],
    "MCC0007810": [
        "FROZEN VEG",
        "MIXED VEG",
        "MCCAIN",
        "HARVESTIME",
        "FROZENMC"
    ],
    "MCC0007811": [
        "FROZEN VEG",
        "PEAS",
        "MCCAIN",
        "HARVESTIME",
        "FROZENMC"
    ],
    "MCC0007812": [
        "FROZEN VEG",
        "CORN",
        "MCCAIN",
        "HARVESTIME",
        "FROZENMC"
    ],
    "MCC0007813": [
        "FROZEN VEG",
        "GREEN BEAN",
        "MCCAIN",
        "HARVESTIME",
        "FROZENMC"
    ],
    "MCC0007814": [
        "FROZEN VEG",
        "CARROTS",
        "MCCAIN",
        "HARVESTIME",
        "FROZENMC"
    ],
    "MCC0007815": [
        "FROZEN VEG",
        "PEAS",
        "MCCAIN",
        "HARVESTIME",
        "FROZENMC"
    ],
    "MCC0007817": [
        "FROZEN VEG",
        "GREEN BEAN",
        "MCCAIN",
        "HARVESTIME",
        "FROZENMC"
    ],
    "MCC0007819": [
        "FROZEN POTATO",
        "CHIPS & FRIES",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0007820": [
        "FROZEN VEG",
        "CHIPS & FRIES",
        "MCCAIN",
        "HARVESTIME",
        "FROZENMC"
    ],
    "MCC0007938": [
        "FROZEN POTATO",
        "CHIPS & FRIES",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0008348": [
        "FROZEN VEG",
        "BROCCOLI",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0008356": [
        "FROZEN VEG",
        "BUTTERNUT",
        "MCCAIN",
        "HARVESTIME",
        "FROZENMC"
    ],
    "MCC0008357": [
        "FROZEN VEG",
        "BEETROOT",
        "MCCAIN",
        "HARVESTIME",
        "FROZENMC"
    ],
    "MCC0008358": [
        "FROZEN VEG",
        "POTATO",
        "MCCAIN",
        "HARVESTIME",
        "FROZENMC"
    ],
    "MCC0008408": [
        "FROZEN POTATO",
        "CHIPS & FRIES",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0008409": [
        "FROZEN VEG",
        "PEAS",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0008729": [
        "FROZEN POTATO",
        "CHIPS & FRIES",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0009808": [
        "FROZEN VEG",
        "MIXED VEG",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0009907": [
        "FROZEN POTATO",
        "CHIPS & FRIES",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0009908": [
        "FROZEN POTATO",
        "CHIPS & FRIES",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0009913": [
        "FROZEN VEG",
        "MIXED VEG",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0009914": [
        "FROZEN POTATO",
        "MIXED VEG",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0009921": [
        "FROZEN VEG",
        "MIXED VEG",
        "MCCAIN",
        "HARVESTIME",
        "FROZENMC"
    ],
    "MCC0009922": [
        "FROZEN VEG",
        "PEAS",
        "MCCAIN",
        "HARVESTIME",
        "FROZENMC"
    ],
    "MCC0009926": [
        "FROZEN VEG",
        "PEAS",
        "MCCAIN",
        "HARVESTIME",
        "FROZENMC"
    ],
    "MCC0009929": [
        "FROZEN POTATO",
        "CHIPS & FRIES",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0009930": [
        "FROZEN POTATO",
        "CHIPS & FRIES",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0009931": [
        "FROZEN VEG",
        "SPINACH",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0009932": [
        "FROZEN VEG",
        "MIXED VEG",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0009933": [
        "FROZEN VEG",
        "MIXED VEG",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0009934": [
        "FROZEN VEG",
        "MIXED VEG",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0009936": [
        "FROZEN VEG",
        "MIXED VEG",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0009939": [
        "FROZEN VEG",
        "CARROTS",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0009940": [
        "FROZEN VEG",
        "GREEN BEAN",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0009941": [
        "FROZEN VEG",
        "PEAS",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0009943": [
        "FROZEN VEG",
        "CORN",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0009944": [
        "FROZEN VEG",
        "PUMPKIN",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0009945": [
        "FROZEN VEG",
        "BRUSSEL SPOUTS",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0009950": [
        "FROZEN VEG",
        "STIR FRY",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0009951": [
        "FROZEN VEG",
        "STIR FRY",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0009991": [
        "FROZEN VEG",
        "MIXED VEG",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0030172": [
        "FROZEN POTATO",
        "CHIPS & FRIES",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0030173": [
        "FROZEN POTATO",
        "CHIPS & FRIES",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0039938": [
        "FROZEN VEG",
        "CAULIFLOWER",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0913038": [
        "FROZEN VEG",
        "VEG BURGER",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0913892": [
        "FROZEN VEG",
        "POTATO",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ],
    "MCC0913896": [
        "FROZEN POTATO",
        "POTATO",
        "MCCAIN",
        "MCCAIN",
        "FROZENMC"
    ], }

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
