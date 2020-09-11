import os
import shutil

from PyQt5.QtSql import QSqlQuery

from Login_recorder import logToFile, getCurrentUserId
from Utils import openDB


def deleteImage():
    logger = logToFile()
    UserId = getCurrentUserId()
    #print(UserId)

deleteImage()