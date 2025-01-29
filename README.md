# FatSecret API Integration with FastAPI

This project provides a simple REST API wrapper around the FatSecret API using FastAPI. It allows users to search for food items and retrieve their nutritional information using FatSecret's database.

## Features

- OAuth2 authentication with FatSecret API
- Food search endpoint with pagination
- Error handling and response formatting
- Token caching for better performance

## Prerequisites

- Python 3.7+
- FatSecret API credentials (Client ID and Secret)
- pip (Python package manager)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/frzn23/fatsecret-persist
cd https://github.com/frzn23/fatsecret-persist
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install fastapi uvicorn requests
```

## Configuration

1. Sign up for a FatSecret API account at [FatSecret Platform API](https://platform.fatsecret.com/api/)
2. Obtain your API credentials (Client ID and Client Secret)
3. Open `app.py` and replace the placeholder credentials:
```python
CLIENT_ID = "your_client_id"
CLIENT_SECRET = "your_client_secret"
```

## Running the Application

1. Start the FastAPI server:
```bash
uvicorn app:app --reload
```

2. The API will be available at `http://127.0.0.1:8000`

## API Endpoints

### Search Foods

**Endpoint**: `/foods/search`

**Method**: GET

**Query Parameters**:
- `search_expression` (optional): Search term for foods
- `page_number` (optional): Page number (zero-based index, default: 0)
- `max_results` (optional): Number of results per page (default: 20, max: 50)

**Example Request**:
```bash
curl "http://127.0.0.1:8000/foods/search?search_expression=apple&page_number=0&max_results=20"
```

## Response Format

The API returns JSON responses in the following format:

```json
{
    "foods": {
        "food": [
            {
                "food_id": "string",
                "food_name": "string",
                "food_type": "string",
                "food_url": "string"
            }
        ],
        "max_results": "number",
        "page_number": "number",
        "total_results": "number"
    }
}
```

## Error Handling

The API implements proper error handling for various scenarios:

- Invalid API credentials
- Failed API requests
- Invalid parameters
- Network errors

Errors are returned with appropriate HTTP status codes and descriptive messages.

## Limitations

- This implementation uses the free tier of FatSecret API
- The `foods.search` endpoint has rate limits according to FatSecret's policies
- Token caching is done in-memory and will reset when the server restarts

## Documentation

For more detailed API documentation, visit:
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, please:
1. Check the FatSecret API documentation
2. Open an issue in the repository
3. Contact the maintainers

## Acknowledgments

- [FatSecret Platform API](https://platform.fatsecret.com/api/)
- [FastAPI](https://fastapi.tiangolo.com/)
