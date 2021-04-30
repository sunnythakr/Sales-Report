import uuid

def generate_code():
    code = str(uuid.uuid4()).replace('-','').upper()[:12]  #  this will generate the transition id of combinations of 12 character and digit 
    return code