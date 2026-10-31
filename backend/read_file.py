file_path = "../sample_docs/api_docs.txt"

def read_document(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        return content

    except FileNotFoundError:
        print("Error: Document not found")
        return None

    except PermissionError:
        print("Error: Permission Denied")
        return None


# Test with an existing file
content = read_document(file_path)

if content is not None:
    print(content)


		

#Imagine we ingest a 500-line API documentation file.
#- read() gives us one large string.
#- readlines() gives us a list of individual lines.
#We can then iterate over the lines, inspect them, filter empty lines, or group them into chunks.
#One important distinction: readlines() loads all lines into memory. For very large documents, iterating directly over the file is more memory-efficient.

#3. Iterating directly over the file
#for line in file:    print(line)
#- Reads one line at a time.
#- Processes that line.
#- Moves to the next line.
#- Doesn't need to store the entire document in memory.