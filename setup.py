from cx_Freeze import setup, Executable
import os

# path = "./asset"
# asset_list = os.listdir(path)
# asset_list_completa = [os.path.join(path, asset).replace("\\", "/") for asset in asset_list]
# print(asset_list_completa)

executables = [Executable("main.py")]
# files = {"include_files": asset_list_completa, "packages": ["pygame"]}

setup(
    name="LpaAtividadePratica",
    version="1.0",
    description="Lpa Atividade Pratica app",
    options={
        "build_exe": {
            "packages": ["pygame"],  # Inclui o pacote pygame
            "include_files": ["asset/icone.ico"],  # Inclui o arquivo de ícone
        }
    },
    executables=[
        Executable(
            script="main.py",  # Substitua pelo nome do seu script principal
            icon="asset/icone.ico",  # Caminho para o ícone
        )
    ],
)

# %%%%%%%%% GERAR A BUILD %%% python setup.py build %%%%
# colocar imagem de icone icon=