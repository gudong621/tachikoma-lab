import urllib.request
import re
import os
import datetime

def collect_apod():
    url = 'https://apod.nasa.gov/apod/astropix.html'
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read().decode('utf-8')
        
        # Extract title using Regex
        title_match = re.search(r'<b>(.*?)</b>', html)
        title = title_match.group(1).strip() if title_match else "Daily Space Image"
        
        # Extract image link using Regex
        img_match = re.search(r'<img src="(image/.*?)"', html)
        if not img_match:
            print('No image found today.')
            return
        
        img_rel_url = img_match.group(1)
        img_url = 'https://apod.nasa.gov/apod/' + img_rel_url
        
        # Extract explanation (coarse extraction)
        explanation_match = re.search(r'<b> Explanation: </b>(.*?)<p>', html, re.DOTALL)
        explanation = explanation_match.group(1).strip() if explanation_match else ""
        explanation = re.sub('<[^<]+?>', '', explanation) # Strip HTML tags
        
        # Save logic
        today = datetime.date.today().isoformat()
        base_dir = os.path.dirname(os.path.abspath(__file__))
        folder = os.path.join(base_dir, '..', 'gallery', today)
        os.makedirs(folder, exist_ok=True)
        
        # Download image
        urllib.request.urlretrieve(img_url, os.path.join(folder, 'image.jpg'))
            
        # Write markdown
        with open(os.path.join(folder, 'README.md'), 'w', encoding='utf-8') as f:
            f.write(f'# {title}\n\nDate: {today}\n\n![Daily Space]({img_url})\n\n## Explanation\n{explanation}\n')
        
        print(f'Successfully collected APOD: {title}')
    except Exception as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    collect_apod()
