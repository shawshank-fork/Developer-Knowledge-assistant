
def chunk_text(text, chunk_size):
    words = text.split()

    chunks = []

    for i in range(0, len(words), chunk_size):
        chunk = words[i:i + chunk_size]
        chunks.append(" ".join(chunk))

    return chunks


text = "FastAPI is a Python framework. It supports GET and POST requests. Pydantic validates incoming data."

result = chunk_text(text, 5)

for chunk in result:
    print(chunk)
    print("-----")
