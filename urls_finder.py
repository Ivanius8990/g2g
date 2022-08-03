import sqlite3


conn = sqlite3.connect('servers.db')
cur = conn.cursor()

####функция удаления ненужных символов
def name_replace(name):
    encode_name = name.encode("ascii", "ignore").decode()  ###удаление русских символов
    simb = '[] ()-'  ###символы которые надо удалить
    for char in simb:
        encode_name = encode_name.replace(char, '')
    return encode_name
###функция возвращает короткий номер сервера
def serv_ind(serv):
    id=serv[serv.find("lgc_")+4:]
    id=id[:id.find('_')]
    return id

url_list = []
cur.execute("""SELECT * from servers_WOW""")
records = cur.fetchall()
for row in records:
    serv_name=row[1]
    reg=row[2]
    serv_index= row[3]
    url='https://www.g2g.com/offer/'+name_replace(serv_name)+'?service_id=lgc_service_1&brand_id=lgc_game_'+\
        serv_ind(serv_index)+'&'+reg+'&'+serv_index+'&sort=lowest_price&include_offline=1'
    url_list.append(url)
cur.close()


print(url_list)
print(len(url_list))