import json






with open("grades.json", "r", encoding="utf-8") as f:



    grade_intervals = json.load(f)



print(grade_intervals)