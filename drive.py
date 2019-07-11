from pprint import pprint
from apiclient.discovery import build
from apiclient.http import MediaFileUpload
from oauth2client.service_account import ServiceAccountCredentials
import config

def get_service(api_name, api_version, scopes, key_file_location):
    """Get a service that communicates to a Google API.

    Args:
        api_name: The name of the api to connect to.
        api_version: The api version to connect to.
        scopes: A list auth scopes to authorize for the application.
        key_file_location: The path to a valid service account JSON key file.

    Returns:
        A service that is connected to the specified API.
    """

    credentials = ServiceAccountCredentials.from_json_keyfile_name(
            key_file_location, scopes=scopes)

    # Build the service object.
    service = build(api_name, api_version, credentials=credentials)

    return service

def upload(file_name, title = False):
    if not title:
        title = file_name
    service = get_service(
            api_name='drive',
            api_version='v3',
            scopes=config.scopes,
            key_file_location=config.key_file_location)
    file_metadata = {'name': title, 'parents' : [config.folder_id]}
    media = MediaFileUpload(file_name, mimetype='application/zip')
    file = service.files().create(body=file_metadata,
                                        media_body=media,
                                        fields='id').execute()
    print ('Upload File ID: %s' % file.get('id'))
    return file.get('id')

if __name__ == '__main__':
    upload('test.txt')


