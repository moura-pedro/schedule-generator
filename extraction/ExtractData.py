"""
Author: Pedro Moura
Year: 2022

"""

from selenium import webdriver

PATH = './chromedriver'
driver = webdriver.Chrome(PATH)

PAGES = 58

def main():
   file = open('data.txt', 'w')
   extractAllData(PAGES, file)


def extractAllData (numOfPages, file):
   for i in range (numOfPages):
      openScheadule (i + 1)
      print("PAGE Visited: " + str(i + 1))

      writeDataInTXT(file, extractDataFromPage())
      

def openScheadule (pageIdx):
   fitURL = "https://apps.fit.edu/schedule/main-campus/fall?query=&page=" + str(pageIdx)
   driver.get(fitURL)


def extractDataFromPage():
   return driver.find_element_by_xpath('//*[@id="course-table"]/tbody').text


def writeDataInTXT(file, data):
   
      for line in data:
         file.write(line)



if __name__ == '__main__':
   main()
