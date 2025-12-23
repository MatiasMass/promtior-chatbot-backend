import requests
from bs4 import BeautifulSoup
from fpdf import FPDF

URL = "https://www.promtior.ai/"


def scrape_to_pdf(output_filename):
    # 1. Descargar el contenido
    response = requests.get(URL)
    response.encoding = 'utf-8' # Asegurar tildes y eñes
    
    print(response.content)
    # 2. Parsear con BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extraemos el título y el texto de los párrafos
    title = soup.title.string if soup.title else "Información de la Empresa"
    paragraphs = soup.find_all('p') # Buscamos todas las etiquetas <p>
    
    # 3. Crear el PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # Escribir el título
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt=title, ln=True, align='C')
    pdf.ln(10)
    
    # Escribir el contenido limpio
    pdf.set_font("Arial", size=12)
    for p in paragraphs:
        text = p.get_text().strip()
        if text:
            # Multi_cell es mejor para párrafos largos
            pdf.multi_cell(0, 10, txt=text)
            pdf.ln(2)
            
    pdf.output(output_filename)
    print(f"✅ PDF guardado como: {output_filename}")

# Uso
# scrape_to_pdf("https://www.promtior.ai/", "datos_promtior.pdf")

scrape_to_pdf("data_promtior.pdf")