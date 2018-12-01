from azure.storage.table import TableService, Entity
import urllib, json

azurestorageaccount = '<storage account name>'
azurestoragekey = '<storage account key>'
scoreboardurl = 'http://localhost/scoreboard/score'
timeclockurl = 'http://localhost/timeclock/time'
partitionkey= 'DeKorf'

table_service = TableService(account_name=azurestorageaccount, account_key=azurestoragekey)

response = urllib.urlopen(scoreboardurl)
data = json.loads(response.read())
print data

table_service.insert_or_replace_entity('score', partitionkey, '1', data)

response = urllib.urlopen(timeclockurl)
data = json.loads(response.read())
print data

table_service.insert_or_replace_entity('time', partitionkey, '1', data)

