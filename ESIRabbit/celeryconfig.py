task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
enable_utc = True
task_default_queue = "ESIRabbitDefault"
task_routes = {
               "AllianceInfo": {"queue": "GetAllianceInfo"},
               "CharacterPublicInfo": {"queue": "GetCharacterPublicInfo"},
               "CorporationInfo": {"queue": "GetCorporationInfo"},
               "PricesList": {"queue": "GetPricesList"},
               "CategoryInfo": {"queue": "GetCategoryInfo"},
               "ConstellationInfo": {"queue": "GetConstellationInfo"},
               "FactionsList.": {"queue": "GetFactionsList"},
               "GroupInfo": {"queue": "GetGroupInfo"},
               "RegionInfo": {"queue": "GetRegionInfo"},
               "SystemInfo": {"queue": "GetSystemInfo"},
               "TypeInfo": {"queue": "GetTypeInfo"}
               }


