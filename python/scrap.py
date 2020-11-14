
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


location = "https://docs.google.com/forms/d/e/1FAIpQLSfzocEm6IEDKVzVGOlg8ijysWZyAvQur0NheJb_I_xozgKusA/viewform?usp=sf_link"

data = {}

driver = webdriver.Chrome(executable_path="/home/pmoracho/Tmp/chromedriver")

driver.get(location)

title = driver.find_element_by_class_name(
    "freebirdFormviewerViewHeaderTitleRow"
    ).text
data[title] = {}

while True:
    containers = driver.find_elements_by_class_name(
        "freebirdFormviewerViewNumberedItemContainer"
        )
    btns = driver.find_elements_by_css_selector(".appsMaterialWizButtonEl")
    if not btns:
        break
    for container in containers:
        try:
            question = container.find_element_by_class_name(
                "freebirdFormviewerViewItemsItemItemTitle"
                )
        except NoSuchElementException:
            continue
        responses = container.find_elements_by_class_name(
            "docssharedWizToggleLabeledLabelText"
            )
        data[title][question.text] = [response.text for response in responses]
    btns[-1].click()
driver.quit()

print(data)