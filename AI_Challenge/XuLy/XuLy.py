import googleapiclient.discovery
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.http import MediaIoBaseDownload

# Thực hiện xác thực tương tự như trong câu trả lời trước

# Tải xuống tệp từ Google Drive
drive_service = build('drive', 'v3', credentials=creds)
file_id = 'your_file_id'  # ID của tệp trên Google Drive
request = drive_service.files().get_media(fileId=file_id)
file_name = 'my_code.py'  # Tên tệp bạn muốn tải xuống
with io.FileIO(file_name, 'wb') as fh:
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
