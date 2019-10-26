from selenium.common.exceptions import NoSuchElementException as SelNoEl
from selenium import webdriver
from time import sleep
import selenium
import sys

class Anketa():
    def __init__(self, username, passw):
        self.bot = webdriver.Chrome()
        self.username = username
        self.password = passw

    def login(self):
        self.bot.get('https://moj.tvz.hr/')
        sleep(2)
        self.bot.find_element_by_xpath('/html/body/div/div/div/div/div/div[2]/form/div[1]/input').send_keys(self.username)
        self.bot.find_element_by_xpath('/html/body/div/div/div/div/div/div[2]/form/div[2]/input').send_keys(self.password)
        self.bot.find_element_by_xpath('/html/body/div/div/div/div/div/div[2]/form/div[3]/button').click()
        sleep(2)

    def crunch_time(self):
        try:
            ankete = self.bot.find_elements_by_xpath('//button[contains(text(), "Ispuni anketu")]')
            ankete[0].click()
            sleep(2)
        except (SelNoEl, IndexError):
            print('Anketa gotova')
            sys.exit()

        while True:
            pr = self.bot.find_elements_by_xpath('//button[contains(text(), "predavanja")]')
            for _ in range (len(pr)):
                try:
                    pr[_].click()
                    sleep(1)
                except:
                    pass

            vj = self.bot.find_elements_by_xpath('//button[contains(text(), "vježbe")]')
            for _ in range (len(vj)):
                try:
                    vj[_].click()
                    sleep(1)
                except:
                    pass

            nemrem = self.bot.find_elements_by_xpath("//input[@value='0']")
            for _ in nemrem:
                _.click()

            sleep(5)
            self.bot.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/form/button[2]').click()
            print('+1 done')


        #  STARI NACIN
        # while True:
            # sleep(2)
            # ankete = self.bot.find_elements_by_xpath('//button[contains(text(), "Ispuni anketu")]')
            # ankete[0].click()
            # sleep(2)
        #     for _ in range (7):
        #         try:
        #             pr = self.bot.find_elements_by_xpath('//button[contains(text(), "predavanja")]')
        #             for _ in pr:
        #                 _.click()
        #                 sleep(1)
        #         except:
        #             pass
        #
        #     for _ in range (7):
        #         try:
        #             vj = self.bot.find_elements_by_xpath('//button[contains(text(), "vježbe")]')
        #             for _ in vj:
        #                 _.click()
        #                 sleep(1)
        #         except:
        #             pass
        #
        #     nemrem = self.bot.find_elements_by_xpath("//input[@value='0']")
        #     for _ in nemrem:
        #         _.click()
        #
        #     sleep(5)
        #     self.bot.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/form/button[2]').click()
        #     print('+1 done')
