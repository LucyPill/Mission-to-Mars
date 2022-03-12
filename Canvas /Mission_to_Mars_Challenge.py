#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[2]:


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### Visit the NASA Mars News Site

# In[3]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[4]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


# In[5]:


slide_elem.find('div', class_='content_title')


# In[6]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[7]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### JPL Space Images Featured Image

# In[8]:


# Import Splinter and BeautifulSoup
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager


# In[9]:


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[10]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[11]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[12]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[13]:


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[14]:


# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Mars Facts

# In[15]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()


# In[16]:


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[17]:


df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[18]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[19]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[20]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []


# In[21]:


# 3. Write code to retrieve the image urls and titles for each hemisphere.

# 3.1 Create an empty list to hold new items:
item_list = []

# 3.2 parent element
image_list = img_soup.select('div.item')

# 3.3 append url to the image_list
for i in image_list:
    item_url = i.find('a')['href']
    item_list.append(item_url)
    
# 3.4 loop through pages for the hemisphere jpg ans the titles
for hemisphere in item_list:
    browser.visit(f'{url}{hemisphere}')
    hemisphere_html = browser.html
    hemisphere_soup = soup(hemisphere_html, 'html.parser')

    # jpg urls
    jpg = hemisphere_soup.select('div.downloads')
    for link in jpg:
        jpg_url = link.find('a')['href']
        
    # titles
    titles = hemisphere_soup.select('h2.title')
    for title in titles:
        hemisphere_title = title.text
        
    # addinf jpg urls and titles to the hemisphere_image_url
    hemisphere_image_urls.append({"title": hemisphere_title, "img_url": f'{url}{jpg_url}'})


# In[22]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[23]:


# 5. Quit the browser
browser.quit()


# # DONE!

# In[ ]:




