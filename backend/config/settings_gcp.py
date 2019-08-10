from google.cloud import datastore

client = datastore.Client()

def get_setting(name):
    query = client.query(kind="Settings", filters=[["name", "=", name]])
    entitys = list(query.fetch())
    if not entitys:
        raise ValueError("Could not find any entity")
    return entitys[0]['value']
