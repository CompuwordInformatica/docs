import streamlit as st

def especificacoes():
    import streamlit as st

    st.sidebar.success("Selecione o equipamento")

    """
    # CHECKLIST - ESPECIFICAÇÕES

    """
    informacoes = {
        "dados": {
            "dados_serial_number": "",
            "dados_modelo": "",
            "dados_service_tag": ""
        },
        "processadores": {

        },
        "memorias": {},
        "sistema_operacional": [],
        "armazenamento": [],
        "placa_de_video": [],
        "placa_mae": {
            "fabricante": "",
            "modelo": "",
            "versao_bios": ""
        }
    }

    with st.expander("DADOS"):
        dados_col1, dados_col2, dados_col3 = st.columns(3)

        with dados_col1:
            dados_serial_number = st.text_input('DADOS - SERIAL NUMBER', '')
            informacoes['dados']['dados_serial_number'] = dados_serial_number

        with dados_col2:
            dados_modelo = st.text_input('DADOS - MODELO', '')
            informacoes['dados']['dados_modelo'] = dados_modelo
            
        with dados_col3:
            dados_service_tag = st.text_input('DADOS - SERVICE TAG', '')
            informacoes['dados']['dados_service_tag'] = dados_service_tag

    with st.expander("PROCESSADORES"):
        num_processors = st.number_input("Quantidade de Processadores:", min_value=0, value=0)

        if num_processors:
            processador_marca = st.radio(
                "MARCA DO PROCESSADOR:",
                ["INTEL", "AMD", "OUTRO"],
                index=None,
                key="processador_marca"
            )
            informacoes['processadores']['marca'] = processador_marca
            st.write(informacoes)
            
            for num in range(num_processors):
                informacoes['processadores'][f'processador{num}'] = {}
                expand = st.checkbox(f"PROCESSADOR {num + 1}")
                
                if expand:
                    processador_col1, processador_col2 = st.columns(2)
                    with processador_col1:
                        processador_modelo = st.text_input("MODELO DO PROCESSADOR", key=f"processador_modelo{num}")
                        informacoes['processadores'][f'processador{num}']['modelo'] = processador_modelo

                    with processador_col2:
                        processador_ghz = st.number_input("MODELO DO PROCESSADOR", key=f"processador_ghz{num}")
                        informacoes['processadores'][f'processador{num}']['ghz'] = processador_ghz
                    
                if num_processors > 1:
                    remove = st.button(f"Remover Processador {num + 1}")
                    
                    if remove:
                        # Aqui, você pode remover o processador da lista ou resetar os campos
                        pass
                            
                st.write("-------------")
                    
    with st.expander("MEMÓRIAS"):

        num_memories = st.number_input("Quantidade de Memórias:", min_value=0, value=0)

        memorias_ddr = st.selectbox(
            'QUAL DDR?',
            ('DDR1', 'DDR2', 'DDR3', 'DDR4', 'DDR5'), index=None)
        informacoes['memorias']['ddr'] = memorias_ddr
        
        for num in range(num_memories):
            expand = st.checkbox(f"MEMORIA {num + 1}")
            
            if expand:
                informacoes['memorias'][f'memoria{num}'] = {}
                memorias_col1, memorias_col2, memorias_col3 = st.columns(3)

                with memorias_col1:
                    memorias_gb = st.selectbox(
                    'GB DE MEMÓRIA',
                    ('1', '2', '4', '8', '16', '32', '64'), index=None, key=f"memorias_gb{num}")
                    informacoes['memorias'][f'memoria{num}']['gb'] = memorias_gb

                with memorias_col2:
                    memoria_marca = st.text_input('MARCA', '', key=f"memorias_marca{num}")
                    informacoes['memorias'][f'memoria{num}']['marca'] = memoria_marca    

                with memorias_col3:
                    memoria_frequencia = st.number_input('FREQUENCIA', '', key=f"memoria_frequencia{num}")
                    informacoes['memorias'][f'memoria{num}']['frequencia'] = memoria_frequencia 
                    
                if num_memories > 1:
                    remove = st.button(f"Remover Memoria {num + 1}")
                    
                    if remove:
                        # Aqui, você pode remover o processador da lista ou resetar os campos
                        pass
                        
            st.write("-------------")        

    with st.expander("SISTEMA OPERACIONAL"):
        num_sistemas = st.number_input("Quantidade de SO's:", min_value=0, value=0)

        for num in range(num_sistemas):
            expand = st.checkbox(f"SISTEMA OPERACIONAL {num + 1}")
            
            if expand:
                sistema_operacional_col1, sistema_operacional_col2 = st.columns(2)

                with sistema_operacional_col1:
                    sistema_operacional = st.radio(
                    "SELECIONE O SISTEMA",
                    ["Windows", "MacOS", "Linux"], index=None, key=f"sistema_operacional{num}"
                    )

                if sistema_operacional:
                    with sistema_operacional_col2:
                        if sistema_operacional == "Windows":
                            tipo_sistema = st.selectbox(
                                "QUAL WINDOWS?",
                                ("Windows Server", "Windows 11", "Windows 10", "Windows 8.1", "Windows 8", "Windows 7", "Windows Vista", "Windows XP", "Windows CE", "Windows 98", "Windows 95"),
                                index=None,
                                placeholder="Selecione a versão do Windows...",
                                key=f"tipo_sistema{num}"
                            )
                            if tipo_sistema == "Windows Server":
                                versao_sistema = st.selectbox(
                                    "QUAL VERSÃO?",
                                    ("2022", "2019", "2016", "2012", "2008", "2003", "2000", "HPC Server 2008", "Home Server", "Home Server 2011", "Small Business Server", "Essential Business Server", "Windows NT Server"),
                                    index=None,
                                    placeholder="Selecione a versão do Windows...",
                                    key=f"versao_sistema{num}"
                                )
                            else:
                                versao_sistema = st.selectbox(
                                    "QUAL VERSÃO?",
                                    ("Pro", "Home", "Home Single Language", "Enterprise", "Ultimate"),
                                    index=None,
                                    placeholder="Selecione a versão do Windows...",
                                    key=f"versao_sistema{num}"
                                )
                        elif sistema_operacional == "MacOS":
                            tipo_sistema = st.selectbox(
                                "QUAL MACOS?",
                                ("MacOS Sonoma", "MacOS Ventura", "MacOS Monterey", "MacOS Big Sur", "MacOS Catalina", "MacOS Mojave", "MacOS High Sierra",
                                "MacOS Sierra", "OS X El Capitan", "OS X Yosemite", "OS X Mavericks", "OS X Mountain Lion",
                                "OS X Lion", "Mac OS X Snow Leopard", "Mac OS X Leopard", "Mac OS X Tiger", "Mac OS X Panther",
                                "Mac OS X Jaguar", "Mac OS X Puma", "Mac OS X Cheetah"),
                                index=None,
                                placeholder="Selecione a versão do MacOS...",
                                key=f"tipo_sistema{num}"
                            )
                        else:
                            tipo_sistema = st.text_input('DISTRIBUIÇÃO:', '', key=f"tipo_sistema{num}")


    with st.expander("ARMAZENAMENTO"):
        num_armazenamento = st.number_input("Quantidade de Discos:", min_value=0, value=0)

        for num in range(num_armazenamento):
            expand = st.checkbox(f"DISCO DE ARMAZENAMENTO {num + 1}")
            
            if expand:
                armazenamento_col1, armazenamento_col2, armazenamento_col3 = st.columns(3)
                armazenamento_col4, armazenamento_col5 = st.columns(2)
        
                with armazenamento_col1:
                    tipo_disco = st.selectbox(
                                "TIPO DE DISPOSITIVO:",
                                ("HDD", "SSD", "NVme M.2", "SATA M.2"),
                                index=None,
                                placeholder="Selecione o tipo de dispositivo...",
                                key=f"tipo_disco{num}"
                            )

                with armazenamento_col2:
                    modelo_disco = st.text_input('MODELO:', '', key=f"modelo_disco{num}")

                with armazenamento_col3:
                    estado_disco = st.selectbox(
                        "ESTADO DISPOSITIVO:",
                        ("SAUDÁVEL", "ALERTA", "CRÍTICO", "NÃO RECONHECE"),
                        index=None,
                        placeholder="Selecione o estado do dispositivo...",
                        key=f"estado_disco{num}"
                    )
        
                with armazenamento_col4:
                    capacidade_disco = st.number_input("CAPACIDADE:", value=None, placeholder="Escreva em GB...", key=f"capacidade_disco{num}")

                with armazenamento_col5:
                    livre_disco = st.number_input("ESPAÇO LIVRE:", value=None, placeholder="Escreva em GB...", key=f"livre_disco{num}")


    with st.expander("PLACA DE VÍDEO"):
        num_videos = st.number_input("Quantidade de Placas de Vídeo:", min_value=0, value=0)

        for num in range(num_videos):
            expand = st.checkbox(f"PLACA DE VIDEO {num + 1}")

            if expand:
                placa_de_video_col1, placa_de_video_col2 = st.columns(2)

                with placa_de_video_col1:
                    fabricante_placa = st.radio(
                        "SELECIONE O FABRICANTE",
                        ["NVidia", "AMD", "Intel"], index=None,
                        key=f"fabricante_placa_video{num}"
                    )

                with placa_de_video_col2:
                    modelo_placa_video = st.text_input('MODELO DA PLACA DE VÍDEO:', '', key=f"modelo_placa_video{num}")
            
        

    with st.expander("PLACA MÃE"):
        placa_mae_fabricante = st.selectbox(
            "FABRICANTE DA PLACA MÃE:",
            ("ASUS", "Gigabyte", "MSI", "ASRock", "EVGA", "Intel", "Biostar", "AORUS", "ROG", "MSI MPG", "ZOTAC", "Supermicro", "Outra"),
            index=None,
            placeholder="Selecione o Fabricante...",
        )

        placa_mae_modelo = st.text_input('MODELO DA PLACA MÃE:', '')
        placa_mae_bios = st.number_input("VERSÃO DA BIOS:", value=None, placeholder="Escreva a versão...")


    st.divider()

    button_col1, button_col2 = st.columns(2, gap="small")

    with button_col1:
        st.button("LIMPAR")
    

    with button_col2:
        st.button("SALVAR", type="primary")  
         

page_names_to_funcs = {
    "ESPECIFICAÇÕES": especificacoes,
}

demo_name = st.sidebar.selectbox("SELECIONE UM PROCEDIMENTO", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()