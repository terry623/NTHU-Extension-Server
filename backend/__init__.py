from .views import app
from .crawler import add_data, db_to_csv
from .sim import sim_to_csv, csv_to_neo

# db_to_csv()
# add_data()
# sim_to_csv()
# csv_to_neo()

# searchOnlyKeyword("課程中文名稱", "程式設計")
# searchDoubleKeyword("時間", "英文", "M1M2")
# searchBySingleCourseNo("10620CS 471000")

# group = [{"other_id": 5, "compare_value": 0.99},
#          {"other_id": 10, "compare_value": 0.88},
#          {"other_id": 15, "compare_value": 0.77}]
         
# searchByID_Group(group)
