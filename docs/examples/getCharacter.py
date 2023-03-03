from ESICelery.CeleryApps import CeleryWorker
from ESICelery.tasks.Character import *
import os


def main():
    c = CeleryWorker()

    r = CharacterPublicInfo().get_sync(timeout=5, character_id=1326083433)
    print(r)


if __name__ == '__main__':
    main()
