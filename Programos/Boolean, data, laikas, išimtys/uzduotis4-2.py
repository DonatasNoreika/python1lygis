# datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)

import datetime
from datetime import timedelta

now = datetime.datetime.now()
print(now)
print(now - timedelta(days=5))
print(now + timedelta(hours=8))
print(now.strftime("%Y %m %d, %X"))
