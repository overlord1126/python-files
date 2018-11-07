from urllib import request,parse
from random import choice
import json
import re
import pymysql
import time
from tqdm import tqdm

agent_list = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]

def p(filename,string):
	with open( "%s.html"%filename,"a",encoding="utf-8" ) as f:
		f.write(str( string ))	
		print( "写入%s 完成 .\n\n"%filename )

def loadPage( pageNum ):
	queryString = {
		"extras[]": "activities",
		"geohash": "wtw37qwmsjcj",
		"latitude": 31.193908,
		"limit": 24,
		"longitude": 121.440641,
		"offset": str( 24*pageNum ),
		"terminal": "web"
	}

	ua = {
		"user-agent": choice( agent_list ),
		"cookie":"ubt_ssid=rb5poobto016bec6pe4qz440v1wim6r3_2018-10-29; _utrace=ba425622a0bd847ea2967ea83df294fa_2018-10-29; cna=QhySESuCpx4CAbStnuD9CNYR; track_id=1540804731|adc56f4ae8acf34d6c30d43263bf7b53e3371a51efdfe542a2|8b904edfc927a43042eef9f87b76b4c1; USERID=24375998; SID=octCHOYxmq1B33qMLeFy29u35I99TKB6cNlQ; isg=BB8fJUj9uACtc7wccYZZBSE7rnOjWHyUzKTJh7FsQk4RQDfCrlbWdw5xBtA-WEue"
	}
	# print( ua )
	url = "https://www.ele.me/restapi/shopping/restaurants?" + parse.urlencode( queryString )
	print( "请求获取 第%s页 商家列表: "%pageNum, url ) 
	req = request.Request( url,headers=ua )
	res = json.loads( request.urlopen( req ).read().decode("utf-8") )
	# p(res)

	for shop in res:
	# for shop in res[:2]:
		tempObj = {}
		# 取出商家名字,商家图片,id
		tempObj["name"] = shop["name"]
		tempObj["shopLogo"] = shop["image_path"]	
		tempObj["id"] = shop["id"]		
		shops.append( tempObj )
		# print( "休息 2s后 爬取下一家" )
		# time.sleep( 2 )
		# 获取该商家的 菜品信息
		getMenus( shop["id"] )

def getMenus( shopId ):
	ua = {
		"user-agent": choice( agent_list ),
		"cookie":"ubt_ssid=rb5poobto016bec6pe4qz440v1wim6r3_2018-10-29; _utrace=ba425622a0bd847ea2967ea83df294fa_2018-10-29; cna=QhySESuCpx4CAbStnuD9CNYR; track_id=1540804731|adc56f4ae8acf34d6c30d43263bf7b53e3371a51efdfe542a2|8b904edfc927a43042eef9f87b76b4c1; USERID=24375998; SID=octCHOYxmq1B33qMLeFy29u35I99TKB6cNlQ; isg=BB8fJUj9uACtc7wccYZZBSE7rnOjWHyUzKTJh7FsQk4RQDfCrlbWdw5xBtA-WEue"
	}
	print( ua )
	url = "https://www.ele.me/restapi/shopping/v2/menu?restaurant_id=%s&terminal=web"%shopId
	req = request.Request( url,headers=ua )
	res = json.loads( request.urlopen( req ).read().decode("utf-8") )
	for menu in res:
		for food in menu["foods"] :
			tempFood = {}
			tempFood["item_id"] = food["item_id"]
			tempFood["name"] = food["name"]
			tempFood["restaurant_id"] = food["restaurant_id"]
			tempFood["rating"] = food["rating"]
			tempFood["rating_count"] = food["rating_count"]
			tempFood["satisfy_count"] = food["satisfy_count"]
			tempFood["satisfy_rate"] = food["satisfy_rate"]
			tempFood["photos"] = food["photos"]
			tempFood["original_price"] = food["specfoods"][0]["original_price"]
			tempFood["price"] = food["specfoods"][0]["price"]
			tempFood["sold_out"] = food["specfoods"][0]["sold_out"]
			tempFood["month_sales"] = food["month_sales"]
			menus.append( tempFood )

# 初始化
shops = []
shopsNum = 0
errShopsNum = 0
menus = []
menusNum = 0
errmenusNum = 0

start = int( input( "请输入开始页: " ) )
length = int( input( "请输入爬取长度(一页24条): " )  )

# 爬取
print( "开始爬取..." )
for i in range(start,start+length) :
	loadPage( i )
	# print( "休息 10s后,爬取下一页" )
	# time.sleep( 10 )
# p( "1",menus )
print( "爬取结束..." )

db = pymysql.connect(host="localhost", user="root", password="123456", db="myele2", charset="utf8mb4")
print( "连接数据库成功...." )
cursor = db.cursor()  # 创建一个游标对象

# 写入 商家
cursor.execute("DROP TABLE IF EXISTS shop")  # 如果表存在则删除
# 创建表sql语句
createTab = """create table shop(
		id int primary key auto_increment,
		shop_id varchar(50),
		name varchar(100) not null,
		shopLogo varchar(200) not null
		) CHARSET=utf8;"""
cursor.execute(createTab)  # 执行创建数据表操作
print( "创建 商家表成功...." )

print( "开始写入商家信息" )
sql = "INSERT INTO `shop`(`shop_id`,`name`,`shopLogo`) VALUES(%s,%s,%s)"
for shop in tqdm(shops):
	try:
		cursor.execute(sql, ( shop["id"],shop["name"],shop["shopLogo"] ))
		db.commit()
		# print("写入商家成功")
		shopsNum += 1
	except:
		p("失败商家",shop["name"])
		errShopsNum += 1
		db.rollback()

# 写入商品
cursor.execute("DROP TABLE IF EXISTS menus")  # 如果表存在则删除
# 创建表sql语句
createTab = """create table menus(
		id int primary key auto_increment,
		item_id varchar(50),
		name varchar(100) not null,
		restaurant_id varchar(50), 
		photos varchar(2000),
		rating float,
		satisfy_rate float,
		rating_count int,
		satisfy_count int,
		original_price float,
		price float,
		sold_out tinyint,
		month_sales int
		) CHARSET=utf8;"""
cursor.execute(createTab)  # 执行创建数据表操作
print( "创建 菜品表 成功...." )
sql = "INSERT INTO `menus`(`item_id`,`name`,`restaurant_id`,`photos`,`rating`,`satisfy_rate`,`rating_count`,`satisfy_count`,`original_price`,`price`,`sold_out`,`month_sales`) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
for menu in tqdm(menus):
	try:
		cursor.execute(sql, ( menu["item_id"],menu["name"],menu["restaurant_id"],str(menu["photos"]),menu["rating"],menu["satisfy_rate"],menu["rating_count"],menu["satisfy_count"],menu["original_price"],menu["price"],menu["sold_out"],menu["month_sales"] ))
		db.commit()
		# print("写入菜品成功")
		menusNum += 1
	except:
		p("失败菜品",menu["name"])
		errmenusNum += 1
		db.rollback()
db.close()
print( '''
数据库写入结束...
	成功写入商家 %s 家,
	失败 %s 家,

	成功写入菜品 %s ,
	失败 %s,
''' %( shopsNum,errShopsNum,menusNum,errmenusNum ))
  


