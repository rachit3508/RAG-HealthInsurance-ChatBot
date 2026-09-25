from langchain_pymupdf4llm import PyMuPDF4LLMLoader

class PDFLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load(self):
        loader = PyMuPDF4LLMLoader(
        file_path=self.file_path,
        mode="page",
        pages_delimiter="\n\f")

        docs = loader.load()

        return docs
