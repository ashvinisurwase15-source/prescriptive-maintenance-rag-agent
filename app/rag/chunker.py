from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
Machine temperature exceeds 100 degrees.
Check cooling fan.
Inspect airflow.
Reduce machine load.
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=50,
    chunk_overlap=10
)

chunks = splitter.split_text(text)

for i, chunk in enumerate(chunks):
    print(f"\nChunk {i+1}")
    print(chunk)