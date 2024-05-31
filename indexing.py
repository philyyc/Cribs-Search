import os
from whoosh.fields import Schema, TEXT, ID
from whoosh import index
from pdf_scraping import pdf_texts

schema = Schema(
    title = ID(stored=True),
    content = TEXT(stored=True)
)

index_dir = "Index"

def make_index(index_dir, pdf_texts):
    """
    if not os.path.exists(index_dir):
        os.makedirs(index_dir)
        idx = index.create_in(index_dir, schema)
    else:
        idx = index.open_dir(index_dir)
    
    writer = idx.writer()
    """
    if not index.exists_in(index_dir):
        idx = index.create_in(index_dir, schema)
    
    idx = index.open_dir(index_dir)
    writer = idx.writer()

    for file_name, text in pdf_texts.items():
        writer.add_document(title = file_name, content = text)

    writer.commit()

make_index(index_dir, pdf_texts)
print("Index created")