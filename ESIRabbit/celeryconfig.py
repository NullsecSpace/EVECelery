import os


def get_broker_url():
    """read env vars for rabbit mq to generate connect url"""
    user = os.environ["MessageQueueUser"]
    password = os.environ["MessageQueuePassword"]
    host = os.environ["MessageQueueHost"]
    port = os.environ["MessageQueuePort"]
    vhost = os.environ["MessageQueueVhost"]
    return f"amqp://{user}:{password}@{host}:{port}/{vhost}"


def get_redis_url():
    """read env vars for redis to generate connect url"""
    user = os.environ["RedisUser"]
    password = os.environ["RedisPassword"]
    host = os.environ["RedisHost"]
    port = os.environ["RedisPort"]
    db = os.environ["RedisDb"]
    return f"redis://{user}:{password}@{host}:{port}/{db}"


broker_url = get_broker_url()
result_backend = get_redis_url()
task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
enable_utc = True
include = ["ESIRabbit.tasks.Alliance.AllianceInfo",
           "ESIRabbit.tasks.Character.CharacterPublicInfo",
           "ESIRabbit.tasks.Corporation.CorporationInfo",
           "ESIRabbit.tasks.Market.PricesList",
           "ESIRabbit.tasks.Universe.CategoryInfo",
           "ESIRabbit.tasks.Universe.ConstellationInfo",
           "ESIRabbit.tasks.Universe.FactionsList",
           "ESIRabbit.tasks.Universe.GroupInfo",
           "ESIRabbit.tasks.Universe.RegionInfo",
           "ESIRabbit.tasks.Universe.SystemInfo",
           "ESIRabbit.tasks.Universe.TypeInfo"
           ]
task_default_queue = "CeleryDefault"
task_routes = {
               "ESIRabbit.tasks.Alliance.AllianceInfo.*": {"queue": "GetAllianceInfo"},
               "ESIRabbit.tasks.Character.CharacterPublicInfo.*": {"queue": "GetCharacterPublicInfo"},
               "ESIRabbit.tasks.Corporation.CorporationInfo.*": {"queue": "GetCorporationInfo"},
               "ESIRabbit.tasks.Market.PricesList.*": {"queue": "GetPricesList"},
               "ESIRabbit.tasks.Universe.CategoryInfo.*": {"queue": "GetCategoryInfo"},
               "ESIRabbit.tasks.Universe.ConstellationInfo.*": {"queue": "GetConstellationInfo"},
               "ESIRabbit.tasks.Universe.FactionsList.*": {"queue": "GetFactionsList"},
               "ESIRabbit.tasks.Universe.GroupInfo.*": {"queue": "GetGroupInfo"},
               "ESIRabbit.tasks.Universe.RegionInfo.*": {"queue": "GetRegionInfo"},
               "ESIRabbit.tasks.Universe.SystemInfo.*": {"queue": "GetSystemInfo"},
               "ESIRabbit.tasks.Universe.TypeInfo.*": {"queue": "GetTypeInfo"}
               }


