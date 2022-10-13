from youtubesearchpython import VideosSearch
import youtube_dl

from replit import audio


def ytbsearch(query):
  videosSearch = VideosSearch(str(query), limit=1)
  result = videosSearch.result()
  '''print(result)
  print("-------------")
  print(result['result'][0]['id'])'''
  return result['result'][0]['id']


def dlmp3(input):
  video_url = input
  video_info = youtube_dl.YoutubeDL().extract_info(url=video_url,
                                                   download=False)
  filename = f"{video_info['title']}.mp3"
  options = {
    'format': 'bestaudio/best',
    'keepvideo': False,
    'outtmpl': filename,
  }

  with youtube_dl.YoutubeDL(options) as ydl:
    ydl.download([video_info['webpage_url']])

  print("Download complete... {}".format(filename))
  return filename

filename = dlmp3(ytbsearch("saul goodman 3d itsnickford"))
print(filename)
audio.play_file(str(filename))
print("played")