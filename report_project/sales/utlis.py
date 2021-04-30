import uuid

def generate_code():
    code = str(uuid.uud4()).replace('-','')[:12]
    return code