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

def gacha_insert(id, number):
    gacha.append_row([str(id), number])

def gacha_find(id):
    cell = gacha.find(id)
    return cell

def gacha_tebak(id):
    cell = gacha_find(id)
    if cell != None:
        val = gacha.cell(cell.row, 2)
        return val.value

def gacha_tebak1(id, number):
    num_rows = gacha.row_count - 1
    curr_row = 0
    arr = []

    while curr_row < num_rows:
        try:
            curr_row += 1
            row = gacha.row_values(curr_row)
            arr.append(row)
            # return (row and (id in row) and (number in row))
        except IndexError:
            pass
    
    print(arr)
            # print(number in row)
            # print(id in row)

    # return 'hai'

    # return cell.get_all_values()
    # <class 'list'>
    # if cell != None:
    #     if id in cell:
    #         print(cell[1])
    #         return cell[1]

        # print(type(cell))
        # return type(cell)
        # for (row, col) in cell:
        #     return row
        # val = gacha.cell(cell.row, 2)
        # return val
    # return cell
    # if cell != None:
    #     return gacha.cell(cell.row, 2)
        # val = reputation.cell(cell.row, 2)
        # return val.value



# def gacha_unique(id):
#     member = gacha_find(id)
#     if member != None:
#     return member
    # return (number != None)

    # if cell != None:
    #     val = gacha.cell(cell.row, 2)
    #     return val.value
        
        # bikin aja, yang gacha disini aja langsung

        # knp mantap kan? o