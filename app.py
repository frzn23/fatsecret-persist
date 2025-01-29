from fastapi import FastAPI, Query, HTTPException
from fastapi.responses import JSONResponse
import requests
from typing import Optional

app = FastAPI()

# OAuth credentials
CLIENT_ID = ""  # Replace with your client ID
CLIENT_SECRET = "" # Replace with your secret key
TOKEN_URL = "https://oauth.fatsecret.com/connect/token"
API_URL = "https://platform.fatsecret.com/rest/server.api"

# Cache the token globally
access_token = None

def get_access_token():
    """
    Fetch and cache the OAuth2 access token.
    """
    global access_token
    if not access_token:
        payload = {
            "grant_type": "client_credentials",
            "scope": "basic"  # Changed to basic scope
        }
        response = requests.post(
            TOKEN_URL,
            data=payload,
            auth=(CLIENT_ID, CLIENT_SECRET),
        )
        if response.status_code == 200:
            access_token = response.json()["access_token"]
        else:
            raise HTTPException(
                status_code=response.status_code,
                detail=f"Failed to fetch access token: {response.text}"
            )
    return access_token

@app.get("/foods/search")
def search_foods(
    search_expression: Optional[str] = Query(None, description="Search term for foods"),
    page_number: int = Query(0, ge=0, description="Page number (zero-based index)"),
    max_results: int = Query(20, ge=1, le=50, description="Number of results per page"),
):
    """
    Search the FatSecret food database based on user input.
    """
    token = get_access_token()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    params = {
        "method": "foods.search",  # Changed to basic foods.search method
        "search_expression": search_expression,
        "page_number": page_number,
        "max_results": max_results,
        "format": "json",
    }
    
    try:
        response = requests.get(API_URL, headers=headers, params=params)
        response.raise_for_status()
        return JSONResponse(content=response.json())
    except requests.exceptions.RequestException as e:
        raise HTTPException(
            status_code=response.status_code if hasattr(e, 'response') else 500,
            detail=f"Failed to fetch food search results: {str(e)}"
        )
