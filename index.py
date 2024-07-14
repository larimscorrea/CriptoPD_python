import PyPDF2
import secrets
import string

# Função para gerar uma senha aleatória
def generate_random_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for i in range(length))
    return password

# Função para adicionar senha a um PDF existente
def protect_pdf(input_filename, output_filename, password):
    with open(input_filename, 'rb') as input_file:
        reader = PyPDF2.PdfReader(input_file)
        writer = PyPDF2.PdfWriter()

        # Adicionar todas as páginas ao writer
        for page_num in range(len(reader.pages)):
            writer.add_page(reader.pages[page_num])

        # Adicionar senha
        writer.encrypt(password)

        # Escrever o PDF protegido
        with open(output_filename, 'wb') as output_file:
            writer.write(output_file)

# Nome do arquivo PDF a ser protegido
input_pdf_filename = "documento.pdf"
# Nome do arquivo PDF protegido
protected_pdf_filename = "documento_protegido.pdf"

# Gera uma senha aleatória
password = generate_random_password()
print(f"A senha gerada é: {password}")

# Protege o PDF com a senha gerada
protect_pdf(input_pdf_filename, protected_pdf_filename, password)

print(f"O PDF protegido foi salvo como {protected_pdf_filename}")
