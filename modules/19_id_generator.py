import uuid

def generate_id():
    return str(uuid.uuid4())

if __name__ == "__main__":
    id = generate_id()
    print(id)