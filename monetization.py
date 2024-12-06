import os
from dotenv import load_dotenv
import google.ads.googleads.client
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request

load_dotenv()

def monetize_content(content):
    # Initialize Google AdSense client
    client_id = os.getenv('ADSENSE_CLIENT_ID')
    client_secret = os.getenv('ADSENSE_CLIENT_SECRET')
    refresh_token = os.getenv('ADSENSE_REFRESH_TOKEN')
    
    creds = Credentials(
        None,
        client_id=client_id,
        client_secret=client_secret,
        refresh_token=refresh_token,
        token_uri='https://oauth2.googleapis.com/token'
    )
    
    creds.refresh(Request())
    
    # Create AdSense client
    adsense = google.ads.googleads.client.GoogleAdsClient.load_from_env(
        credentials=creds
    )
    
    # Create ad unit
    ad_unit_service = adsense.get_service('AdUnitService')
    ad_unit_operation = ad_unit_service.ad_unit_path(
        customer_id=os.getenv('ADSENSE_CUSTOMER_ID'),
        ad_unit_id='example-ad-unit'
    )
    
    # Get ad code
    ad_code_response = ad_unit_service.get_ad_code(ad_unit_operation)
    ad_code = ad_code_response.ad_code
    
    # Insert ad code into blog post content
    monetized_content = f'{content}
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<ins class="adsbygoogle" style="display:inline-block;width:728px;height:90px" data-ad-client="{os.getenv("ADSENSE_PUBLISHER_ID")}" data-ad-slot="{ad_code}"></ins>
<script>(adsbygoogle = window.adsbygoogle || []).push({});</script>'
    
    return monetized_content
