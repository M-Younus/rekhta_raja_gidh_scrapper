# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 19:58:56 2019

@author: MY
"""
#%%
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
#%%
browser=webdriver.Chrome('chromedriver.exe')

#%%
link='https://www.rekhta.org/ebooks/raja-gidh-bano-qudsiya-ebooks'

#%%
browser.get(link)

#%%
print(browser.title)

#%%

browser.save_screenshot('all_images\\0.png')
for i in range(1,559):
    browser.find_element_by_class_name('ebookprev').click()
    sleep(5)
    while(1):
        try:
            print('in')
            browser.find_element_by_id('activeAfterZoom')
            browser.save_screenshot(f'all_images\\{i}.png')
            break
        except:
            continue
    

#%%