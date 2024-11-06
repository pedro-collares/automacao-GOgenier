import asyncio
import json
from playwright.async_api import async_playwright
import os
import base64
import io
from pydub import AudioSegment
from pydub.playback import play
import requests

# ---------------------

# Requests de API's de Agentes, Chat, Copilot, STT, TTS, Insights e Autenticação do banco de dados

# ---------------------


async def test_api():
    async with async_playwright() as p:

        async def agents():
            request_context = await p.request.new_context()

            url = 'https://app.genier.ai/qa/api/agent/agent_40814927-2e7c-4742-b323-2ba7750c82b2'

            headers = { 
                'Authorization' : '17fe10f1-35a0-47cc-a631-9d33f408961a',
                'Content-Type': 'application/json'
            }

            data = {
                "history": [],
                "query": "Bom dia"
            }

            response = await request_context.post(url, headers=headers, data=data)

            if response.status == 200:
                json_response = await response.json()
                print("REPOSTA DA API DO AGENTE:", json_response['history'][0]['output'], "\n")
            else:
                print(f"ERRO DA NA API DO AGENTE {response.status}: {await response.text()}", "\n")
        

        async def copilot():
            request_context = await p.request.new_context()

            url = 'https://app.genier.ai/qa/api/generate' 

            headers = {
                'Authorization' : '17fe10f1-35a0-47cc-a631-9d33f408961a',
                'Content_Type' : 'application/json'

            }

            data = { 
                'model' : 'model_e3572f67-0784-490f-b901-854471edba18', 
                'query' : 'Fale sobre o Golf',
                'ret_sources' : 'false|true'
            }


            response = await request_context.post(url, headers=headers, data=data)

            if response.status == 200:
                json_response = await response.json()    
                print("RESPOSTA DA API DO COPILOT:", json_response['response'], "\n")
            else:
                print(f"ERRO NA API DO COPILOT {response.status}: {await response.text()}")

        async def chat():
            request_context = await p.request.new_context()

            url = 'https://app.genier.ai/qa/api/generate_mem' 

            headers = {
                'Authorization' : '17fe10f1-35a0-47cc-a631-9d33f408961a',
                'Content_Type' : 'application/json'
            }

            data = { 
                'model' : 'model_e3572f67-0784-490f-b901-854471edba18', 
                'query' : 'Fale sobre o Jetta',
                'session' : '<ID RECEBIDO NA PRIMEIRA CHAMADA>',
                'ret_sources' : 'false|true'
            }


            response = await request_context.post(url, headers=headers, data=data)

            if response.status == 200: 
                json_response = await response.json()    
                print("RESPOSTA DA API DO CHAT:", json_response['response'], "\n")
            else:
                print(f"ERRO NA API DO CHAT {response.status}: {await response.text()}")

        async def search():
            request_context = await p.request.new_context()

            url = 'https://app.genier.ai/qa/api/search' 

            headers = {
                'Authorization' : '17fe10f1-35a0-47cc-a631-9d33f408961a',
                'Content_Type' : 'application/json'
            }

            data = { 
                'model' : 'model_e3572f67-0784-490f-b901-854471edba18', 
                'query' : 'Jetta'
               
            }


            response = await request_context.post(url, headers=headers, data=data)

            if response.status == 200: 
                print("RESPOSTA DA API DO SEARCH:", await response.json(), "\n")
            else:
                print(f"ERRO NA API DO SEARCH {response.status}: {await response.text()}")


        async def stt():

            current_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(current_dir, 'files', 'audio.flac')

            url = 'https://app.genier.ai/qa/api/stt_transcribe'

            headers = {
                'Authorization': '17fe10f1-35a0-47cc-a631-9d33f408961a'
                }
            
            request_context = await p.request.new_context()

            try:
                with open(file_path, 'rb') as file:
                    response = await request_context.post(url, headers=headers, multipart={'file': {
                        'name': 'audio.flac', 
                        'mimeType': 'audio/x-flac',  
                        'buffer': file.read()
                        }
                    }
                )
                    if response.status == 200:
                        result_json = await response.json()
                        print("RESPOSTA DA API DO STT:", result_json['result'], "\n")
                    else:   
                        print(f"ERRO NA API DO STT {response.status}: {await response.text()}")
            except Exception as e:
                print(f'Erro ao enviar o arquivo {e}')

        async def tts():
            request_context = await p.request.new_context()

            url = "https://app.genier.ai/qa/api/tts"
        
            headers = {
                "Authorization": "17fe10f1-35a0-47cc-a631-9d33f408961a",
                "Content-Type": "application/json"
            }

            data = {
                "query": "Este é um exemplo de síntese de texto para fala."
            }

            response = await request_context.post(url, headers=headers, data=data)

            if response.status == 200: 
                print("AUDIO TRANSCRITO: \n")
                json_response = await response.json() 
                audio_base64 = json_response.get("audio_content_base64") 
                audio_bytes = base64.b64decode(audio_base64)

                audio = AudioSegment.from_file(io.BytesIO(audio_bytes), format="mp3")
                play(audio)

            else:
                print(f"ERRO NA API DO TTS {response.status}: {await response.text()}")

        async def database():
            request_context = await p.request.new_context()

            url = "https://app.genier.ai/qa/godb/api/admins/auth-with-password"
        
            headers = {
                "Authorization": "17fe10f1-35a0-47cc-a631-9d33f408961a",
                'Cookie': '_9451f=2b943671967f49df'
            }

            data = {
                "identity": "pedro.bigiunas@fortics.com.br",
                "password": "@Collares123"
            }

            response = await request_context.post(url, headers=headers, data=data)

            if response.status == 200: 
                json_response = await response.json()
                token = json_response.get("token")  
                print("\nTOKEN DO DATABASE:", token, "\n")
                return token
            else:
                print(f"ERRO NA API DO DATABASE {response.status}: {await response.text()}")
                return None



        async def list_db(token):
            request_context = await p.request.new_context()

            url = "https://app.genier.ai/qa/godb/api/collections/automation/records"
        
            headers = { 
                'Authorization': f'Bearer {token}'
                }

            response = await request_context.get(url, headers=headers)

            if response.status == 200: 
                print("CONSULTA DO DATABASE:", await response.json() , "\n")
            else:
                print(f"ERRO NA API DO DATABASE {response.status}: {await response.text()}")



        async def agent_multimodal():
            current_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(current_dir, 'files', 'golf_gti.mp3')

            url = "https://app.genier.ai/qa/api/agent_mm/agent_40814927-2e7c-4742-b323-2ba7750c82b2"

            headers = {
                "Authorization": "17fe10f1-35a0-47cc-a631-9d33f408961a"
            }

            history_json = json.dumps([]) 

            try:
                with open(file_path, 'rb') as audio:
                    files = { 
                    	'history': (None, history_json, 'application/json'),
                    	'audio': ('golf.gti.mp3', audio, 'audio/mpeg'),
                    	'tts': (None, 'true')
                    }
                    response = requests.post(url, headers=headers, files=files)
                
                if response.status_code == 200 :
                    print("AUDIO TRANSCRITO: \n")
                    audio_base64 = response.json().get("tts_audio_mp3_encoded_base64") 
                    audio_bytes = base64.b64decode(audio_base64)
                
                    audio = AudioSegment.from_file(io.BytesIO(audio_bytes), format="mp3")
                    play(audio)
                else:
                    print(f"Erro na API do agente multimodal {response.status_code}")
            except Exception as e:
                print(f"Erro ao enviar arquivo {e}")


        await agents()  	
        await copilot()
        await chat()
        await search()
        await stt() 
        await tts()
        token = await database() 
        if token:
            await list_db(token)
        await agent_multimodal()

asyncio.run(test_api())