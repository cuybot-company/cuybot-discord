import gspread
import datetime
time = datetime.datetime.now()

cloud = gspread.service_account(filename='./config/gkt.json')
excel = cloud.open('cuybot-discord-request').sheet1
reputation = cloud.open('cuybot-discord-request').get_worksheet(1) # gspread only implement sheet1 so do it manually
reward = cloud.open('cuybot-discord-request').get_worksheet(2)
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
def reputation_update(id, point):
    cell = reputation_find(id)
    value = reputation_value(id)
    reputation.update_cell(cell.row, 2, str(int(value) + point))


def reward_insert(id, num):
    reward.append_row([str(id), num])
def reward_find(id):
    cell = reward.find(str(id))
    return cell
def reward_value(id):
    cell = reward_find(id)
    if cell != None:
        val = reward.cell(cell.row, 2)
        return val.value
def reward_check(id):
    cell = reward.find(id)
    if cell != None:
        val = reward.cell(cell.row, 2)
        return val.value
    else:
        return '0'
