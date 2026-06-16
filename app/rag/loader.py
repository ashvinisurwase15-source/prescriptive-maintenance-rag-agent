from pathlib import Path
from langchain_core.documents import Document

documents = []

for file in Path("data/alerts").glob("*.txt"):
    content = file.read_text()
    documents.append(
        Document(
            page_content=content,
            metadata={"source": str(file)}
        )
    )

for file in Path("data/manuals").glob("*.txt"):
    content = file.read_text()
    documents.append(
        Document(
            page_content=content,
            metadata={"source": str(file)}
        )
    )

print(f"Loaded {len(documents)} documents")

for doc in documents:
    print("\n----------------")
    print(doc.metadata)
    print(doc.page_content)