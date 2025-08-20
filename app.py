import streamlit as st
import PyPDF2
import re

# Imagem do ícone
st.image("mood.jpeg", width=200)

# Título com fonte Lemon Milk Light
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Lemon+Milk:wght@300&display=swap" rel="stylesheet">
    <h1 style='font-family: "Lemon Milk", sans-serif; font-weight: 200;'>
        Leitor de provas!
    </h1>
""", unsafe_allow_html=True)

# Subtítulo com Lemon Milk
st.markdown("""
    <h2 style='font-family: "Lemon Milk", sans-serif; font-weight: 50;'>
        Banco de Dados
    </h2>
""", unsafe_allow_html=True)

# Upload de vários PDFs
pdf_files = st.file_uploader(
    "ENVIE UM OU MAIS ARQUIVOS PDF", 
    type=["pdf"], 
    accept_multiple_files=True
)

# Palavra-chave
palavra = st.text_input("DIGITE A PALAVRA-CHAVE PARA BUSCAR")

if pdf_files and palavra:
    for pdf_file in pdf_files:
        st.subheader(f"Arquivo: {pdf_file.name}")
        try:
            leitor = PyPDF2.PdfReader(pdf_file)
            resultados = []

            for i, pagina in enumerate(leitor.pages):
                texto = pagina.extract_text()
                if texto and palavra.lower() in texto.lower():
                  if texto and palavra.lower() in texto.lower():
                    # Destacar todas as ocorrências da palavra-chave
                    # re.escape garante que caracteres especiais não quebrem a regex
                    # (?i) torna a busca insensível a maiúsculas/minúsculas
                    texto_destacado = re.sub(
                        f"(?i)({re.escape(palavra)})", 
                        r'**⚡\1⚡**', 
                        texto
                    )
                    resultados.append(f"### Página {i+1}\n\n{texto_destacado[:1500]}...\n")

            if resultados:
                st.success(f"Encontrado em {len(resultados)} páginas")
                for r in resultados:
                    st.markdown(r)
            else:
                st.warning("Nenhuma ocorrência encontrada.")

        except Exception as e:
            st.error(f"Erro ao ler o arquivo {pdf_file.name}: {e}")
