from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from tkinter import *

window = Tk()
window.title("Ennn Ucuzunu Bul")

product=Label(text="enter product name :")
product.grid(row=0,column=1)

product_entry=Entry()
product_entry.grid(row=0,column=2)

result_label=Label(text="enter")
result_label.grid(row=2,column=1)


def enucuzunubul():
    driver = webdriver.Edge()
    driver.minimize_window()
    driver.get("https://www.google.com")

    WebDriverWait(driver,4).until(expected_conditions.visibility_of_element_located((By.NAME,"q")))
    input_element_by_name = driver.find_element(By.NAME,"q")

    input_element_by_name.send_keys(product_entry.get())

    WebDriverWait(driver,4).until(expected_conditions.visibility_of_element_located((By.NAME,"btnK")))
    search_button=driver.find_element(By.NAME,"btnK")

    WebDriverWait(driver,4).until(expected_conditions.element_to_be_clickable((By.NAME,"btnK")))
    search_button.click()

    WebDriverWait(driver,4).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME,"LatpMc")))
    shop_button=driver.find_element(By.CLASS_NAME,"LatpMc")

    WebDriverWait(driver,4).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME,"LatpMc")))
    shop_button.click()

    WebDriverWait(driver,4).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME,"iXEZD")))
    prices=driver.find_element(By.CLASS_NAME,"iXEZD")
    WebDriverWait(driver,4).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME,"iXEZD")))
    prices.click()

    WebDriverWait(driver,20).until(expected_conditions.visibility_of_element_located((By.ID,"sh-osd__online-sellers-cont")))
    producs_list=driver.find_element(By.ID,"sh-osd__online-sellers-cont")
    #print(producs_list.text)
    result_label.config(text=(producs_list.text))

show_prices_button=Button(text=f"find the cheapest prices for {product_entry}",command=enucuzunubul)
show_prices_button.grid(row=1,column=1)

window.mainloop()





