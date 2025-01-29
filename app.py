from fastapi import FastAPI, Query, HTTPException
from fastapi.responses import JSONResponse
import requests
from typing import Optional

app = FastAPI()

# OAuth credentials
CLIENT_ID = ""  # This is a dummy client ID, please replace it with your own client ID
CLIENT_SECRET = "" # This is a dummy secret key, please replace it with your own secret key
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
        payload = {"grant_type": "client_credentials"}
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
                detail="Failed to fetch access token",
            )
    return access_token


@app.get("/foods/search")
def search_foods(
    search_expression: Optional[str] = Query(None, description="Search term for foods"),
    page_number: int = Query(0, ge=0, description="Page number (zero-based index)"),
    max_results: int = Query(20, ge=1, le=50, description="Number of results per page"),
    include_sub_categories: Optional[bool] = Query(False, description="Include sub-categories"),
    include_food_images: Optional[bool] = Query(False, description="Include food images"),
):
    """
    Search the FatSecret food database based on user input.
    """
    token = get_access_token()
    headers = {"Authorization": f"Bearer {token}"}
    params = {
        "method": "foods.search.v3",
        "search_expression": search_expression,
        "page_number": page_number,
        "max_results": max_results,
        "include_sub_categories": str(include_sub_categories).lower(),
        "include_food_images": str(include_food_images).lower(),
        "format": "json",
    }

    response = requests.get(API_URL, headers=headers, params=params)

    if response.status_code == 200:
        return JSONResponse(content=response.json())
    else:
        raise HTTPException(
            status_code=response.status_code,
            detail="Failed to fetch food search results",
        )



