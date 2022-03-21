from selenium import webdriver
import time


class Fill:

    # Filling the data form
    def __init__(self, addr, price, link):
        PATH = PATH DE SEU CHROME WEBDRIVER

        driver = webdriver.Chrome(PATH)

        driver.get(A URL DE SEU FORM)

        time.sleep(3)

        input_addr = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div['
                                                  '1]/div/div[1]/input')
        input_addr.send_keys(addr)

        input_price = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div['
                                                   '1]/div/div[1]/input')
        input_price.send_keys(price)

        input_link = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div['
                                                  '1]/div/div[1]/input')

        input_link.send_keys(link)

        time.sleep(3)
        send = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
        send.click()