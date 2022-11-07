import json
from flask import Flask, render_template, request, jsonify
import pymysql
import time as tm
app = Flask(__name__)


@app.route('/')                                     # 请求首页接口
def index():
   return render_template('index.html')


@app.route('/xdf')                                  # 请求首页接口
def xdf():
   return render_template('xdf.html')

 
@app.route('/input', methods=['GET', 'POST'])       # 输入单词接口 
def input():
   if request.method == 'GET':
        return render_template('input.html')

   if request.method == 'POST':
        word = request.form['word']
        chinese = request.form['chinese']
        timeNum = int(round(tm.time() * 1000))
        time = tm.strftime('%Y-%m-%d %H:%M:%S',tm.localtime(timeNum/1000))

        conn = pymysql.connect(host='127.0.0.1', user='root', password='', db='ietls', port=3306, charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

        sql = "INSERT INTO test (word, chinese, time) VALUES (%s, %s, %s)"
        cursor.execute(sql, (word, chinese, time))
        conn.commit()

        cursor.close()
        conn.close()

        return render_template('input.html')

 
@app.route('/importWordXdf', methods=['GET', 'POST'])       # 输入单词接口 
def importWordXdf():
   if request.method == 'GET':
        return render_template('importWordXdf.html')

   if request.method == 'POST':
        word = request.form['word']
        word = word.split("\r\n")
        for i in range(0, len(word)):
            word[i] = word[i].split(",")
        english = []
        chinese = []
        for i in range(0,len(word)):
            english.append(word[i][0])
            chinese.append(word[i][1])
        print(english)
        print(chinese)
        timeNum = int(round(tm.time() * 1000))
        time = tm.strftime('%Y-%m-%d %H:%M:%S',tm.localtime(timeNum/1000))

        conn = pymysql.connect(host='127.0.0.1', user='root', password='', db='ietls', port=3306, charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

        for i in range(0,len(word)):
            sql = "INSERT INTO xdf (word, chinese, time) VALUES (%s, %s, %s)"
            cursor.execute(sql, (english[i], chinese[i], time))
            conn.commit()

        cursor.close()
        conn.close()

        return render_template('importWordXdf.html')

 
@app.route('/inputXdf', methods=['GET', 'POST'])       # 输入单词接口 
def inputXdf():
   if request.method == 'GET':
        return render_template('inputXdf.html')

   if request.method == 'POST':
        word = request.form['word']
        chinese = request.form['chinese']
        timeNum = int(round(tm.time() * 1000))
        time = tm.strftime('%Y-%m-%d %H:%M:%S',tm.localtime(timeNum/1000))

        conn = pymysql.connect(host='127.0.0.1', user='root', password='', db='ietls', port=3306, charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

        sql = "INSERT INTO xdf (word, chinese, time) VALUES (%s, %s, %s)"
        cursor.execute(sql, (word, chinese, time))
        conn.commit()

        cursor.close()
        conn.close()

        return render_template('inputXdf.html')


@app.route('/wordbase', methods=['GET', 'POST'])    # 词库查询接口
def wordbase():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='', db='ietls', port=3306, charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    sql = "SELECT * FROM test order by id desc"
    cursor.execute(sql)
    data_list = cursor.fetchall()
    time_list = []
    for i in range(0, len(data_list)):
        time_all = data_list[i]['time']
        time_less = time_all[5:10]
        time_list.append(time_less)
    for i in range(0, len(time_list)):
        data_list[i]['time'] = time_list[i]
    # print(data_list)
    wordNum = len(data_list)

    cursor.close()
    conn.close()

    return render_template('wordbase.html', data_list=data_list, wordNum=wordNum)


@app.route('/wordbaseXdf', methods=['GET', 'POST'])    # 词库查询接口
def wordbaseXdf():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='', db='ietls', port=3306, charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    sql = "SELECT * FROM xdf order by id desc"
    cursor.execute(sql)
    data_list = cursor.fetchall()
    time_list = []
    for i in range(0, len(data_list)):
        time_all = data_list[i]['time']
        time_less = time_all[5:10]
        time_list.append(time_less)
    for i in range(0, len(time_list)):
        data_list[i]['time'] = time_list[i]
    # print(data_list)
    wordNum = len(data_list)

    cursor.close()
    conn.close()

    return render_template('wordbaseXdf.html', data_list=data_list, wordNum=wordNum)


@app.route('/starWords', methods=['GET', 'POST'])   # 查询星标词汇接口
def starWords():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='', db='ietls', port=3306, charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    sql = "SELECT * FROM test where star = 1 order by id desc"
    cursor.execute(sql)
    data_list = cursor.fetchall()
    time_list = []
    for i in range(0, len(data_list)):
        time_all = data_list[i]['time']
        time_less = time_all[5:10]
        time_list.append(time_less)
    for i in range(0, len(time_list)):
        data_list[i]['time'] = time_list[i]
    # print(data_list)
    wordNum = len(data_list)

    cursor.close()
    conn.close()

    return render_template('starWords.html', data_list=data_list, wordNum=wordNum)


@app.route('/starWordsXdf', methods=['GET', 'POST'])   # 查询星标词汇接口
def starWordsXdf():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='', db='ietls', port=3306, charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    sql = "SELECT * FROM xdf where star = 1 order by id desc"
    cursor.execute(sql)
    data_list = cursor.fetchall()
    time_list = []
    for i in range(0, len(data_list)):
        time_all = data_list[i]['time']
        time_less = time_all[5:10]
        time_list.append(time_less)
    for i in range(0, len(time_list)):
        data_list[i]['time'] = time_list[i]
    # print(data_list)
    wordNum = len(data_list)

    cursor.close()
    conn.close()

    return render_template('starWordsXdf.html', data_list=data_list, wordNum=wordNum)


@app.route('/reciteOrder', methods=['GET', 'POST']) # 顺序背单词请求接口
def reciteOrder():
    if request.method == 'GET':
        conn = pymysql.connect(host='127.0.0.1', user='root',
                               password='', db='ietls', port=3306, charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    sql = "SELECT * FROM test order by id desc"
    cursor.execute(sql)
    data_list = cursor.fetchall()
    listLenth = len(data_list)-1
    cursor.close()
    conn.close()
    return render_template('reciteOrder.html',listLenth=listLenth)


@app.route('/reciteStar', methods=['GET', 'POST']) # 背星标单词请求接口
def reciteStar():
    if request.method == 'GET':
        conn = pymysql.connect(host='127.0.0.1', user='root',
                               password='', db='ietls', port=3306, charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    sql = "SELECT * FROM test where star=1 order by id desc"
    cursor.execute(sql)
    data_list3 = cursor.fetchall()
    listLenth = len(data_list3)-1
    cursor.close()
    conn.close()
    return render_template('reciteStar.html',listLenth=listLenth)


@app.route('/reciteRand', methods=['GET', 'POST'])  # 乱序背单词请求接口
def reciteRand():
    if request.method == 'GET':
        conn = pymysql.connect(host='127.0.0.1', user='root',
                               password='', db='ietls', port=3306, charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    sql = "select * from test order by rand()"
    cursor.execute(sql)
    data_list2 = cursor.fetchall()
    listLenth = len(data_list2)-1
    cursor.close()
    conn.close()
    return render_template('reciteRand.html',listLenth=listLenth)


@app.route('/reciteOrderXdf', methods=['GET', 'POST']) # 顺序背单词请求接口
def reciteOrderXdf():
    if request.method == 'GET':
        conn = pymysql.connect(host='127.0.0.1', user='root',
                               password='', db='ietls', port=3306, charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    sql = "SELECT * FROM xdf order by id desc"
    cursor.execute(sql)
    data_list = cursor.fetchall()
    listLenth = len(data_list)-1
    cursor.close()
    conn.close()
    return render_template('reciteOrderXdf.html',listLenth=listLenth)


@app.route('/reciteStarXdf', methods=['GET', 'POST']) # 背星标单词请求接口
def reciteStarXdf():
    if request.method == 'GET':
        conn = pymysql.connect(host='127.0.0.1', user='root',
                               password='', db='ietls', port=3306, charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    sql = "SELECT * FROM xdf where star=1 order by id desc"
    cursor.execute(sql)
    data_list3 = cursor.fetchall()
    listLenth = len(data_list3)-1
    cursor.close()
    conn.close()
    return render_template('reciteStarXdf.html',listLenth=listLenth)


@app.route('/reciteRandXdf', methods=['GET', 'POST'])  # 乱序背单词请求接口
def reciteRandXdf():
    if request.method == 'GET':
        conn = pymysql.connect(host='127.0.0.1', user='root',
                               password='', db='ietls', port=3306, charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    sql = "select * from xdf order by rand()"
    cursor.execute(sql)
    data_list2 = cursor.fetchall()
    listLenth = len(data_list2)-1
    cursor.close()
    conn.close()
    return render_template('reciteRandXdf.html',listLenth=listLenth)


# 两个varchar  一个int
@app.route('/update', methods=['GET', 'POST'])      # 更新当日背单词任务接口
def update():
    if request.method == 'GET':
        for i in range(0, 366):
            conn = pymysql.connect(host='127.0.0.1', user='root', password='', db='ietls', port=3306, charset='utf8')
            cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
            sql = "INSERT INTO punch (date,status,num) values (%s, %s, %s);"
            cursor.execute(sql, (i, '0', 0))
            conn.commit()
            cursor.close()
            conn.close()

    return render_template('recite.html')


@app.route('/recitepost', methods=['GET', 'POST'])  # 背单词查询接口
def recitepost():
    if request.method == 'POST':
        indexNum = int(request.form['indexNum'])

        conn = pymysql.connect(host='127.0.0.1', user='root',
                               password='', db='ietls', port=3306, charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

        sql = "SELECT * FROM test LIMIT %s,1;"
        cursor.execute(sql, indexNum)
        conn.commit()

        cursor.close()
        conn.close()
        word_list = cursor.fetchall()
        list = word_list[0]
        getId = list['id']
        getWord = list['word']
        getChinese = list['chinese']
        getTime = list['time']
        getTime = getTime[5:10]
        getStar = list['star']
        json_dict = {
            'id': getId,
            'word': getWord,
            'time': getTime,
            'chinese': getChinese,
            'star': getStar
        }
        json_dict = json.dumps(json_dict)

        return jsonify(json_dict)


@app.route('/recitepostStar', methods=['GET', 'POST'])  # 背单词查询接口
def recitepostStar():
    if request.method == 'POST':
        indexNum = int(request.form['indexNum'])

        conn = pymysql.connect(host='127.0.0.1', user='root',
                               password='', db='ietls', port=3306, charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

        sql = "SELECT * FROM test where star=1 LIMIT %s,1;"
        cursor.execute(sql, indexNum)
        conn.commit()

        cursor.close()
        conn.close()
        word_list = cursor.fetchall()
        list = word_list[0]
        getId = list['id']
        getWord = list['word']
        getChinese = list['chinese']
        getTime = list['time']
        getTime = getTime[5:10]
        getStar = list['star']
        json_dict = {
            'id': getId,
            'word': getWord,
            'time': getTime,
            'chinese': getChinese,
            'star': getStar
        }
        json_dict = json.dumps(json_dict)
        print(json_dict)

        return jsonify(json_dict)


@app.route('/recitepostXdf', methods=['GET', 'POST'])  # 背单词查询接口
def recitepostXdf():
    if request.method == 'POST':
        indexNum = int(request.form['indexNum'])

        conn = pymysql.connect(host='127.0.0.1', user='root',
                               password='', db='ietls', port=3306, charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

        sql = "SELECT * FROM xdf LIMIT %s,1;"
        cursor.execute(sql, indexNum)
        conn.commit()

        cursor.close()
        conn.close()
        word_list = cursor.fetchall()
        list = word_list[0]
        getId = list['id']
        getWord = list['word']
        getChinese = list['chinese']
        getTime = list['time']
        getTime = getTime[5:10]
        getStar = list['star']
        json_dict = {
            'id': getId,
            'word': getWord,
            'time': getTime,
            'chinese': getChinese,
            'star': getStar
        }
        json_dict = json.dumps(json_dict)

        return jsonify(json_dict)


@app.route('/recitepostStarXdf', methods=['GET', 'POST'])  # 背单词查询接口
def recitepostStarXdf():
    if request.method == 'POST':
        indexNum = int(request.form['indexNum'])

        conn = pymysql.connect(host='127.0.0.1', user='root',
                               password='', db='ietls', port=3306, charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

        sql = "SELECT * FROM xdf where star=1 LIMIT %s,1;"
        cursor.execute(sql, indexNum)
        conn.commit()

        cursor.close()
        conn.close()
        word_list = cursor.fetchall()
        list = word_list[0]
        getId = list['id']
        getWord = list['word']
        getChinese = list['chinese']
        getTime = list['time']
        getTime = getTime[5:10]
        getStar = list['star']
        json_dict = {
            'id': getId,
            'word': getWord,
            'time': getTime,
            'chinese': getChinese,
            'star': getStar
        }
        json_dict = json.dumps(json_dict)
        print(json_dict)

        return jsonify(json_dict)
    

checkFlag = 0
@app.route('/check', methods=['GET', 'POST'])       # 查询当日背单词任务接口
def check():
    global checkFlag
    if request.method == 'GET':
        if checkFlag == 1:
            return 'done'
        if checkFlag == 0:
            return 'none'
    if request.method == 'POST':
        checkNum = int(request.form['checkNum'])
        if checkNum == 1:
            checkFlag = 1


@app.route('/addStarXdf', methods=['GET', 'POST'])     # 加星标接口
def addStarXdf():
    if request.method == 'POST':
        starId = int(request.form['starId'])
        conn = pymysql.connect(host='127.0.0.1', user='root',
                               password='', db='ietls', port=3306, charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

        sql = "update xdf set star='1' where id=%s;"
        cursor.execute(sql, starId)
        conn.commit()

        cursor.close()
        conn.close()
        return ('done')


@app.route('/addStarBtnXdf', methods=['GET', 'POST'])  # 加星标接口
def addStarBtnXdf():
    if request.method == 'POST':
        getWord = request.form['getWord']
        conn = pymysql.connect(host='127.0.0.1', user='root',
                               password='', db='ietls', port=3306, charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

        sql = "update xdf set star='1' where word=%s;"
        cursor.execute(sql, getWord)
        conn.commit()

        cursor.close()
        conn.close()
        return ('done')


@app.route('/cancelStarXdf', methods=['GET', 'POST'])  # 取消星标接口
def cancelStarXdf():
    if request.method == 'POST':
        starId = int(request.form['starId'])
        conn = pymysql.connect(host='127.0.0.1', user='root',
                               password='', db='ietls', port=3306, charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

        sql = "update xdf set star='0' where id=%s;"
        cursor.execute(sql, starId)
        conn.commit()

        cursor.close()
        conn.close()
        return ('done')


@app.route('/addStar', methods=['GET', 'POST'])     # 加星标接口
def addStar():
    if request.method == 'POST':
        starId = int(request.form['starId'])
        conn = pymysql.connect(host='127.0.0.1', user='root',
                               password='', db='ietls', port=3306, charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

        sql = "update test set star='1' where id=%s;"
        cursor.execute(sql, starId)
        conn.commit()

        cursor.close()
        conn.close()
        return ('done')


@app.route('/addStarBtn', methods=['GET', 'POST'])  # 加星标接口
def addStarBtn():
    if request.method == 'POST':
        getWord = request.form['getWord']
        conn = pymysql.connect(host='127.0.0.1', user='root',
                               password='', db='ietls', port=3306, charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

        sql = "update test set star='1' where word=%s;"
        cursor.execute(sql, getWord)
        conn.commit()

        cursor.close()
        conn.close()
        return ('done')


@app.route('/cancelStar', methods=['GET', 'POST'])  # 取消星标接口
def cancelStar():
    if request.method == 'POST':
        starId = int(request.form['starId'])
        conn = pymysql.connect(host='127.0.0.1', user='root',
                               password='', db='ietls', port=3306, charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

        sql = "update test set star='0' where id=%s;"
        cursor.execute(sql, starId)
        conn.commit()

        cursor.close()
        conn.close()
        return ('done')


@app.errorhandler(404)                              # 传入错误码作为参数状态
def error_date(error):                              # 接受错误作为参数
    return render_template("404.html"), 404


@app.route('/cancelStarBtn', methods=['GET', 'POST'])  # 取消星标接口
def cancelStarBtn():
    if request.method == 'POST':
        getWord = request.form['getWord']
        conn = pymysql.connect(host='127.0.0.1', user='root',
                               password='', db='ietls', port=3306, charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

        sql = "update test set star='0' where word=%s;"
        cursor.execute(sql, getWord)
        conn.commit()

        cursor.close()
        conn.close()
        return ('done')


@app.route('/developing', methods=['GET', 'POST'])  # 取消星标接口
def developing():
    return render_template('developing.html')


if __name__ == '__main__':
   app.run(debug=True)
