from ESICelery.CeleryApps import CeleryWorker
from ESICelery.tasks.Routes import *

CeleryWorker.create_class()
r = Route().get_sync(timeout=5, origin=30000142, destination=30002659)  # Jita to Dodixie - 12 jumps
print(f"Jumps: {len(r) - 1} Systems: {r} ")
