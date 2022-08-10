import sqlite3


conn = sqlite3.connect('prices_g2g.db')
cur = conn.cursor()

conn2 = sqlite3.connect('prices_funpay.db')
cur2 = conn2.cursor()

reg='US'### азвание региона

conn3 = sqlite3.connect('prices_all.db')
cur3 = conn3.cursor()
cur3.execute("""CREATE TABLE IF NOT EXISTS all_prices(
   name TEXT,
   name1 TEXT,
   prise1 TEXT,
   prise2 TEXT);
""")
gg_list=[]
cur.execute("""SELECT * from prices_WOW_g2g""")
records = cur.fetchall()
for row in records:
    g_list=[]
    g_list.append(row[0])
    g_list.append(row[1])
    g_list.append(row[3])
    g_list.append(row[4])
    gg_list.append(g_list)
print(gg_list)

fp_list=[]
cur2.execute("""SELECT * from prices_WOW_US_funpay""")
records2 = cur2.fetchall()
for row in records2:
    f_list=[]
    f_list.append(row[0])
    f_list.append(row[1])
    f_list.append(row[3])
    f_list.append(row[4])
    fp_list.append(f_list)
print(fp_list)
hh=[]
h=[]
for i in range(len(gg_list)):
    if gg_list[i][0].find(reg) != -1:
        for j in range(len(fp_list)):
            name = gg_list[i][1].find(fp_list[j][0])
            rassa = gg_list[i][1].find(fp_list[j][1])
            hh = []
            if name != -1 and rassa != -1 and float(fp_list[j][2]) >= float(gg_list[i][2]) * 1.4:
                hh.append(fp_list[j][0] + ' ' + fp_list[j][1])
                hh.append(gg_list[i][1])
                hh.append(fp_list[j][2])
                hh.append(gg_list[i][2])
                h.append(hh)

for z in h:
    print(z)
    cur3 = conn3.cursor()
    cur3.execute("REPLACE INTO all_prices VALUES(?, ?, ?, ?);", z)
    conn3.commit()
