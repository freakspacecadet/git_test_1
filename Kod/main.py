from datetime import datetime

print('Hello world!')
now = datetime.now().strftime("%A, %B %d")
output = str(now)
print('Date: ' + output)
