
# Imports
import pandas            as pd
import streamlit         as st

# Função principal da aplicação
def main():
    # Configuração inicial da página da aplicação
    st.set_page_config(page_title = 'Telemarketing analysis', \
        page_icon = 'telmarketing_icon.png',
        layout="wide",
        initial_sidebar_state='expanded'
    )

    # Título principal da aplicação
    st.write('# Telemarketing analysis')
    st.markdown("---")
    
if __name__ == '__main__':
	main()
    









