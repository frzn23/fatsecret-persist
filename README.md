```markdown
# FatSecret Food Search API

This project provides a FastAPI-based wrapper for interacting with the FatSecret Food Database API. It enables you to search for foods and retrieve information through an easy-to-use RESTful API interface.

## Features

- **OAuth2 Authentication**: Automatically handles token generation for authenticating with the FatSecret API.
- **Food Search**: Search for food items using customizable parameters like search term, pagination, and result limits.
- **Query Options**: Supports optional parameters such as including sub-categories or food images in the search results.

## Prerequisites

To run this project, you will need:

1. Python 3.9 or later.
2. FatSecret API credentials:
   - `CLIENT_ID`
   - `CLIENT_SECRET`

## Installation

1. **Clone the repository**:

   ```bash
   git clone [https://github.com/your-username/fatsecret-food-search-api.git](https://github.com/your-username/fatsecret-food-search-api.git)
   cd fatsecret-food-search-api
   ```

2. **Set up a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Add your FatSecret API credentials:**

   Replace the `CLIENT_ID` and `CLIENT_SECRET` placeholders in the code with your actual FatSecret API credentials.

## Usage

1. **Run the FastAPI server:**

   ```bash
   uvicorn app:app --reload
   ```

2. **Access the API documentation:**

   Open your browser and navigate to `http://127.0.0.1:8000/docs` to explore the interactive Swagger UI.

3. **Example Request:**

   Search for foods using the `/foods/search` endpoint. For example:

   ```
   GET [http://127.0.0.1:8000/foods/search?search_expression=Cheerios&page_number=1&max_results=10](http://127.0.0.1:8000/foods/search?search_expression=Cheerios&page_number=1&max_results=10)
   ```

## API Endpoints

### `GET /foods/search`

Search the FatSecret food database based on the query parameters.

**Query Parameters:**

- `search_expression` (string, optional): The term to search for.
- `page_number` (int, default: 0): The page index (zero-based).
- `max_results` (int, default: 20): Number of results to return per page (1–50).
- `include_sub_categories` (bool, default: false): Whether to include sub-categories in the results.
- `include_food_images` (bool, default: false): Whether to include food images in the results.

**Example Request:**

```bash
curl -X GET "[http://127.0.0.1:8000/foods/search?search_expression=Cheerios&page_number=1&max_results=10](http://127.0.0.1:8000/foods/search?search_expression=Cheerios&page_number=1&max_results=10)" -H "accept: application/json"
```

## Error Handling

The API provides descriptive error messages for:

- Missing OAuth2 credentials.
- Invalid or expired access tokens.
- API request failures.

## Deployment

To deploy this project, consider hosting it on a platform like Heroku, AWS, or Google Cloud. For example:

**Heroku Deployment Steps:**

1. Create a `Procfile` with the following content:

   ```
   web: uvicorn app:app --host 0.0.0.0 --port ${PORT}
   ```

2. Push the code to your Heroku repository and deploy:

   ```bash
   git push heroku app
   ```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License.

## Acknowledgments

- FastAPI: The Python web framework used in this project.
- FatSecret: The API powering the food search functionality.
