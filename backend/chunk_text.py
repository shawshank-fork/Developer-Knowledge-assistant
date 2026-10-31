def chunk_text(text, chunk_size, overlap):
    words = text.split()
    chunks = []

    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than zero")

    if overlap < 0 or overlap >= chunk_size:
        raise ValueError("overlap must be non-negative and smaller than chunk_size")

    step = chunk_size - overlap

    for i in range(0, len(words), step):
        chunk = words[i:i + chunk_size]
        chunks.append(" ".join(chunk))
    return chunks    


text = "FastAPI is a Python framework used to build APIs efficiently."

result = chunk_text(text, 4, 4)

for chunk in result:
    print(chunk)
    print("-----")