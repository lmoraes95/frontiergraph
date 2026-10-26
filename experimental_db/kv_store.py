
log = []
def append_record(log, key, value):
    record = {
        "key": key,
        "value": value
    }
    log.append(record)
    return log



append_record(log, "paper:101", {"title": "Efficient Language Models"})

def lookup(log, key):
    for i in range(len(log)-1,-1,-1):
        if log[i]["key"] == key:
            return log[i]["value"]
        
    return None