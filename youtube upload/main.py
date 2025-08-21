from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
import os
import json

# 1. Authenticate
SCOPES = [
    "https://www.googleapis.com/auth/youtube.upload",
    "https://www.googleapis.com/auth/youtube.force-ssl"
]
flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", SCOPES)
credentials = flow.run_local_server(port=0)
youtube = build("youtube", "v3", credentials=credentials)

# Playlist ID where you want to add the uploaded video
PLAYLIST_ID = "PLmWo09RLhFvLEUujNZ1yR8bUP6SUEXJ7J"

# 2. Your shorts list
try:
    with open('shorts_list.json', 'r') as file:
        shorts_list = json.load(file)
except FileNotFoundError:
    print("shorts_list.json not found")
    shorts_list = []  # or some default value
except json.JSONDecodeError:
    print("Invalid JSON in shorts_list.json")
    shorts_list = []

# 3. Upload each short
for short in shorts_list:
    print(f"Uploading: {short['title']}")
    media = MediaFileUpload(short["file"], chunksize=-1, resumable=True)

    # Upload video
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
    video_id = response.get("id")
    print("Uploaded video ID:", video_id)

    # Add video to playlist
    youtube.playlistItems().insert(
        part="snippet",
        body={
            "snippet": {
                "playlistId": PLAYLIST_ID,
                "resourceId": {
                    "kind": "youtube#video",
                    "videoId": video_id
                }
            }
        }
    ).execute()
    print(f"Added video {video_id} to playlist {PLAYLIST_ID}")
