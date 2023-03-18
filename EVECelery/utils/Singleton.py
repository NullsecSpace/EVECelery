import threading
import logging


class Singleton(type):
    _lock = threading.Lock()
    _init_locks = {}
    _instances = {}
    logger = logging.getLogger('EVECelery.Singleton')

    def __call__(cls, *args, **kwargs):
        cls_name = cls.__name__
        cls.logger.info(f"Request for {cls_name}")
        with cls._lock:
            lock = cls._init_locks.get(cls_name)
            if lock is None:
                lock = threading.Lock()
                cls._init_locks[cls_name] = lock
        with lock:
            if not cls._instances.get(cls_name):
                cls.logger.info(f"Class '{cls_name}' does not exist yet. Attempting to create.")
                cls._instances[cls_name] = super(Singleton, cls).__call__(*args, **kwargs)
            else:
                cls.logger.info(f"Class '{cls_name}' already exists. "
                                f"Returning existing instance at {id(cls._instances[cls_name])}")
            return cls._instances[cls_name]

    @classmethod
    def clear_instance_references(cls):
        with cls._lock:
            cls._init_locks = {}
            cls._instances = {}
