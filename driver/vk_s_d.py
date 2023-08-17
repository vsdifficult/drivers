from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 

import sys

class vkP(): 

    def __init__(self, page) -> None:
        self.page = page 
        
        if page is None: 
            print('You must write a https://vk.com')  
            sys.exit()
        
        elif page is "https://vk.com": 
            print('Starting')
        
        else:  
            sys.exit()

    
    def commentV(self, post_id, your_vk_login, your_vk_pass):  
        post_id = self.page_post_id
        driver_selen = webdriver.Chrome("./driverpath.exe")
        driver_selen.get(self.page) 
        username = driver_selen.find_element(By.ID, 'email') 
        password = driver_selen.find_element(By.ID, 'password') 
        username.send_keys(your_vk_login) 
        password.send_keys(your_vk_pass) 
        driver_selen.find_element(By.ID, 'login_button').click() 

        driver_selen.get(f"https://vk.com/{post_id}") 

        try: 
            comments = driver_selen.find_element(By.CLASS_NAME, 'reply_table') 
            for comm in comments: 
                print(comm)
        except ConnectionError as e: 
            return e
