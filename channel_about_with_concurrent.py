from pprint import pprint
from pytubefix import Search, Channel
import time
import re

pattern = r"\"(\d+(?:\.\d+)?[KMB]?)\s+subscribers\""
pattern = r"\"content\":\"(\d+(?:\.\d+)?[KMB]?)\s+subscribers\""


# youtube_data_list.append({'keyword': keyword,
#                                                               'youtube_list': line_complete, 
#                                                               'volume': volume })

# def get_video_data_with_subscribers_12_28_2024(keyword_arg, line_complete, volume):
def get_video_data_with_subscribers_12_28_2024_with_concurrent(youtube_data):
    compete_dictionary = []
    videos = Search("python").videos
    videos = Search(youtube_data['keyword']).videos
    match_list = []
    print(youtube_data['volume'])
    volume2 = float(youtube_data['volume'].replace(',',''))
    if volume2 > 2000:
        for video in videos[:5]:
      

            channel = Channel(video.channel_url)
      
       
            about_html = channel.about_html
            matches = re.search(pattern, about_html)
          
            match_list.append(matches.group(1))
       
        time.sleep(5)
        print(match_list)
        less_than_10k_list = []
        
        for value in match_list:
            if value:
                numeric_value = convert_to_number(value)
                if numeric_value < 10000:
              
                    less_than_10k_list.append(value)
        if len(less_than_10k_list) >= 3:
            print("WE CAN COMPETE!") 
            print(less_than_10k_list)
            print(youtube_data['volume'])
            print(youtube_data['youtube_list'])
            compete_dictionary.append({'compete_list': str(less_than_10k_list), 'keyword_arg': youtube_data['keyword'],'line_complete': youtube_data['youtube_list'] })

            return compete_dictionary
    else: 
        return None    
    # print(compete_dictionary)
    # from pprint import pprint 
    # pprint(compete_dictionary)

def get_video_data():
    videos = Search("python").videos
    videos = Search("email marketing for beginners").videos

    for video in videos:
        print(video.title)
        print(video.views)
        channel = Channel(video.channel_url)
        print(channel.channel_name)
        about_html = channel.about_html
        matches = re.search(pattern, about_html)
        print(matches)
        print(matches.group(1))
        print("="*50)


def get_video_data_with_subscribers():
    videos = Search("python").videos
    videos = Search("robert kiyosaki books").videos

    for video in videos[:5]:
        print(video.title)
        print(video.views)
        channel = Channel(video.channel_url)
        print(channel.channel_name)
        print(channel.channel_id)
        print(channel.channel_url)
        about_html = channel.about_html
        matches = re.search(pattern, about_html)
        print(matches)
        print(matches.group(1))
        print("="*50)


def get_video_data_with_subscribers_with_views_per_minute(keyword_arg, line_complete):
    videos = Search("python").videos
    videos = Search(keyword_arg).videos
    match_list = []
    for video in videos[:5]:
        print(video.title)
        print(video.views)
        # print(video.views_per_hour)
        channel = Channel(video.channel_url)
        print(channel.channel_name)
        print(channel.channel_id)
        print(channel.channel_url)
        print(keyword_arg)
        print(line_complete)
        about_html = channel.about_html
        matches = re.search(pattern, about_html)
        print(matches)
        print(matches.group(1))
        match_list.append(matches.group(1))
        print("="*50)
    time.sleep(5)
    print(match_list)

compete_dictionary = []
def get_video_data_with_subscribers_12_26_2024(keyword_arg, line_complete, volume):
    videos = Search("python").videos
    videos = Search(keyword_arg).videos
    match_list = []
    print(volume)
    volume2 = float(volume.replace(',',''))
    if volume2 > 10000:
        for video in videos[:5]:
            # print(video.title)
            # print(video.views)

            channel = Channel(video.channel_url)
            # print(channel.channel_name)
            # print(channel.channel_id)
            # print(channel.channel_url)
            # print(keyword_arg)
            # print(line_complete)
            about_html = channel.about_html
            matches = re.search(pattern, about_html)
            # print(matches)
            # print(matches.group(1))
            match_list.append(matches.group(1))
            # print("="*50)
        time.sleep(5)
        print(match_list)
        less_than_10k_list = []
        
        for value in match_list:
            if value:
                # print(value)
                numeric_value = convert_to_number(value)
                if numeric_value < 10000:
                    # print(f"{value} -> {numeric_value} is less than 10K")
                    less_than_10k_list.append(value)
        if len(less_than_10k_list) >= 3:
            print("WE CAN COMPETE!") 
            print(less_than_10k_list)
            print(keyword_arg)
            print(line_complete)
            compete_dictionary.append({'compete_list': str(less_than_10k_list), 'keyword_arg': keyword_arg,'line_complete': line_complete })


    # print(compete_dictionary)
    from pprint import pprint 
    pprint(compete_dictionary)


def convert_to_number(s):
    if 'K' in s:
        return float(s.replace('K', '')) * 1000
    elif 'M' in s:
        return int(2000000)
    else:
        return int(s)
# get_video_data_with_subscribers()
# get_video_data_with_subscribers_with_views_per_minute()