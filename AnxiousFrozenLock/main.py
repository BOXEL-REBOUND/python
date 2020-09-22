from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials

auth.authenticate_user()
gauth = GoogleAuth()
gauth.credentials = GoogleCredentials.get_application_default()
drive = GoogleDrive(gauth)

downloaded = drive.CreateFile({'id':'1Is4FcZlfqZyNSShTrJONE3xyCj3hXRo4'})
downloaded.GetContentFile('submission1.csv')

downloaded = drive.CreateFile({'id':'1BDL9kiH9UpzyEBYYV0rLRW_XoY8LxgF1'})
downloaded.GetContentFile('submission2.csv')

downloaded = drive.CreateFile({'id':'1bhZa2avIf6NEIlUeclJ3En8hn9Af-TZ8'})
downloaded.GetContentFile('submission3.csv')

downloaded = drive.CreateFile({'id':'1NnjEw0Pbpd-337PEhfKYvFEPtQBBVUl4'})
downloaded.GetContentFile('submission10.csv')

downloaded = drive.CreateFile({'id':'1koEAL-c1cQq3JefXBE7pNoctDanpwSrG'})
downloaded.GetContentFile('submission11.csv')
