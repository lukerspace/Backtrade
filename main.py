from scrape_tool import *
# try:


scraper = IndexScraper()
scraper.set_index_ticker('ark')
scraper.start()

scraper.set_index_ticker('qqq')
scraper.start()

scraper.set_index_ticker('spy')
scraper.start()


# # except:
#     pass