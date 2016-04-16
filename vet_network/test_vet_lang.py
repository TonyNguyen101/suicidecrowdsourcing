import requests
import bs4
import json
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError, CollectionInvalid
import datetime as dt
import Twython

db_cilent = MongoClient()




veteran_buzzwords = ['veteran', 'force', 'specialforces', 'weaponsmaniac'
'navy', 'marine', 'airforce', 'weaponsdialy', 'army', 'veteransday'
'weapon'  ,'gun'  ,'weapons'  ,'soldier'  ,'weaponsfanatics'  ,'military'
'marines'  ,'guns'  ,'navylife'  ,'proudusa'  ,'veteransday2015'  ,'hooah'
'veterandaughters'  ,'usnavysailor'  ,'armylife'  ,'veterandaughter'
'veteranspark'  ,'americanpatriots'  ,'armytshirt'  ,'veteran'  ,'veteranday', 'armystrong' , 'armydad' , 'veterangrandpa' , 'usarmy' , 'usnavyseals' , 'armyveteranfamily' , 'usnavy' , 'veteranos' , 'semperfi' , 'americanveterans' , 'veteransupport' , 'usarmyvet' , 'proudforveterans' ,
'goarmy' , 'armyveteran' , 'uscg' , 'armyvet' , 'usmc' , 'militaryvet' ,
'navyveteran' , 'america' , 'usa' , 'coastguard' , 'veteranwife' , 'americanveteran' ,
'proudveteran' , 'navyvet' , 'veterans' , 'congrats' , 'washingtonmemorial']
