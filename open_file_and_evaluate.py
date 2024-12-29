
import os

def channel_about_12_28_2024():
    # keywords text files/learn python-matching-terms-27-12-2024.txt
    keywords_to_search = [
        'learn python',
'python tutorial',
'learn python',
'python course',

    ]
    for kw in keywords_to_search:
        root_keyword = kw
        # base_path = r'C:\Users\thesm\OneDrive\Desktop\
        base_path = r'C:\Users\thesm\OneDrive\Desktop\keywords text files'
        file_list = ['-questions','-matching-terms','-related-keywords']
        for file_to_iterate in file_list:
            file_name = file_to_iterate 
            
            file_extension = '-27-12-2024.txt'

            file_name = f"{root_keyword}{file_name}"

            # Combine variables into the full file path
            file_path2 = os.path.join(base_path, file_name + file_extension)

            # Print the file path
            print(file_path2)
            # Adjust the path to the location of your file
            # file_path = 'C:\\Users\\thesm\\OneDrive\\Desktop\\python-related-keywords-vidiq-results-25-12-2024.txt'  # Windows
            file_path2 = os.path.join(base_path, file_name + file_extension)
         
            import re
            import channel_about
            pattern = r'Keyword:\s*(.*?),'
            pattern_volume = r'Search Volume:\s*(.*?), '
            line_list = []
            try:
                with open(file_path2, 'r', encoding='utf-8') as file:
                        for line in file:
                            if line: 
                                if "LOW" in line.upper():
                                    line_list.append(line)
                        for line in line_list:
                      
                            try:
                            
                                # print(line.strip()) 
                                text = line.strip()
                                match = re.search(pattern, text)
                                match2 = re.search(pattern_volume, text)
                                # Printing the extracted text
                                if match and match2:

                                    keyword = match.group(1)
                                    volume = match2.group(1)
                                    # print(line.strip()) 
                                    line_complete = line.strip()
                                    # print(keyword)
                                    # print(volume)

                                    channel_about.get_video_data_with_subscribers_12_28_2024(keyword, line_complete, volume)
                                    # print('='*100)
                                
                                    
                                else:
                                    print("No match found.")
                            except Exception as e:
                                print("Hit Exception:",e)   
                        
            except FileNotFoundError:
                print("The file was not found.")
            except Exception as e:
                print(f"An error occurred: {e}")


def channel_about_12_26_2024():
    # Define variables
    keywords_to_search = [
        'digital marketing',
'social media marketing',
'content marketing',
'email marketing',
'affiliate marketing',
'influencer marketing',
'marketing strategy',
'marketing automation',
'search engine optimization',
'online marketing',
'marketing plan',
    ]
    for kw in keywords_to_search:
        root_keyword = kw
        base_path = r'C:\Users\thesm\OneDrive\Desktop'
        file_list = ['-questions','-matching-terms','-related-keywords']
        for file_to_iterate in file_list:
            file_name = file_to_iterate 
            
            file_extension = '-27-12-2024.txt'

            file_name = f"{root_keyword}{file_name}"

            # Combine variables into the full file path
            file_path2 = os.path.join(base_path, file_name + file_extension)

            # Print the file path
            print(file_path2)
            # Adjust the path to the location of your file
            # file_path = 'C:\\Users\\thesm\\OneDrive\\Desktop\\python-related-keywords-vidiq-results-25-12-2024.txt'  # Windows
            file_path2 = os.path.join(base_path, file_name + file_extension)
            # file_path = '/Users/YourUsername/Desktop/example.txt'  # macOS
            # file_path = '/home/YourUsername/Desktop/example.txt'  # Linux
            # C:\Users\thesm\OneDrive\Desktop\open_file_and_evaluate.py
            # Open the file and read through each line

            import re
            import channel_about
            pattern = r'Keyword:\s*(.*?),'
            pattern_volume = r'Search Volume:\s*(.*?), '
            line_list = []
            try:
                with open(file_path2, 'r', encoding='utf-8') as file:
                        for line in file:
                            if line: 
                                if "LOW" in line.upper():
                                    line_list.append(line)
                        for line in line_list:
                            # from pprint import pprint 
                            # pprint(line_list)
                            try:
                            
                                # print(line.strip()) 
                                text = line.strip()
                                match = re.search(pattern, text)
                                match2 = re.search(pattern_volume, text)
                                # Printing the extracted text
                                if match and match2:
                                    # print(match.group(1))  # This prints the captured group from the regex
                                    keyword = match.group(1)
                                    volume = match2.group(1)
                                    # print(line.strip()) 
                                    line_complete = line.strip()
                                    # print(keyword)
                                    # print(volume)

                                    channel_about.get_video_data_with_subscribers_12_26_2024(keyword, line_complete, volume)
                                    # print('='*100)
                                
                                    
                                else:
                                    print("No match found.")
                            except Exception as e:
                                print("Hit Exception:",e)   
                        
            except FileNotFoundError:
                print("The file was not found.")
            except Exception as e:
                print(f"An error occurred: {e}")


def channel_about():
    # Adjust the path to the location of your file
    file_path = 'C:\\Users\\thesm\\OneDrive\\Desktop\\software development-matching-terms-vidiq-results-25-12-2024.txt'  # Windows
    # file_path = '/Users/YourUsername/Desktop/example.txt'  # macOS
    # file_path = '/home/YourUsername/Desktop/example.txt'  # Linux
    # C:\Users\thesm\OneDrive\Desktop\open_file_and_evaluate.py
    # Open the file and read through each line

    import re
    import channel_about
    pattern = r'Keyword:\s*(.*?),'
    line_list = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    if line: 
                        if "LOW" in line.upper():
                            line_list.append(line)
                for line in line_list:
                    # from pprint import pprint 
                    # pprint(line_list)
                    try:
                    
                        # print(line.strip()) 
                        text = line.strip()
                        match = re.search(pattern, text)
                        # Printing the extracted text
                        if match:
                            # print(match.group(1))  # This prints the captured group from the regex
                            keyword = match.group(1)
                            # print(line.strip()) 
                            line_complete = line.strip()

                            channel_about.get_video_data_with_subscribers_12_26_2024(keyword, line_complete)
                            # print('='*100)
                            
                        else:
                            print("No match found.")
                    except Exception as e:
                        print("Hit Exception:",e)   
                    
    except FileNotFoundError:
        print("The file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")



channel_about_12_28_2024()