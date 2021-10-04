import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файл на Яндекс диск"""
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
            }
        params = {
            'path': file_path,
            'overwrite': 'true'
            }
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        link_for_upload_response = requests.get(url=upload_url, headers=headers, params=params)
        href_for_upload = link_for_upload_response.json()['href']
        
        with open(file_path, 'rb') as file:
            response = requests.put(url=href_for_upload, data=file)
        if response.status_code == 201:
            print('Файл загружен')


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = ...
    token = ...
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
