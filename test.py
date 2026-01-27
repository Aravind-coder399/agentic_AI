from langchain_text_splitters import RecursiveCharacterTextSplitter

# 1. First, we need to read the content of your file
with open("sample_document.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

# 2. Initialize the splitter
# We use 'Recursive' because it tries to split on paragraphs, then sentences, 
# then words, keeping the structure as intact as possible.
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100, 
    chunk_overlap=20  # Adding overlap so context isn't cut in half!
)

# 3. Split the text
texts = text_splitter.split_text(raw_text)

# 4. View the results
for i, chunk in enumerate(texts):
    print(f"--- Chunk {i+1} ---")
    print(chunk)