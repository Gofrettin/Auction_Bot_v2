from datetime import datetime
import json
import os

# Daten für Froststoff sind leider buggy 300g und mehr pro Item...

def process_scan_folder(path):
    files = os.listdir(path)

    for filename in files:
        process_auc_scan(path + filename)
    return


def process_auc_scan(scan_file, debbuging=False):
    file = open(scan_file, "r", encoding='UTF-8')
    print("Opening " + str(scan_file))

    set_start_time = False
    start_time = ''

    data = []

    for line in file:
        if "startTime" in line and set_start_time == False:
            start_time = str(datetime.utcfromtimestamp(int(line[22:-2])).strftime('%Y_%m_%d_%H_%M_%S'))
            print(start_time)
            set_start_time = True

        if "\"return {{" in line:
            raw_items = line.split("},{")
            for element in raw_items:
                raw_item = element.split(",")
                for part in raw_item:
                    if part.startswith(' '):
                        raw_item.remove(part)

                item_class = raw_item[2][2:-2]
                item_category = raw_item[3][2:-2]
                item_name = raw_item[8][2:-2]
                item_seller = raw_item[19][2:-2]
                item_amount = int(raw_item[10])
                item_bid_price = int(raw_item[14]) / (100 * 100)
                item_sell_price = int(raw_item[16]) / (100 * 100)
                item_sell_price_per_unit = item_sell_price / item_amount
                item_id = raw_item[11]

                item_dict = {
                    'name': item_name,
                    'class': item_class,
                    'category': item_category,
                    'seller': item_seller,
                    'amount': item_amount,
                    'sell price': item_sell_price,
                    'price per unit': item_sell_price_per_unit,
                    'date': start_time
                }

                data.append(item_dict)
        with open('C:/Users/Mikey/PycharmProjects/AuctionBot_v2/processed_data/' + start_time + '_data.json', 'w', encoding='UTF-8') as outfile:
            json.dump(data, outfile, indent=4)

            if debbuging:
                # print(item_class)
                # print(item_category)
                # print(item_name)
                # print(item_seller)
                # print(item_amount)
                # print(item_bid_price)
                # print(item_sell_price)
                for i in range(len(raw_item)):
                    print(raw_item[i])
                # exit()
    return
