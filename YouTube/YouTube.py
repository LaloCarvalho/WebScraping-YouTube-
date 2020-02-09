from apiclient.discovery import build
import matplotlib.pyplot as pd

#Add below your YouTube Keys
DEVELOPER_KEY = ""
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,developerKey=DEVELOPER_KEY)

#max_results = quantities of videos to search
def youtube_search(q, max_results=50,order="relevance", token=None, location=None, location_radius=None):

  #youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,developerKey=DEVELOPER_KEY)
  search_response = youtube.search().list(
            q=q,
            type="video",
            pageToken=token,
            order = order,
            part="id,snippet", 
            maxResults=max_results,
            location=location,
            locationRadius=location_radius).execute()
  
  videos = []
  
  for search_result in search_response.get("items", []):
   if search_result["id"]["kind"] == "youtube#video":
    videos.append(search_result["id"]["videoId"])
  return videos 

lista = []
def get_comment_threads(youtube, video_id):
        results = youtube.commentThreads().list(               
          part="snippet",                                      
          videoId=video_id,               
          textFormat="plainText"
        ).execute()                                                                                            
        
        for item in results["items"]:                                                              
          comment = item["snippet"]["topLevelComment"]                                             
          author = comment["snippet"]["authorDisplayName"]
          text = comment["snippet"]["textDisplay"]    
          published_at = comment["snippet"]["publishedAt"]    
          data = "Nome:  %s, Texto: %s, DataPublicação: %s" % (author, text, published_at)
          lista.append(data)
          #print(data)
        with open('Youtube.txt', 'w', encoding='utf-8') as save:
             save.writelines('\n'.join(lista))
        print(lista)
     

try:
	#Add below the key word
    for i in youtube_search(""):
        print('CONT:', i, get_comment_threads(youtube, i))
except:
    print('error')
