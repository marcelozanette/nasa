## Coleta de fotos da API da NASA
### Descrição
  Esse script foi projetado para coletar imagens coletadas pelos rovers Curiosity, Opportunity e Spirit da NASA em Marte via API. Essa coleta é filtrada pela data 
corrente day-2 salvandao as em um diretório local.
  Também salva um arquivo .csv, no diretório local, com as informações sbre as fotos coletadas como:
    -photo_id,
    -sol,
    -camera_id,
    -camera_name,
    -camera_full_name,
    -img_src,
    -earth_date,
    -rover_id,
    -rover_name,
    -rover_landing_date,
    -rover_launch_date,
    -rover_status.

### Câmeras Rover

![image](https://github.com/user-attachments/assets/12f7a188-46f8-41b8-aeef-eeefa4d01133)

### Consultando pelo sol marciano

![image](https://github.com/user-attachments/assets/4ba53504-94fb-4a34-a102-012d28277328)

### Consultas de exemplo
https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=DEMO_KEY



https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&camera=fhaz&api_key=DEMO_KEY

https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&page=2&api_key=DEMO_KEY

### Consultando por data da Terra

![image](https://github.com/user-attachments/assets/ce05ad4c-6896-42d4-8655-5e4cf1236d3d)





