from EVECelery.CeleryApps import CeleryWorker
from EVECelery.tasks.Universe import *

CeleryWorker.create_class()
r = SystemInfo().get_sync(timeout=5, system_id=30000142)
print(r)
