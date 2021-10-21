import gspread
import datetime
time = datetime.datetime.now()

# name_exel = 'cuybot-discord-request'
name_exel = 'discord-test'
cloud = gspread.service_account(filename='./config/gkt.json')

excel = cloud.open(name_exel).sheet1
reputation = cloud.open(name_exel).get_worksheet(1) # gspread only implement sheet1 so do it manually
gacha = cloud.open(name_exel).get_worksheet(3)

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

def gacha_insert(id, number):
    gacha.append_row([str(id), number])

def gacha_find(id):
    cell = gacha.find(id)
    return cell

def gacha_tebak(id, number):
    num_rows = gacha.row_count - 1
    curr_row = 0
    arr = []

    while curr_row < num_rows:
        try:
            curr_row += 1
            row = gacha.row_values(curr_row)
            arr.append(row)
        except IndexError:
            break
    
    id_check = any(id in id_list for id_list in arr)
    number_check = any(number in number_list for number_list in arr)

    return (id_check and number_check)