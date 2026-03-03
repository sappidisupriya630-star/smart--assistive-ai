def validat_task_data(data):
if not data:
     retrun False
if 'title' not in data or not data['title']:
     retrun False
return True
