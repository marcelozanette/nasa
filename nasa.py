import requests
import pandas as pd
import os
from datetime import datetime, timedelta

# Substitua 'SUA_CHAVE_DE_API_AQUI' pela sua chave de API da NASA
api_key = 'fnKD61B5ruwETmo2klaQTNpZajzdDHlfRfvsPfS5'


def obter_dados_api(url):
    # Fazendo a solicitação GET para a API
    response = requests.get(url)

    # Verificando se a solicitação foi bem-sucedida
    if response.status_code == 200:
        # Convertendo a resposta para formato JSON
        data = response.json()
        # Retornando os dados
        return data
    else:
        print("Erro ao acessar a API")


# Função para gerar as datas do mês atual até D-2
def gerar_datas_mes_corrente():
    hoje = datetime.now()
    data_final = hoje - timedelta(days=2)
    data_inicial = hoje.replace(day=1)
    datas = []
    while data_inicial <= data_final:
        datas.append(data_inicial.strftime('%Y-%m-%d'))
        data_inicial += timedelta(days=1)
    return datas

# Gerar as datas desejadas
datas_para_busca = gerar_datas_mes_corrente()

# Inicializando uma lista para armazenar os dados do rover
photo_data = []

#pra cada data coletar os dados do rover
for data in datas_para_busca:
    url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/Perseverance/photos?earth_date={data}&api_key={api_key}"
    print(f"Buscando dados para a data: {data}")
    dados = obter_dados_api(url)
    
    if dados and 'photos' in dados:
        for photo in dados['photos']:
            photo_data.append({
                'photo_id': photo['id'],
                'sol': photo['sol'],
                'camera_id': photo['camera']['id'],
                'camera_name': photo['camera']['name'],
                'camera_full_name': photo['camera']['full_name'],
                'img_src': photo['img_src'],
                'earth_date': photo['earth_date'],
                'rover_id': photo['rover']['id'],
                'rover_name': photo['rover']['name'],
                'rover_landing_date': photo['rover']['landing_date'],
                'rover_launch_date': photo['rover']['launch_date'],
                'rover_status': photo['rover']['status'],
            })



# Criando o DataFrame a partir da lista de dicionários
df = pd.DataFrame(photo_data)

# Exibindo o DataFrame
print(df)
# Salvar o DataFrame em formato CSV
df.to_csv('Perseverance.csv', index=False)

# Criar o diretório principal com o nome do rover
if photo_data:
    rover_name = photo_data[0]['rover_name']
    directory = rover_name
    print(f"criando o diretorio {directory}")
    os.makedirs(directory, exist_ok=True)

    # Baixar cada uma das fotos e salvar no diretório organizado por data
    for photo in photo_data:
        data_pasta = photo['earth_date']
        data_directory = os.path.join(directory, data_pasta)
        os.makedirs(data_directory, exist_ok=True)
        print(f"criando o diretorio {data_directory}")

        img_url = photo['img_src']
        img_name = os.path.join(data_directory, f"{photo['photo_id']}.jpg")
        response = requests.get(img_url)
        if response.status_code == 200:
            with open(img_name, 'wb') as img_file:
                img_file.write(response.content)
                print(f"coletei a imagem {img_name}")
        else:
            print(f"Erro ao baixar a imagem {photo['photo_id']} da data {data_pasta}")
            

