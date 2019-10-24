import os
import urllib.request
import logging

logging.basicConfig(level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')

filename = 'data/creditcardfraud.zip'
url = 'https://th-koeln.sciebo.de/s/Rr6anchxnzD4hi0/download'

if not os.path.isfile(filename):
    logging.info("download data ... please wait")
    urllib.request.urlretrieve(url, filename) 
    logging.info("download finished")
else:
    logging.info("data allready exist")

