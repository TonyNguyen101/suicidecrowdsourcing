import requests
import bs4
import json
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError, CollectionInvalid
import datetime as dt
import Twython

db_cilent = MongoClient()


t = Twython(app_key='viFcnMBuuVEEACYk8uHVJFxGl',
   app_secret='EoDGnIUQ316VbzaMt3nfcvwj4qnhpz8RyWWgyO28LF4HMFbHTu',
   oauth_token='67738036-SM5J8ZMIqXTYkhLfcnrBphP4Y7QbUITZwZ6IWxsF0',
   oauth_token_secret='FNaXS2d7JvdY4GLOMXHqWHR7iIMU10GR94GUmafBBClXn')



geo_enabled = True, 'country_code' = 'US'

t.lookup_status(id=432656548536401920)


veteran_buzzwords = ['veteran', 'force', 'specialforces', 'weaponsmaniac'
'navy', 'marine', 'airforce', 'weaponsdialy', 'army', 'veteransday'
'weapon'  ,'gun'  ,'weapons'  ,'soldier'  ,'weaponsfanatics'  ,'military'
'marines'  ,'guns'  ,'navylife'  ,'proudusa'  ,'veteransday2015'  ,'hooah'
'veterandaughters'  ,'usnavysailor'  ,'armylife'  ,'veterandaughter'
'veteranspark'  ,'americanpatriots'  ,'armytshirt'  ,'veteran'  ,'veteranday', 'armystrong' , 'armydad' , 'veterangrandpa' , 'usarmy' , 'usnavyseals' , 'armyveteranfamily' , 'usnavy' , 'veteranos' , 'semperfi' , 'americanveterans' , 'veteransupport' , 'usarmyvet' , 'proudforveterans' ,
'goarmy' , 'armyveteran' , 'uscg' , 'armyvet' , 'usmc' , 'militaryvet' ,
'navyveteran' , 'america' , 'usa' , 'coastguard' , 'veteranwife' , 'americanveteran' ,
'proudveteran' , 'navyvet' , 'veterans' , 'congrats' , 'washingtonmemorial']
