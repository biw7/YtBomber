import time
from tbselenium.tbdriver import TorBrowserDriver
from os.path import dirname, join, realpath, getsize


for i in range (50):
	with TorBrowserDriver("/home/biwxx/Downloads/tor-browser_en-US") as driver:
		driver.load_url('Envidious url here', wait_for_page_body=True)
    		time.sleep(4)
    #play = driver.find_element_by_class_name('autoplay skeleton-light-border-bottom')
    #play.click();
    		play_button = driver.find_element_by_class_name("vjs-poster")
    		play_button.click()
    		time.sleep(20)
    		driver.close();
    
    
