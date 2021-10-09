import gspread
import datetime
time = datetime.datetime.now()

cloud = gspread.service_account(filename='./config/gkt.json')
excel = cloud.open('cuybot-discord-request').sheet1

def insert(sender, request):
    save = excel.append_row([str(sender), str(request), str(time)])
    return save