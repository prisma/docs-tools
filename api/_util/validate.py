from typing import Dict, List

NoneType = type(None)

def get_from_dict(item: str, dict: Dict):
    if item in dict:
        return dict[item]
    else:
        return

def validate_query(data: Dict, query_type: Dict[str, List[type]]) -> Dict:
    result = {}
    for key, item in data.items():
        if key in query_type.keys():
            if type(item) in query_type[key]:
                result[key] = item
            else:
                raise Exception("Wrong shape for query")
    return result

def validate_type(data: Dict, query_type: Dict[str, List[type]]) -> Dict:
    result = {}
    for key, item in query_type.items():
        if type(get_from_dict(key, data)) in item:
            result[key] = data[key]
        else:
            raise Exception("Wrong shape for type")
    return result