from pprint import pprint
from apiclient.discovery import build
from apiclient.http import MediaFileUpload
from oauth2client.service_account import ServiceAccountCredentials
import config
import looter
import sheet

def main():
    is_handle = sheet.get_next_handle()
    print('Processing \'%s\'' % is_handle)
    download_result = looter.download(is_handle)

    if download_result.returncode:
        msg = download_result.stderr.decode('utf-8')
        sheet.set_handle_result(is_handle, msg)
    else:
        looter.zip(is_handle)
        id = looter.upload(is_handle)
        msg = 'https://docs.google.com/uc?id=%s' % id
        sheet.set_handle_result(is_handle, msg)

if __name__ == '__main__':
    main()    




