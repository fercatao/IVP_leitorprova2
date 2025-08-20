import streamlit as st
import PyPDF2
import re

st.title("📖 Leitor de Provas em PDF (multi-upload)")

# Upload de vários PDFs
pdf_files = st.file_uploader(
    "Envie um ou mais arquivos PDF", 
    type=["pdf"], 
    accept_multiple_files=True
)

# Palavra-chave
palavra = st.text_input("Digite a palavra-chave para buscar")

if pdf_files and palavra:
    for pdf_file in pdf_files:
        st.subheader(f"Arquivo: {pdf_file.name}")
        try:
            leitor = PyPDF2.PdfReader(pdf_file)
            resultados = []

            for i, pagina in enumerate(leitor.pages):
                texto = pagina.extract_text()
                if texto and palavra.lower() in texto.lower():
                    # Destacar todas as ocorrências da palavra-chave
                    # re.escape garante que caracteres especiais não quebrem a regex
                    # (?i) torna a busca insensível a maiúsculas/minúsculas
                    texto_destacado = re.sub(
                        f"(?i)({re.escape(palavra)})", 
                        r"**\1**", 
                        texto
                    )
                    resultados.append(f"### Página {i+1}\n\n{texto_destacado[:800]}...\n")

            if resultados:
                st.success(f"Encontrado em {len(resultados)} páginas")
                for r in resultados:
                    st.markdown(r)
            else:
                st.warning("Nenhuma ocorrência encontrada.")

        except Exception as e:
            st.error(f"Erro ao ler o arquivo {pdf_file.name}: {e}")
