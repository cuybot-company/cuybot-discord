import gspread
import datetime
time = datetime.datetime.now()

cloud = gspread.service_account(filename='./config/gkt.json')
excel = cloud.open('cuybot-discord-request').sheet1
reputation = cloud.open('cuybot-discord-request').get_worksheet(1) # gspread only implement sheet1 so do it manually
def insert(sender, request):
    save = excel.append_row([str(sender), str(request), str(time)])
    return save
def reputation_insert(id):
    reputation.append_row([str(id), '0'])
def reputation_find(id):
    cell = reputation.find(id)
    return cell
def reputation_value(id):
    cell = reputation_find(id)
    if cell != None:
        val = reputation.cell(cell.row, 2)
        return val.value
    else:
        return '0'
def reputation_update(id, option):
    cell = reputation_find(id)
    value = reputation_value(id)
    if option == 'add':
        reputation.update_cell(cell.row, 2, str(int(value) + 1))
    elif option == 'reduce':
        reputation.update_cell(cell.row, 2, str(int(value) - 1))