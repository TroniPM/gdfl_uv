from __future__ import print_function

import httplib2
import os
import io
from apiclient.http import MediaIoBaseDownload

from arquivo import Arquivo

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/drive-python-quickstart.json

#SCOPES = 'https://www.googleapis.com/auth/drive.metadata.readonly'
SCOPES = 'https://www.googleapis.com/auth/drive'

CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'GDFL_UPM'
service = "" #usado para manter sessao
PATH_DOWNLOAD = "./mydrive/"

STRING_QUERY = "files(id, name, mimeType, version, fileExtension, size, parents)"

def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'drive-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def download_file(arquivo):
    global service
        
    if(arquivo.isGDFile == True):
        #isso vai baixar o arquivo pra offline SEMPRE como pdf
        #request = service.files().export_media(fileId=arquivo.id, mimeType='application/pdf')
        
        #crio um html e redireciono o usuário par abri-lo no navegador
        fo = open(PATH_DOWNLOAD + arquivo.name + ".html", "wb")
        fo.write('<meta http-equiv="refresh" content="0; url=https://docs.google.com/open?id=' + arquivo.id + '" />');
        fo.close()
    #quando for pasta, cria-la
    #if(arquivo.isFolder == True):
    #    if not os.path.exists(directory):
    #        os.makedirs(directory)
    else:
        request = service.files().get_media(fileId=arquivo.id)
        fh = io.FileIO(PATH_DOWNLOAD + arquivo.name, mode='wb')
        #fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print("Download %d."%int(status.progress() * 100))

def download_all_folders():
    global service
    
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('drive', 'v3', http=http)
    
    page_token = None
    while True:
        response = service.files().list(q="mimeType='application/vnd.google-apps.folder'",
                                              spaces='drive',
                                              fields='nextPageToken, ' + STRING_QUERY,
                                              pageToken=page_token).execute()
        for file in response.get('files', []):
            # Process change
            print('Found file: %s (%s)' % (file.get('name'), file.get('id')))
        page_token = response.get('nextPageToken', None)
        if page_token is None:
            break

def main():
    global service
    qtd_files = 10
    """Shows basic usage of the Google Drive API.

    Creates a Google Drive API service object and outputs the names and IDs
    for up to 10 files.
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('drive', 'v3', http=http)

    ##results = service.files().list(pageSize=qtd_files,fields="nextPageToken, " + STRING_QUERY).execute()
    ##items = results.get('files', [])

    ####for test####
    items = [{u'mimeType': u'application/vnd.google-apps.spreadsheet', u'version': u'348398', u'parents': [u'0B-aYr0S4sKhvRW9HZjdsNkVjS0U'], u'id': u'1qZuvQ8ceL3Vv1eg1UCHt2x7t79ITI17_kcW9iE3H9q0', u'name': u'Convidados'}, {u'mimeType': u'application/vnd.google-apps.spreadsheet', u'version': u'31', u'parents': [u'1pFEP2WJC8OE_gSDAnldME0czW9RYCKjZ'], u'id': u'1q8dm7Yrq-WalYCMjStMT61HCLzECSNZAVurb1YSKFxs', u'name': u'VII SOS - Inscri\xe7\xe3o (respostas)'}, {u'mimeType': u'application/vnd.google-apps.document', u'version': u'317353', u'parents': [u'0ByujnwiFiZ1lWlhVNHR0RW4tcjQ'], u'id': u'1hQUcOxjvtEQmxplIk1I8bsACvc-K-dx4RrDZhK4nLeI', u'name': u'III SOS - Programacao.docx'}, {u'mimeType': u'application/vnd.openxmlformats-officedocument.wordprocessingml.document', u'name': u'Curso de Batismo INSCRI\xc7\xc3O.docx', u'version': u'3', u'parents': [u'1c2bJ3sZzN_3HBidPQE6iJKNThEhZDP4N'], u'fileExtension': u'docx', u'id': u'1St0k0BWrLMezn2RuYGBssZ63Rwe0QU8w', u'size': u'15587'}, {u'mimeType': u'application/vnd.google-apps.form', u'version': u'18', u'parents': [u'0ByujnwiFiZ1lNk41RHhES0ZVdFE'], u'id': u'1-oWMByigUTZu7HW6AUmdhCADxLYahQbcEPxcOzZ7ky4', u'name': u'Novo nome CLG'}, {u'mimeType': u'application/vnd.google-apps.form', u'version': u'20', u'parents': [u'1c2bJ3sZzN_3HBidPQE6iJKNThEhZDP4N'], u'id': u'1CAsM3ZB_UeD5LlhKynLeA_6lNExNiFlpdSNAyGVPKa8', u'name': u'Inscri\xe7\xe3o - Retiro Espiritual IK 2018'}, {u'mimeType': u'application/vnd.google-apps.spreadsheet', u'version': u'61', u'parents': [u'0B-aYr0S4sKhvRW9HZjdsNkVjS0U'], u'id': u'1nH7e3XpEhLtT-WpoumNmS_zvvAZf0GiinzHohJVHHmM', u'name': u'confirma\xe7\xf5es'}, {u'mimeType': u'application/vnd.google-apps.form', u'version': u'23', u'parents': [u'1pFEP2WJC8OE_gSDAnldME0czW9RYCKjZ'], u'id': u'1rPlP_U4O1-DjS5eY8A5RjJ2zmIhK6_pP4Uhqo_8i2Vk', u'name': u'VII SOS - Inscri\xe7\xe3o'}, {u'mimeType': u'application/vnd.google-apps.document', u'version': u'38', u'parents': [u'0B-aYr0S4sKhvRW9HZjdsNkVjS0U'], u'id': u'1inQSlUk-vl17-vmSTO7N1yQ6lAg9UKaRl5qApHvelG0', u'name': u'Presentes.docx'}, {u'mimeType': u'application/vnd.google-apps.document', u'version': u'78', u'parents': [u'0B-aYr0S4sKhvRW9HZjdsNkVjS0U'], u'id': u'1twVIYlBvk5ObK8ienam6YKD-JwXTX5MEqrtsBlEGxUk', u'name': u'Confirma\xe7\xf5es - Camila'}]
    #print(items)
    #print("\n\n\n\n\n")
    
    if not items:
        print('No files found.')
    else:
        print('Files (%d):'%len(items))
	#print("QUANTIDADE DOS ARQUIVOS: %s"%len(items))
        for item in items:
            arq = Arquivo(item)
            #print(arq)
            print(arq.id)
            print(arq.name)
            print(arq.mimeType)
            print("isGDFile: " + str(arq.isGDFile))
            print("isFolder: " + str(arq.isFolder))
            print("....:DOWNLOAD:....")
            download_file(arq)
            print()
			
if __name__ == '__main__':
    #main()
    download_all_folders()
    a = raw_input("Press enter to exit")
