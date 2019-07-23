from pprint import pprint
from datetime import datetime
from apiclient.discovery import build
from apiclient.http import MediaFileUpload
from oauth2client.service_account import ServiceAccountCredentials
import config
import looter

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

def get_spreadsheets_service():
    # Authenticate and construct service.
    service = get_service(
            api_name='sheets',
            api_version='v4',
            scopes=config.scopes,
            key_file_location=config.key_file_location)

    return service.spreadsheets()


def get_next_handle():

    # Authenticate and construct service.
    service = get_service(
            api_name='sheets',
            api_version='v4',
            scopes=config.scopes,
            key_file_location=config.key_file_location)

    sheet = service.spreadsheets()
    result = get_spreadsheets_service().values().get(spreadsheetId=config.sheet_id,
                                range="A2:B").execute()
    values = result.get('values', [])

    for (index, row) in enumerate(values):
        if(len(row) == 1):
            return row[0]

def set_handle_result(is_handle, info):

    result = get_spreadsheets_service().values().get(spreadsheetId=config.sheet_id,
                                range="A2:B").execute()
    values = result.get('values', [])

    for (index, row) in enumerate(values):
        if(row[0] == is_handle and len(row) == 1):
            range = "B%s:C%s" % (index+2, index+2) 
            values = [[str(info), get_date_stamp()]]
            print('Saving result in row %s: \'%s\'' % (index + 2, info))
            get_spreadsheets_service().values().update(
                spreadsheetId=config.sheet_id,
                range=range, 
                valueInputOption='RAW',
                body = { 'values': values}).execute()
            return 0
    raise Exception("Handle %s not found in spreadsheet" % is_handle)

def get_date_stamp():
    return datetime.now().strftime("%H:%M:%S (%d-%b-%Y)")

if __name__ == '__main__':
    main()    




