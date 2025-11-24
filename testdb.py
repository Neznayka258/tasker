from pathlib import Path
from db_manager import DBManager
from datetime import datetime


db = DBManager()
db.add_task("сделать дз","",datetime.now(),1, "Учебная" )
db.add_task("сходить на прогулку","",datetime.now(),1, "Другое" )
print(db.get_tasks()[0])