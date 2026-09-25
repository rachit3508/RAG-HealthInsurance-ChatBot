from src.ingestion.docLoader.pdfLoader import PDFLoader

def pdfLoader(file_path):
    loader = PDFLoader(file_path)
    return loader.load()

if __name__ == "__main__":
    docs = pdfLoader(r"E:\AI Projects\rag-healthinsurance-bot\RAG-HealthInsurance-ChatBot\data\nsa-health-insurance-basics.pdf")
    print(docs)
