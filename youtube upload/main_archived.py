from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
import os

# 1. Authenticate
SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]
flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", SCOPES)
credentials = flow.run_local_server(port=0)
youtube = build("youtube", "v3", credentials=credentials)

# 2. Your shorts list (could be from CSV/JSON)
shorts_list = [
    {
        "file": "ms_ai102_50.mp4",
        "title": "AI-102 Prep: Make a Field Appear in Search Results | Azure AI Search",
        "description": "To include a field in search results, set its attribute to retrievable in the index definition.\n#AzureAI #AISearch #IndexDesign #AI102 #MicrosoftLearn #Certification #ExamPrep",
        "tags": ["AzureAI", "AISearch", "IndexDesign", "AI102", "MicrosoftLearn", "Certification", "ExamPrep"],
        "privacy": "private",  # will be 'private' until scheduled publish
        "publishAt": "2025-08-12T10:30:00Z",
        "categoryId": "28"
    }
]

for short in shorts_list:
    print(f"Uploading: {short['title']}")
    media = MediaFileUpload(short["file"], chunksize=-1, resumable=True)
    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": short["title"],
                "description": short["description"],
                "tags": short["tags"],
                "categoryId": short["categoryId"]
            },
            "status": {
                "privacyStatus": short["privacy"],
                "publishAt": short.get("publishAt"),
                "selfDeclaredMadeForKids": False
            }
        },
        media_body=media
    )
    response = request.execute()
    print("Uploaded video ID:", response.get("id"))
