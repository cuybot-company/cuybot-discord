import os, gspread, datetime
import helper.constants as c
time = datetime.datetime.now()

credential = c.request_g_credentials

gcloud_connect = gspread.service_account_from_dict(credential)
gsheet = gcloud_connect.open(os.getenv('GSHEET_PROJECT_NAME')).sheet1

def insert(sender, request):
    save_data = gsheet.append_row([str(sender), str(request), str(time)])
    return save_data
