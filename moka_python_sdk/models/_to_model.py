from dacite import from_dict
from humps import decamelize

def _to_model(model, data):
    if "data" in data:
        data = data["data"]
    return from_dict(data_class=model, data=decamelize(data))
