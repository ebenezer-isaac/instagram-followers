import os
import webbrowser
from bs4 import BeautifulSoup

def extract_text_from_span(html_content, class_name):
    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all span elements with the specified class name
    span_elements = soup.find_all('span', class_=class_name)

    # Extract and return the text content of each span element
    text_list = [span.get_text() for span in span_elements]
    
    return text_list

def find_elements_not_in_followers(followers_list, following_list):
    return list(set(following_list) - set(followers_list))

def read_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def write_to_html(output_file_path, elements):
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write('<html><head><title>Output</title></head><body>')
        file.write('<h2>Elements in following not present in followers:</h2>')
        file.write('<ul>')
        for element in elements:
            # Prepend 'https://www.instagram.com/' to each element
            full_url = 'https://www.instagram.com/{}'.format(element)
            file.write('<li><a href="{}" target="_blank">{}</a></li>'.format(full_url, full_url))
        file.write('</ul></body></html>')

# File paths
followers_file_path = 'followers.txt'
following_file_path = 'following.txt'
class_name_to_extract = '_ap3a _aaco _aacw _aacx _aad7 _aade'
output_file_name = 'output.html'

# Get the current path of the script file
script_path = os.path.dirname(os.path.realpath(__file__))

# Construct the full output file path by prepending the script path
output_file_path = os.path.join(script_path, output_file_name)

# Read HTML content from files
followers_html_content = read_html_file(followers_file_path)
following_html_content = read_html_file(following_file_path)

# Extract text lists from HTML content
followers_text_list = extract_text_from_span(followers_html_content, class_name_to_extract)
following_text_list = extract_text_from_span(following_html_content, class_name_to_extract)

# Find elements in following not present in followers
elements_not_in_followers = find_elements_not_in_followers(followers_text_list, following_text_list)

# Write output to HTML file
write_to_html(output_file_path, elements_not_in_followers)

print("Output has been written to '{}'.".format(output_file_path))

# Open the HTML file with Chrome
chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"  # Adjust the path based on your system
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
webbrowser.get('chrome').open(output_file_path, new=2)
