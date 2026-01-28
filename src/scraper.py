import requests
from bs4 import BeautifulSoup

class AdventureScraper:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        })

    def get_episode_data(self, url):
        """Extrae los metadatos y la lista de servidores del episodio."""
        try:
            response = self.session.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Buscamos los servidores en los elementos de la lista de reproducción
            items = soup.find_all('li', class_='dooplay_player_option')
            
            servers = []
            for item in items:
                servers.append({
                    'name': item.find('span', class_='title').text.strip(),
                    'type': item.get('data-type'),
                    'post': item.get('data-post'),
                    'nume': item.get('data-nume')
                })
            
            return servers
        except Exception as e:
            return f"Error al conectar con la web: {e}"