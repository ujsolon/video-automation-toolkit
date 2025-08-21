from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
import os

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
shorts_list = [
    {
        "file": "ms_ai102_68.mp4",
        "title": "68. AI-102 Prep: Fix Word Doc Errors in Azure Document Intelligence",
        "description": """Azure AI Document Intelligence does not support Word files. Convert Word to PDF before submitting for analysis.

#AzureAI #DocumentIntelligence #AI102 #MicrosoftLearn #Certification #ExamPrep
""",
        "tags": ["AzureAI", "DocumentIntelligence", "AI102", "MicrosoftLearn", "Certification", "ExamPrep"],
        "privacy": "private",
        "publishAt": "2025-08-31T18:00:00Z",
        "categoryId": "28"
    },
    {
        "file": "ms_ai102_69.mp4",
        "title": "69. AI-102 Prep: Extract Invoices with Azure Document Intelligence",
        "description": """Use Analyze Invoice and Get Analyze Invoice Result API calls to extract data with the prebuilt invoice model.

#AzureAI #DocumentIntelligence #InvoiceAI #AI102 #MicrosoftLearn #Certification #ExamPrep
""",
        "tags": ["AzureAI", "DocumentIntelligence", "InvoiceAI", "AI102", "MicrosoftLearn", "Certification", "ExamPrep"],
        "privacy": "private",
        "publishAt": "2025-09-01T10:00:00Z",
        "categoryId": "28"
    },
    {
        "file": "ms_ai102_70.mp4",
        "title": "70. AI-102 Prep: Extract Receipts Data with Azure Document Intelligence",
        "description": """For scanned receipts, use the prebuilt receipts model to extract merchant, date, and total.

#AzureAI #DocumentIntelligence #ReceiptsAI #AI102 #MicrosoftLearn #Certification #ExamPrep
""",
        "tags": ["AzureAI", "DocumentIntelligence", "ReceiptsAI", "AI102", "MicrosoftLearn", "Certification", "ExamPrep"],
        "privacy": "private",
        "publishAt": "2025-09-01T18:00:00Z",
        "categoryId": "28"
    },
    {
        "file": "ms_ai102_71.mp4",
        "title": "71. AI-102 Prep: Training Custom Models in Document Intelligence",
        "description": """Training requires providing forms and associated JSON label files (ocr.json, labels.json, singlefields.json).

#AzureAI #DocumentIntelligence #CustomModel #AI102 #MicrosoftLearn #Certification #ExamPrep
""",
        "tags": ["AzureAI", "DocumentIntelligence", "CustomModel", "AI102", "MicrosoftLearn", "Certification", "ExamPrep"],
        "privacy": "private",
        "publishAt": "2025-09-02T10:00:00Z",
        "categoryId": "28"
    },
    {
        "file": "ms_ai102_72.mp4",
        "title": "72. AI-102 Prep: Base Model for ChatGPT in Azure OpenAI",
        "description": """Deploy gpt-35-turbo to access ChatGPT capabilities in Azure OpenAI.

#AzureAI #OpenAI #ChatGPT #gpt35turbo #AI102 #MicrosoftLearn #Certification #ExamPrep
""",
        "tags": ["AzureAI", "OpenAI", "ChatGPT", "gpt35turbo", "AI102", "MicrosoftLearn", "Certification", "ExamPrep"],
        "privacy": "private",
        "publishAt": "2025-09-02T18:00:00Z",
        "categoryId": "28"
    },
    {
        "file": "ms_ai102_73.mp4",
        "title": "73. AI-102 Prep: Control Creativity with Temperature Parameter",
        "description": """Adjust the temperature parameter to control randomness and creativity of model completions.

#AzureAI #OpenAI #Temperature #AI102 #MicrosoftLearn #Certification #ExamPrep
""",
        "tags": ["AzureAI", "OpenAI", "Temperature", "AI102", "MicrosoftLearn", "Certification", "ExamPrep"],
        "privacy": "private",
        "publishAt": "2025-09-03T10:00:00Z",
        "categoryId": "28"
    },
    {
        "file": "ms_ai102_74.mp4",
        "title": "74. AI-102 Prep: Which Playground Supports Conversation? | Azure OpenAI",
        "description": """Use the Chat playground for conversation-in, message-out scenarios.

#AzureAI #OpenAI #ChatPlayground #AI102 #MicrosoftLearn #Certification #ExamPrep
""",
        "tags": ["AzureAI", "OpenAI", "ChatPlayground", "AI102", "MicrosoftLearn", "Certification", "ExamPrep"],
        "privacy": "private",
        "publishAt": "2025-09-03T18:00:00Z",
        "categoryId": "28"
    },
    {
        "file": "ms_ai102_75.mp4",
        "title": "75. AI-102 Prep: Required Values for Azure OpenAI Requests",
        "description": """Key, Endpoint, and Deployment name are required to make requests to Azure OpenAI.

#AzureAI #OpenAI #APIKeys #AI102 #MicrosoftLearn #Certification #ExamPrep
""",
        "tags": ["AzureAI", "OpenAI", "APIKeys", "AI102", "MicrosoftLearn", "Certification", "ExamPrep"],
        "privacy": "private",
        "publishAt": "2025-09-04T10:00:00Z",
        "categoryId": "28"
    },
    {
        "file": "ms_ai102_76.mp4",
        "title": "76. AI-102 Prep: Endpoints in Azure OpenAI",
        "description": """The three endpoints are Completion, ChatCompletion, and Embeddings.

#AzureAI #OpenAI #Endpoints #AI102 #MicrosoftLearn #Certification #ExamPrep
""",
        "tags": ["AzureAI", "OpenAI", "Endpoints", "AI102", "MicrosoftLearn", "Certification", "ExamPrep"],
        "privacy": "private",
        "publishAt": "2025-09-04T18:00:00Z",
        "categoryId": "28"
    },
    {
        "file": "ms_ai102_77.mp4",
        "title": "77. AI-102 Prep: Best Endpoint for Conversations in Azure OpenAI",
        "description": """Use the ChatCompletion endpoint to generate the next response in a conversation.

#AzureAI #OpenAI #ChatCompletion #AI102 #MicrosoftLearn #Certification #ExamPrep
""",
        "tags": ["AzureAI", "OpenAI", "ChatCompletion", "AI102", "MicrosoftLearn", "Certification", "ExamPrep"],
        "privacy": "private",
        "publishAt": "2025-09-05T10:00:00Z",
        "categoryId": "28"
    },
    {
        "file": "ms_ai102_78.mp4",
        "title": "78. AI-102 Prep: How to Optimize Azure OpenAI Models",
        "description": """Provide clear and descriptive instructions to get better performance and more accurate results.

#AzureAI #OpenAI #PromptEngineering #AI102 #MicrosoftLearn #Certification #ExamPrep
""",
        "tags": ["AzureAI", "OpenAI", "PromptEngineering", "AI102", "MicrosoftLearn", "Certification", "ExamPrep"],
        "privacy": "private",
        "publishAt": "2025-09-05T18:00:00Z",
        "categoryId": "28"
    },
    {
        "file": "ms_ai102_79.mp4",
        "title": "79. AI-102 Prep: Purpose of System Message in a Prompt",
        "description": """System messages guide the model with instructions, context, or perspective for better responses.

#AzureAI #OpenAI #SystemMessage #AI102 #MicrosoftLearn #Certification #ExamPrep
""",
        "tags": ["AzureAI", "OpenAI", "SystemMessage", "AI102", "MicrosoftLearn", "Certification", "ExamPrep"],
        "privacy": "private",
        "publishAt": "2025-09-06T10:00:00Z",
        "categoryId": "28"
    },
    {
        "file": "ms_ai102_80.mp4",
        "title": "80. AI-102 Prep: Why Provide Conversation History to AI?",
        "description": """Conversation history lets AI maintain tone and context while allowing references to earlier messages.

#AzureAI #OpenAI #ConversationHistory #AI102 #MicrosoftLearn #Certification #ExamPrep
""",
        "tags": ["AzureAI", "OpenAI", "ConversationHistory", "AI102", "MicrosoftLearn", "Certification", "ExamPrep"],
        "privacy": "private",
        "publishAt": "2025-09-06T18:00:00Z",
        "categoryId": "28"
    }
]


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
