import pdfplumber

def recuperer_text(chemin):
    with pdfplumber.open(chemin) as tool:
        for np, page in enumerate(tool.pages, 1):
            print("page N ",np)
            donne = page.extract_text()
            print(donne)
            
recuperer_text("C:/Users/tya/Desktop/t/script Python/Script CODE/soutenance-GRP1.pdf")