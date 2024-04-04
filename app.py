import requests
import json

def get_seo_report(api_key, website_url):
    # PageSpeed Insights API setup
    api_url = f'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={website_url}&key={api_key}'
    
    # Fetch data from Google PageSpeed Insights API
    response = requests.get(api_url)
    data = response.json()
    
    # Extract relevant SEO data if it exists
    categories = data.get('lighthouseResult', {}).get('categories', {})
    performance = categories.get('performance', {}).get('score')
    seo = categories.get('seo', {}).get('score')

    if performance is not None and seo is not None:
        performance_score = performance * 100
        seo_score = seo * 100
        message = f'SEO Report for {website_url}: Performance Score: {performance_score}, SEO Score: {seo_score}'
    else:
        message = f'Unable to retrieve the full SEO data for {website_url}.'
    
    print(message)

# Replace 'your-api' with your actual Google PageSpeed Insights API key
api_key = 'your-api'  
website_url = 'your-website'

# Call the function to get the SEO report
get_seo_report(api_key, website_url)
