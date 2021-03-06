# coding=utf-8
"""
Auteur: Bruno DELATTRE
Date : 12/08/2016
"""

import scapperRTL
import scraperBBC
import scraperFranceCulture
import scraperFranceInter
from lib import com_config, com_logger

conf = com_config.Config()
conf.setconfig()
config = conf.getconfig()

logger = com_logger.Logger('Main')
logger.info(config['APPLICATION']['name'] + ' ' + config['APPLICATION']['version'])
logger.info('Start')

# Scrap !   INFO: soup.findall(attrs={'class':None or value})
fc = scraperFranceCulture.FranceCulture()
fc.scrapxml()

fi = scraperFranceInter.FranceInter()
fi.scrapxml()

bbc = scraperBBC.BBC()
bbc.scrap()

rtl = scapperRTL.RTL()
rtl.scrapxml()

logger.info('Stop')
