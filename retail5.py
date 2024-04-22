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

    "RICH016474": [
        "MUFFIN BATTER",
        "LEMON POPPY",
        "RICH",
        "RICH",
        "FROZENRI"
    ],
    "RICH016478": [
        "MUFFIN BATTER",
        "RAISIN BRAN",
        "RICH",
        "RICH",
        "FROZENRI"
    ],
    "RICH016486": [
        "MUFFIN BATTER",
        "MIXED",
        "RICH",
        "RICH",
        "FROZENRI"
    ],
    "RICH016493": [
        "MUFFIN BATTER",
        "MIXED",
        "RICH",
        "RICH",
        "FROZENRI"
    ],
    "RICH018011": [
        "MUFFIN BATTER",
        "CHOC",
        "RICH",
        "RICH",
        "FROZENRI"
    ],
    "RICH018012": [
        "MUFFIN BATTER",
        "BLUEBERRY",
        "RICH",
        "RICH",
        "FROZENRI"
    ],
    "RICH018101": [
        "CREAM",
        "VERSATIE",
        "RICH",
        "RICH",
        "FROZENRI"
    ],
    "RICH018467": [
        "ECLAIRS",
        "WHITE DUO",
        "RICH",
        "RICH",
        "FROZENRI"
    ],
    "RICH019705": [
        "ECLAIRS",
        "CLASSIC",
        "RICH",
        "RICH",
        "FROZENRI"
    ],
    "RICH019706": [
        "ECLAIRS",
        "WHITE CHOC",
        "RICH",
        "RICH",
        "FROZENRI"
    ],
    "RICH019708": [
        "ECLAIRS",
        "RASPBERRY",
        "RICH",
        "RICH",
        "FROZENRI"
    ],
    "RICH019709": [
        "ECLAIRS",
        "CARAMEL",
        "RICH",
        "RICH",
        "FROZENRI"
    ],
    "RICH019710": [
        "ECLAIRS",
        "HAZELNUT",
        "RICH",
        "RICH",
        "FROZENRI"
    ],
    "RICH020168": [
        "BREAD",
        "PRETZEL",
        "RICH",
        "RICH",
        "FROZENRI"
    ],
    "RICH020169": [
        "BREAD",
        "BAGUETTE",
        "RICH",
        "RICH",
        "FROZENRI"
    ],
    "RICH020170": [
        "BREAD",
        "BAGUETTE",
        "RICH",
        "RICH",
        "FROZENRI"
    ],
    "S5TASTY868": [
        "BEEF",
        "SAUSAGE",
        "DEEPCATCH",
        "DEEPCATCH",
        "FROZEN"
    ],
    "S5TASTY882": [
        "BEEF",
        "SAUSAGE",
        "DEEPCATCH",
        "DEEPCATCH",
        "FROZENDC"
    ],
    "SCEL009801": [
        "FROZEN VEG",
        "MUSHROOM",
        "SPFEX",
        "SCELTA",
        "FROZEN"
    ],
    "SCEL042050": [
        "FROZEN VEG",
        "ONION",
        "SPFEX",
        "SCELTA",
        "FROZEN"
    ],
    "SKY0000250": [
        "PROCESSED",
        "SAUSAGE",
        "DEEPCATCH",
        "SKY COUNTR",
        "FROZEN"
    ],
    "SKY0001250": [
        "PROCESSED",
        "SAUSAGE",
        "DEEPCATCH",
        "SKY COUNTR",
        "FROZEN"
    ],
    "SKY0001269": [
        "PROCESSED",
        "SAUSAGE",
        "DEEPCATCH",
        "SKY COUNTR",
        "FROZEN"
    ],
    "SKY0002250": [
        "PROCESSED",
        "PATTIES",
        "DEEPCATCH",
        "SKY COUNTR",
        "FROZEN"
    ],
    "SKY0003072": [
        "PROCESSED",
        "SAUSAGE",
        "DEEPCATCH",
        "SKY COUNTR",
        "FROZEN"
    ],
    "SKY0003250": [
        "PROCESSED",
        "MINCE",
        "DEEPCATCH",
        "SKY COUNTR",
        "FROZEN"
    ],
    "SKY0008056": [
        "PROCESSED",
        "SAUSAGE",
        "DEEPCATCH",
        "SKY COUNTR",
        "FROZEN"
    ],
    "SKY0008124": [
        "PROCESSED",
        "RUSSIANS",
        "DEEPCATCH",
        "SKY COUNTR",
        "FROZEN"
    ],
    "SKY0008344": [
        "PROCESSED",
        "RUSSIANS",
        "DEEPCATCH",
        "SKY COUNTR",
        "FROZEN"
    ],
    "SOV0000836": [
        "CRUMBED,BREADED CHICKEN",
        "BURGER",
        "DEEPCATCH",
        "CHICKA",
        "FROZENSO"
    ],
    "SOV0002919": [
        "CRUMBED,BREADED CHICKEN",
        "BURGER",
        "DEEPCATCH",
        "TIZER",
        "FROZENTI"
    ],
    "SOV0002921": [
        "CRUMBED,BREADED CHICKEN",
        "BURGER",
        "DEEPCATCH",
        "TIZER",
        "FROZENTI"
    ],
    "SOV0002953": [
        "CHICKEN",
        "WINGS",
        "DEEPCATCH",
        "TIZER",
        "FROZENTI"
    ],
    "SOV0002954": [
        "CHICKEN",
        "DRUMSTICKS",
        "DEEPCATCH",
        "TIZER",
        "FROZENTI"
    ],
    "SOV0002955": [
        "CHICKEN",
        "THIGHS",
        "DEEPCATCH",
        "TIZER",
        "FROZENTI"
    ],
    "SOV0003250": [
        "CHICKEN",
        "TERTIARIES",
        "DEEPCATCH",
        "SOV",
        "FROZENTI"
    ],
    "SOV0003481": [
        "CRUMBED,BREADED CHICKEN",
        "BURGER",
        "DEEPCATCH",
        "SPAR",
        "FROZENSO"
    ],
    "SOV0003482": [
        "CRUMBED,BREADED CHICKEN",
        "BURGER",
        "DEEPCATCH",
        "SPAR",
        "FROZENSO"
    ],
    "SOV0003483": [
        "CRUMBED,BREADED CHICKEN",
        "BURGER",
        "DEEPCATCH",
        "SPAR",
        "FROZENSO"
    ],
    "SOV0003484": [
        "CRUMBED,BREADED CHICKEN",
        "BURGER",
        "DEEPCATCH",
        "SPAR",
        "FROZENSO"
    ],
    "SOV0003799": [
        "CHICKEN",
        "LEG QUARTERS",
        "DEEPCATCH",
        "CHICKA",
        "FROZENSO"
    ],
    "SOV0003803": [
        "CHICKEN",
        "BREAST FILLETS",
        "DEEPCATCH",
        "SPAR",
        "FROZENSO"
    ],
    "SOV0003804": [
        "CRUMBED,BREADED CHICKEN",
        "STRIPS",
        "DEEPCATCH",
        "SPAR",
        "FROZENSO"
    ],
    "SOV0003810": [
        "CHICKEN",
        "DRUMSTICKS",
        "DEEPCATCH",
        "CHICKA",
        "FROZENSO"
    ],
    "SOV0003811": [
        "CHICKEN",
        "WINGS",
        "DEEPCATCH",
        "CHICKA",
        "FROZENSO"
    ],
    "SOV0003812": [
        "CHICKEN",
        "THIGHS",
        "DEEPCATCH",
        "CHICKA",
        "FROZENSO"
    ],
    "SOV0003815": [
        "CHICKEN",
        "WINGS",
        "DEEPCATCH",
        "CHICKA",
        "FROZENSO"
    ],
    "SOV0003816": [
        "CHICKEN",
        "BREAST FILLETS",
        "DEEPCATCH",
        "CHICKA",
        "FROZENSO"
    ],
    "SOV0003817": [
        "CRUMBED,BREADED CHICKEN",
        "BITES",
        "DEEPCATCH",
        "CHICKA",
        "FROZENSO"
    ],
    "SOV0003818": [
        "CRUMBED,BREADED CHICKEN",
        "STRIPS",
        "DEEPCATCH",
        "CHICKA",
        "FROZENSO"
    ],
    "SOV0003820": [
        "CHICKEN",
        "DRUMSTICKS",
        "DEEPCATCH",
        "TIZER",
        "FROZENTI"
    ],
    "SOV0003821": [
        "CHICKEN",
        "WINGS",
        "DEEPCATCH",
        "TIZER",
        "FROZENTI"
    ],
    "SOV0003822": [
        "CHICKEN",
        "THIGHS",
        "DEEPCATCH",
        "TIZER",
        "FROZENTI"
    ],
    "SOV0003824": [
        "CHICKEN",
        "WINGS",
        "DEEPCATCH",
        "TIZER",
        "FROZENTI"
    ],
    "SOV0003825": [
        "CHICKEN",
        "WINGS",
        "DEEPCATCH",
        "TIZER",
        "FROZENTI"
    ],
    "SOV0003826": [
        "CHICKEN",
        "BREAST FILLETS",
        "DEEPCATCH",
        "TIZER",
        "FROZENTI"
    ],
    "SOV0003828": [
        "CRUMBED,BREADED CHICKEN",
        "POPS",
        "DEEPCATCH",
        "TIZER",
        "FROZENTI"
    ],
    "SOV0003829": [
        "CRUMBED,BREADED CHICKEN",
        "POPS",
        "DEEPCATCH",
        "TIZER",
        "FROZENTI"
    ],
    "SOV0003830": [
        "CRUMBED,BREADED CHICKEN",
        "STRIPS",
        "DEEPCATCH",
        "TIZER",
        "FROZENTI"
    ],
    "SOV0003886": [
        "CRUMBED,BREADED CHICKEN",
        "BURGER",
        "DEEPCATCH",
        "SPAR",
        "FROZENSO"
    ],
    "SOV0003887": [
        "CRUMBED,BREADED CHICKEN",
        "SCHNITZEL",
        "DEEPCATCH",
        "SPAR",
        "FROZENSO"
    ],
    "SOV0003951": [
        "CRUMBED,BREADED CHICKEN",
        "BITES",
        "DEEPCATCH",
        "SPAR",
        "FROZENSO"
    ],
    "SOV0003952": [
        "CHICKEN",
        "MIXED PORT",
        "DEEPCATCH",
        "SPAR",
        "FROZENSO"
    ],
    "SOV0003955": [
        "CRUMBED,BREADED CHICKEN",
        "BITES",
        "DEEPCATCH",
        "CHICKA",
        "FROZENSO"
    ],
    "SOV0003956": [
        "CRUMBED,BREADED CHICKEN",
        "STRIPS",
        "DEEPCATCH",
        "CHICKA",
        "FROZENSO"
    ],
    "SOV0003957": [
        "CRUMBED,BREADED CHICKEN",
        "BURGER",
        "DEEPCATCH",
        "CHICKA",
        "FROZENSO"
    ],
    "SOV0003958": [
        "CRUMBED,BREADED CHICKEN",
        "SCHNITZEL",
        "DEEPCATCH",
        "CHICKA",
        "FROZENSO"
    ],
    "SOV0003981": [
        "CRUMBED,BREADED CHICKEN",
        "BITES",
        "DEEPCATCH",
        "TIZER",
        "FROZENTI"
    ],
    "SOV0003982": [
        "CRUMBED,BREADED CHICKEN",
        "STRIPS",
        "DEEPCATCH",
        "TIZER",
        "FROZENTI"
    ],
    "SOV0003983": [
        "CRUMBED,BREADED CHICKEN",
        "SCHNITZEL",
        "DEEPCATCH",
        "TIZER",
        "FROZENTI"
    ],
    "SOV0003984": [
        "CRUMBED,BREADED CHICKEN",
        "BURGER",
        "DEEPCATCH",
        "TIZER",
        "FROZENTI"
    ],
    "SOV0004136": [
        "CHICKEN",
        "WINGS",
        "DEEPCATCH",
        "CHICKA",
        "FROZENSO"
    ],
    "SOV0004137": [
        "CHICKEN",
        "WINGS",
        "DEEPCATCH",
        "CHICKA",
        "FROZENSO"
    ],
    "SOV0004157": [
        "CHICKEN",
        "TERTIARIES",
        "DEEPCATCH",
        "CHICKA",
        "FROZENSO"
    ],
    "SOV0004158": [
        "CHICKEN",
        "WINGS",
        "DEEPCATCH",
        "CHICKA",
        "FROZENSO"
    ],
    "SOV0004162": [
        "CHICKEN",
        "TERTIARIES",
        "DEEPCATCH",
        "CHICKA",
        "FROZENSO"
    ],
    "SOV0004600": [
        "CRUMBED,BREADED CHICKEN",
        "BURGER",
        "DEEPCATCH",
        "TIZER",
        "FROZENTI"
    ],
    "SOV0004601": [
        "CRUMBED,BREADED CHICKEN",
        "BITES",
        "DEEPCATCH",
        "TIZER",
        "FROZENTI"
    ],
    "SOV0004602": [
        "CRUMBED,BREADED CHICKEN",
        "STRIPS",
        "DEEPCATCH",
        "TIZER",
        "FROZENTI"
    ],
    "SOV0004603": [
        "CRUMBED,BREADED CHICKEN",
        "STRIPS",
        "DEEPCATCH",
        "SPAR",
        "FROZENSO"
    ],
    "SOV0004604": [
        "CRUMBED,BREADED CHICKEN",
        "BITES",
        "DEEPCATCH",
        "SPAR",
        "FROZENSO"
    ],
    "SOV0004605": [
        "CHICKEN",
        "BREAST FILLETS",
        "DEEPCATCH",
        "SPAR",
        "FROZENSO"
    ],
    "SOV0004606": [
        "CHICKEN",
        "WINGS",
        "DEEPCATCH",
        "TIZER",
        "FROZENTI"
    ],
    "SOV0004607": [
        "CRUMBED,BREADED CHICKEN",
        "BURGER",
        "DEEPCATCH",
        "SPAR",
        "FROZENSO"
    ],
    "SOV0004620": [
        "CHICKEN",
        "WINGS",
        "DEEPCATCH",
        "CHICKA",
        "FROZENSO"
    ],
    "SOV0004640": [
        "CRUMBED,BREADED CHICKEN",
        "CHIPS & FRIES",
        "DEEPCATCH",
        "SPAR",
        "FROZENSO"
    ],
    "SOV0004655": [
        "CHICKEN",
        "BURGER",
        "DEEPCATCH",
        "SPAR",
        "FROZENSO"
    ],
    "SOV0004656": [
        "CHICKEN",
        "BREAST FILLETS",
        "DEEPCATCH",
        "SPAR",
        "FROZENSO"
    ],
    "SOV0004657": [
        "CHICKEN",
        "BREAST FILLETS",
        "DEEPCATCH",
        "SPAR",
        "FROZENSO"
    ],
    "SOV0004662": [
        "CRUMBED,BREADED CHICKEN",
        "BURGER",
        "DEEPCATCH",
        "SPAR",
        "FROZENSO"
    ],
    "SOV0004665": [
        "CRUMBED,BREADED CHICKEN",
        "STRIPS",
        "DEEPCATCH",
        "SPAR",
        "FROZENSO"
    ],
    "SOV0004666": [
        "CRUMBED,BREADED CHICKEN",
        "BITES",
        "DEEPCATCH",
        "SPAR",
        "FROZENSO"
    ]}

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
