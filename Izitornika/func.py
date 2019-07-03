# coding=utf-8
import selenium
from selenium import webdriver
from time import sleep

class Anketa():
    def __init__(self, username, passw):
        self.bot = webdriver.Chrome()
        self.username = username
        self.password = passw
        self.ime_predmeta = 0
        self.vjezbe = 0
        self.oboje = 0

    def login(self):
        self.bot.get('https://moj.tvz.hr/')
        sleep(2)
        self.bot.find_element_by_xpath('/html/body/div/div/div/div/div/div[2]/form/div[1]/input').send_keys(self.username)
        self.bot.find_element_by_xpath('/html/body/div/div/div/div/div/div[2]/form/div[2]/input').send_keys(self.password)
        self.bot.find_element_by_xpath('/html/body/div/div/div/div/div/div[2]/form/div[3]/button').click()
        sleep(2)

    def crunch_time(self):
        while True:
            ankete = self.bot.find_elements_by_xpath('//button[contains(text(), "Ispuni anketu")]')
            ankete[0].click()
            sleep(2)

            for _ in range (3):
                try:
                    pr = self.bot.find_elements_by_xpath('//button[contains(text(), "predavanja")]')
                    for zx in pr:
                        zx.click()
                        sleep(1)
                except:
                    pass

            for _ in range (3):
                try:
                    vj = self.bot.find_elements_by_xpath('//button[contains(text(), "vježbe")]')
                    for yx in vj:
                        yx.click()
                        sleep(1)
                    sleep(1)
                except:
                    pass

            inputi = self.bot.find_elements_by_xpath("//input[@value='0']")
            for input in inputi:
                input.click()

            sleep(5)
            self.bot.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/form/button[2]').click()
            print('Loop done')
