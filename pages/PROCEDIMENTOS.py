import streamlit as st

def intro():
    import streamlit as st

    st.write("# Welcome to Streamlit! 👋")
    st.sidebar.success("Selecione um procedimento acima")

    st.markdown(
        """
        Streamlit is an open-source app framework built specifically for
        Machine Learning and Data Science projects.

        **👈 Select a demo from the dropdown on the left** to see some examples
        of what Streamlit can do!

        ### Want to learn more?

        - Check out [streamlit.io](https://streamlit.io)
        - Jump into our [documentation](https://docs.streamlit.io)
        - Ask a question in our [community
          forums](https://discuss.streamlit.io)

        ### See more complex demos

        - Use a neural net to [analyze the Udacity Self-driving Car Image
          Dataset](https://github.com/streamlit/demo-self-driving)
        - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
    """
    )

def venda_maquina():
    import streamlit as st

    st.markdown(f"# {list(page_names_to_funcs.keys())[2]} 🖥")
    """
    ---
    ### 1 – Instalação limpa do Windows 10 ou 11 no SSD/HDD. 
    `(consulte o guia INSTALAÇÃO WINDOWS)`

    ### 2 – Instalação dos programas padrão 
    `(consulte o guia PROGRAMAS PADRÃO)`
    """
    st.info('⚠️ IMPORTANTE: ENVIAR COM CABO DE FORÇA PADRÃO NOVO. ⚠️')
    """
    ---
    ### ATENÇÃO: CLIENTES COM LICENÇAS ADQUIRIDAS. 📋

    - Instalação do Office 365 caso o cliente possua licença
    
    `(consulte o guia OFFICE 365)`

    - Instalação do Antivírus BitDender caso o cliente possua licença 
    
    `(consulte o guia INSTALAÇÃO BITDEFENDER)`
    """
    

def plotting_demo():
    import streamlit as st

    st.markdown(f'# {list(page_names_to_funcs.keys())[1]} ')
    st.write(
        """
        This demo illustrates a combination of plotting and animation with
Streamlit. We're generating a bunch of random numbers in a loop for around
5 seconds. Enjoy!
"""
    )

def data_frame_demo():
    import streamlit as st

    st.markdown(f"# {list(page_names_to_funcs.keys())[3]}")
    st.write(
        """
        This demo shows how to use `st.write` to visualize Pandas DataFrames.

(Data courtesy of the [UN Data Explorer](http://data.un.org/Explorer.aspx).)
"""
    )

page_names_to_funcs = {
    "—": intro,
    "Plotting Demo": plotting_demo,
    "VENDA DE MICRO": venda_maquina,
    "DataFrame Demo": data_frame_demo
}

demo_name = st.sidebar.selectbox("SELECIONE UM PROCEDIMENTO", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()