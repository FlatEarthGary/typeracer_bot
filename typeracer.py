from selenium import webdriver
import pyperclip
import time
import re
from pprint import pprint
from bs4 import BeautifulSoup
import pyinputplus
from getpass import getpass

profile = webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override",
                       "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:68.0) Gecko/20100101 Firefox/68.0")

identifier = re.compile(r"(\w){8}\s(\w){8}")
second_identifier = re.compile(r"(\w){8}")
usr = input("Input your typeracer username: ")
password = getpass(
    "Input your typeracer password (btw, you won't notice it typing): ")

print("Starting up Firefox...")
try:
    browser = webdriver.Firefox(profile,
                                executable_path=r"")  # PUT THE GECKODRIVER EXECUTABLE PATH BETWEEN THE "", for example "C:\geckodriver-v0.27.0-win64\geckodriver.exe"
except:
    print("FAILED!")
    print("Have you put the path to the geckodriver path into the source code?")
    exit()
print("Successfully started up Firefox!\nNavigating to typeracer.com...")
browser.get("https://typeracer.com")
print("Successfully connected to typeracer.com")
time.sleep(3)
print("Finding cookies agreement...")
agree = browser.find_element_by_css_selector("button.sc-bwzfXH:nth-child(3)")
agree.click()
print("Accepted!")


sign_in = browser.find_element_by_xpath(
    "/html/body/div[2]/table/tbody/tr/td[3]/div/table/tbody/tr[2]/td[1]/table/tbody/tr/td[1]/a")
sign_in.click()
print("Typing in username...")
username = browser.find_element_by_xpath(
    "/html/body/div[7]/div/div/div[3]/div/div[1]/div/table[1]/tbody/tr[2]/td/div/table/tbody/tr[1]/td[2]/input")
username.send_keys(usr)
print("Inputted username successfully!")
psw = browser.find_element_by_xpath(
    "/html/body/div[7]/div/div/div[3]/div/div[1]/div/table[1]/tbody/tr[2]/td/div/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td/input")
psw.send_keys(password)
print("Inputted password successfully!")
submit_elem = browser.find_element_by_xpath(
    "/html/body/div[7]/div/div/div[3]/div/div[1]/div/table[1]/tbody/tr[2]/td/div/table/tbody/tr[4]/td[2]/table/tbody/tr/td[1]/button")
submit_elem.click()
print("Successfully logged in.")
print("To start the bot successfully, please navigate to the start screen. The bot will join race itself and do everything, when it's done you'll get further instructions!")
while True:
    speed = pyinputplus.inputMenu(
        ["Slow (1)", "Medium (0.7)", "Normal (0.6)", "Fast (0.5)", "Hacker (0)", "Custom"], numbered=True)
    print("MODE = %s" % (speed))
    if speed == "Slow (1)":
        speed = 1
    elif speed == "Medium (0.7)":
        speed = 0.7
    elif speed == "Normal (0.6)":
        speed = 0.6
    elif speed == "Fast (0.5)":
        speed = 0.5
    elif speed == "Hacker (0)":
        speed = 0
    elif speed == "Custom":
        speed = pyinputplus.inputNum(
            "Input value (can be either integer or floating-point number):\n")
    start_race = browser.find_element_by_css_selector(
        ".mainMenuItem-highlighted > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > a:nth-child(1)")
    start_race.click()
    print("Successfully joined race!")
    time.sleep(3)
    try:
        text = browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[1]/div[2]/table/tbody/tr[2]/td[2]/div/div[1]/div/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[1]')
    except:
        print("An error has occoured since the first word is too small. I don't have time fixing this, restart the program and try again!")
        exit()
    attrs = browser.execute_script(
        "var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;", text)

    first_char = browser.find_element_by_class_name(attrs["class"][:9])

    first_char = first_char.text

    text = browser.find_element_by_xpath(
        '/html/body/div[2]/div/div[1]/div[2]/table/tbody/tr[2]/td[2]/div/div[1]/div/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[2]')

    first_word = first_char + text.text

    text = browser.find_element_by_xpath(
        '/html/body/div[2]/div/div[1]/div[2]/table/tbody/tr[2]/td[2]/div/div[1]/div/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[3]')
    rest = text.text
    full_text = first_word + " " + rest
    full_text_list = full_text.split(" ")
    typing_field = browser.find_element_by_xpath(
        '/html/body/div[2]/div/div[1]/div[2]/table/tbody/tr[2]/td[2]/div/div[1]/div/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/input')

    input("Press enter to start (when the timer hits 0:00)")
    for word in full_text_list:
        if word == "," or word == ".":
            pass
        else:
            word = word + " "
        typing_field.send_keys(word)
        time.sleep(speed)
    print("Done!")
    yes_no = pyinputplus.inputYesNo(
        "Do you want to continue playing (navigate back to the start screen) or stop? (yes/no)")
    if yes_no == "yes":
        continue
    else:
        break

yes_no = pyinputplus.inputYesNo("Do you want to quit Firefox? (yes/no)")
if yes_no == "yes":
    print("Closing... (this might take a second or two)")
    browser.close()
else:
    print("Done, script stopped successfully!")
print("Successfully stopped!")

stuff = {"https://play.typeracer.com/challenge?id=1598206132924guest:135709686540656": "At last the Dodo suddenly called out to the door, staring stupidly up into the way things had happened lately, that Alice had not a VERY good opportunity",
         "https://play.typeracer.com/challenge?id=1598206196352guest:135709686540656": "And so it was all very well to say it over afterwards, it occured to her that she had never done such a very little! Besides, SHE'S she, and I'm sure",
         "https://play.typeracer.com/challenge?id=1598206222116guest:135709686540656": "After a time she found she could not remember ever having seen in her French lesson book. The Mouse gave a sudden leap out of it, and on it except a tiny",
         "https://play.typeracer.com/challenge?id=1598206453986guest:135709686540656": "It was the first sentence in her lessons in the pictures of him while the Dodo suddenly called out The race is over! and they sat down and cried. Alice",
         "https://play.typeracer.com/challenge?id=1598206536366guest:135709686540656": "It was all very well to say it over afterwards, it occurred to her great delight it fitted! Well! throught Alice to herself, as usual. Come, there's no",
         "https://play.typeracer.com/challenge?id=1598206947788guest:130918443275578": "Alice had been anything near the door, staring stupidly up into hers she could see her after the candle is blown out, for she felt that there was hardly",
         "https://play.typeracer.com/challenge?id=1598207086926guest:130918443275578": "There seemed to quiver all over with fright. Oh, I beg your pardon! cried Alice again, for this curious child was very like a frog; and both footmen, Alice",
         "https://play.typeracer.com/challenge?id=1598207878546guest:23128498042694": "Hardy knowing what she was rather glad there WAS no one listening, this time, as it can't possibly make me larger, it must be getting home; the night",
         "https://play.typeracer.com/challenge?id=1598207965583guest:23128498042694": "Lastly, she pictured to herself Now I can creep under the table she opened it, and finding it very nice, it had, in fact, a sort of circle, the exact shape",
         "https://play.typeracer.com/challenge?id=1598208020030guest:23128498042694": "Then they all moved off, and Alice could only hear whispers now and then; such as, that a red hot poker will burn you if you please! This question the",
         "https://play.typeracer.com/challenge?id=1598208074086guest:23128498042694": "Alice throught this must be kind to them, and it'll sit up and beg for its dinner, and all dripping wet, cross, and uncomfortable. As there seemed to be",
         "https://play.typeracer.com/challenge?id=1598208126157guest:23128498042694": "Alice had no idea what Latitude was, or Longitude I've got to come down the chimney! That's quite enough I hope they'll remember her saucer of milk at",
         "https://play.typeracer.com/challenge?id=1598208191109guest:23128498042694": "She drew her foot, slipped, and in that poky little hoise, and have next to no tuys to play croquet, The Frog Footman repeated, in the distance. Either",
         "https://play.typeracer.com/challenge?id=1598208543484guest:277783907471918": "Oh! So Bill's got to do, and in that poky little house, and wondering what to do so alice ventured to taste it, and fortunately was just in time to see",
         "https://play.typeracer.com/challenge?id=1598208609434guest:277783907471918": "Alice thought to herself, after such a capital one for catching mice oh, I beg your acceptance of this sort in her French lesson book. The Mouse did not",
         "https://play.typeracer.com/challenge?id=1598208714280guest:277783907471918": "Alice was soon left alone. Alice laughed so much at this, but at the sides of it, and found in it about four feet high. Soon her eye fell upon a low curtain.",
         "https://play.typeracer.com/challenge?id=1598209049956guest:102797672937362": "Where's the other queer noises, would change to dull reality the grass would be four thousand miles down, I think I can creep under the circumstances.",
         "https://play.typeracer.com/challenge?id=1598209102409guest:102797672937362": "I wish I could shut up like telescopes this time the Mouse was bristling all over, and she is such a very little use without my shoulders. Oh, how I wish",
         "https://play.typeracer.com/challenge?id=1598209162715guest:102797672937362": "There were doors all round the neck of the house! Which was very hot she kept fanning herself all the same, shedding gallons of tears, until there was."}
