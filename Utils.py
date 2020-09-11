from PyQt5.QtSql import QSqlDatabase

def openDB():
    db = QSqlDatabase.addDatabase("QSQLITE")
    # db.setDatabaseName("../db/ProductManagement_new.db")
    db.setDatabaseName("./db/ProductManagement_new.db")  # 整合框架时使用
    db.open()
    return db




