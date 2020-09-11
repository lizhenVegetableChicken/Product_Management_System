import logging
import os

from PyQt5.QtSql import QSqlQuery
from Utils import openDB
import time


#登录成功时，插入数据
def insert_info(userId):
    db = openDB()
    query = QSqlQuery()
    LoginTime = time.strftime("%Y-%m-%d %H:%M:%S")
    insert_sql = "INSERT INTO Login_info (id,userId,loginTime,isLogining) VALUES (NULL,'%s', '%s','%s')"% \
                 (userId, LoginTime, True)
    query.exec(insert_sql)
    db.commit()
    db.close()

#退出登录时,将此登录用户的登陆状态改为False
def update_currentLoginState():
    db = openDB()
    query = QSqlQuery()
    search_sql = "SELECT * FROM Login_info WHERE isLogining ='%s'"% True
    query.exec_(search_sql)

    if (query.next()):
        thisId = query.value(0)
        update_sql = "UPDATE Login_info SET isLogining = '%s' WHERE id='%s'" % (False, thisId)
        query.exec_(update_sql)
    db.commit()
    db.close()

#获取当前用户id，返回用户id
#返回值：用户id
def getCurrentUserId():
    db = openDB()
    query = QSqlQuery()
    search_sql = "SELECT * FROM Login_info WHERE isLogining='%s'"% True

    query.exec_(search_sql)
    if(query.next()):
        userid = query.value(1)
        db.commit()
        db.close()
    else:
        userid = -1
    return str(userid)

#删除登录时间时间超过一个月的数据记录
def delOverOneMonthItem():
    db = openDB()
    query = QSqlQuery()
    #获取前一个月的时间
    struct_time = ( time.localtime().tm_year,time.localtime().tm_mon-1,time.localtime().tm_mday,
                    time.localtime().tm_hour,time.localtime().tm_min,time.localtime().tm_sec,
                    time.localtime().tm_wday,time.localtime().tm_yday,time.localtime().tm_isdst
                   )
    OneMonthAgo = time.strftime("%Y-%m-%d %H:%M:%S",struct_time)

    delete_sql = "DELETE FROM Login_info WHERE loginTime < '%s'" %OneMonthAgo
    query.exec_(delete_sql)
    db.commit()
    db.close()

 #info级别的正常运行日志，每小时一个文件
#参数message为输出的内容（填写动宾短语最佳）
#返回一个logger对象，以便正确显示日志行所处的位置
def logToFile():
    #1 创建一个logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    #2 创建一个handler，用于写入日志文件
    #每小时一个文件
    rq = time.strftime('%Y-%m-%d-%H',time.localtime(time.time()))
    log_path = os.getcwd()+'/logs/'
    # log_path = "G:\\Work\\Product_Management_System\\logs\\"
    log_name = log_path + rq + '.logs'
    logfile = log_name
    if not logger.handlers:
        fh = logging.FileHandler(logfile,mode='a',encoding='utf-8')#续写
        fh.setLevel(logging.DEBUG)
        #3 定义handler的输出格式
        formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
        fh.setFormatter(formatter)
        #4 将logger添加到handler里面
        logger.addHandler(fh)
    # userid = getCurrentUserId()
    # message = '用户:'+ str(userid)+' ' +message
    # #正常运行
    # logger.info(str(message))
    return logger

#返回一个0或1，来表示当前用户是否为管理员
def distinctUserRight():
    currentUserId = getCurrentUserId()
    db = openDB()
    query = QSqlQuery()
    search_sql = "SELECT * FROM User WHERE IsAdmin='%s'and UserId='%s'" % (str(0),currentUserId)
    query.exec(search_sql)
    db.commit()
    if (query.next()):
        db.close()
        return 0
    db.close()
    return 1

# if __name__ == "__main__":
#     delOverOneMonthItem()