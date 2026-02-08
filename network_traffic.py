import csv
def load_csv_to_list(file_path):
    """מקבלת נתיב לקובץ
     csv
    ומחזירה רשימה של רשימות - כל שורה
    כרשימה של שדות.
        """
    with open(file_path, "r", newline="") as f:
        reader = csv.reader(f)
        return list(reader)
        