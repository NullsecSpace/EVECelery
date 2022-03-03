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
task_default_queue = "ESIRabbitDefault"
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


