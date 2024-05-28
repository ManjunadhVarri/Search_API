# Video Search API

## Overview

The Video Search API allows users to search for videos based on their title, tags, and descriptions. The video data is stored in a JSON file and loaded into memory when the application starts. This API supports querying videos by title, description, and tags.

## Base URL

http://localhost:5000/

## Endpoints

### 1. Search Videos

**Endpoint:** `GET /search`

**Description:** Retrieves a list of videos that match the search criteria based on title, description, and tags.

#### Query Parameters

| Parameter      | Type   | Description                                                   | Required |
|----------------|--------|---------------------------------------------------------------|----------|
| `title`        | string | The title or part of the title of the video to search for.    | No       |
| `description`  | string | The description or part of the description of the video to search for. | No       |
| `tags`         | list   | A list of tags to search for in the video's genre IDs.        | No       |

**Note:** Making the query parameters optional enhances the usability and flexibility of the API. It allows users to search using any combination of title, description, and tags without requiring them to provide all criteria. This design approach makes the API more adaptable to different search scenarios and user needs.

## Project Structure

```
My_Flask_app/
├── application.py
├── data/
│   └── DataSet.json
├── requirements.txt
```

## Instructions for Running the API

1. **Create a virtual environment:**
   ```sh
   python -m venv venv
   ```

2. **Activate the virtual environment:**
   - On Windows:
     ```sh
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```sh
     source venv/bin/activate
     ```

3. **Install Flask and other dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Run the Flask application:**
   ```sh
   python app.py
   ```

5. **Access the API:** Open a web browser or use a tool like Postman to send requests to `http://localhost:5000/search` with the appropriate query parameters.

## Request Examples

- **To search for videos with "Godzilla" in the title:** `GET /search?title=Godzilla`
- **To search for videos with "explosive" in the description:** `GET /search?description=explosive`
- **To search for videos with the tags "878" and "28":** `GET /search?tags=878&tags=28`
- **To search for videos with all criteria combined:** `GET /search?title=Godzilla&description=showdown&tags=878&tags=28`
- **To get all videos:** `GET /search`

## Example Response

```json
[
  {
    "adult": false,
    "backdrop_path": "/j3Z3XktmWB1VhsS8iXNcrR86PXi.jpg",
    "genre_ids": [878, 28, 12],
    "id": 823464,
    "original_language": "en",
    "original_title": "Godzilla x Kong: The New Empire",
    "overview": "Following their explosive showdown, Godzilla and Kong must reunite against a colossal undiscovered threat hidden within our world, challenging their very existence – and our own.",
    "popularity": 7832.06,
    "poster_path": "/v4uvGFAkKuYfyKLGZnYj6l47ERQ.jpg",
    "release_date": "2024-03-27",
    "title": "Godzilla x Kong: The New Empire",
    "video": false,
    "vote_average": 7.249,
    "vote_count": 1920
  }
]
```

## Notes

- **Search Logic:** The search functionality is case-insensitive. The title and description parameters search for partial matches, while the tags parameter matches any of the provided tags in the genre IDs of the videos.
- **Performance:** This implementation loads all video data into memory at startup, which is efficient for small datasets but may require optimization for larger datasets or production environments.
- **Error Handling:** The API returns standard HTTP status codes to indicate the success or failure of a request.

## Common Status Codes

- `200 OK:` The request was successful, and the response contains the requested data.
- `400 Bad Request:` The request could not be understood or was missing required parameters.
- `500 Internal Server Error:` An error occurred on the server.


## Deployment to AWS Cloud

To upload the following application to AWS Cloud, we have two methods:

### Method 1: Directly in AWS Cloud Environment

In both methods, we use AWS Elastic Beanstalk, which is a service that allows you to easily deploy and manage applications in the cloud.

#### Configuration Files

1. **Create a folder named `.ebextensions`**
2. **Create a file named `python.config` inside the `.ebextensions` folder with the following content:**

```yaml
option_settings:
  aws:elasticbeanstalk:container:python:
    WSGIPath: app:app
```

> **.ebextensions Directory:** This directory contains configuration files that allow you to customize and automate the environment setup on AWS Elastic Beanstalk.

> **python.config File:** This file specifies environment options, particularly the WSGIPath, which is necessary for Elastic Beanstalk to know how to start your Flask application.

> **WSGIPath:** This setting points Elastic Beanstalk to the entry point of your Flask application, ensuring it runs correctly in the deployed environment.

Ensure the project structure is as follows:
```
My_Flask_app/
├── application.py
├── data/
│   └── DataSet.json
├── requirements.txt
└── .ebextensions/
    └── python.config
```

By using the `.ebextensions` directory and the `python.config` file, you ensure that your Flask application is configured and deployed correctly on AWS Elastic Beanstalk.

### Steps to Deploy Directly in AWS Cloud Environment

1. **Open AWS Console and search for Elastic Beanstalk. Click on "Create application".**
2. **Configure Environment:**
   - Select "Web server environment" in environment tier.
   - Give a name to your application (e.g., `flask_app`).
   - Leave the rest as default.

3. **Platform:**
   - Select "Python" for the platform.

4. **Prepare Application Code:**
   - Zip the following files: `app.py`, `data`, `requirements.txt`, `.ebextensions`.

5. **Upload the Code:**
   - In application code, select "Upload your code" and upload the zip file.

6. **Configure Service Access:**
   - Select "Create a new service role".
   - Select the EC2 keypair.

7. **Create IAM Role:**
   - Go to IAM and create a new role for EC2 with the necessary permissions.
   - Name the role `ec2_EBS_role`.

8. **Select the EC2 Instance Profile:**
   - Select `ec2_EBS_role`.

9. **Set up Networking, Database, and Tags:**
   - Use the default VPC.
   - Activate instance settings.

10. **Configure Instance Traffic and Scaling:**
    - Leave default settings.

11. **Configure Updates, Monitoring, and Logging:**
    - Select "Enhanced" for health report.

12. **Create the Elastic Beanstalk Environment:**
    - Wait for it to be created and copy the domain URL.

### Example Requests

- **Search for videos with "Godzilla" in the title:** `http://<your-env-url>.elasticbeanstalk.com/search?title=Godzilla`
- **Search for videos with "explosive" in the description:** `http://<your-env-url>.elasticbeanstalk.com/search?description=explosive`
- **Search for videos with the tags "878" and "28":** `http://<your-env-url>.elasticbeanstalk.com/search?genre_ids=878&genre_ids=28`
- **Combined search:** `http://<your-env-url>.elasticbeanstalk.com/search?title=Godzilla&description=showdown&genre_ids=878&genre_ids=28`
- **Get all videos:** `http://<your-env-url>.elasticbeanstalk.com/search`

#### Response

The response is a JSON array of video objects that match the search criteria.

```json
[
  {
    "adult": false,
    "backdrop_path": "/j3Z3XktmWB1VhsS8iXNcrR86PXi.jpg",
    "genre_ids": [878, 28, 12],
    "id": 823464,
    "original_language": "en",
    "original_title": "Godzilla x Kong: The New Empire",
    "overview": "Following their explosive showdown, Godzilla and Kong must reunite against a colossal undiscovered threat hidden within our world, challenging their very existence – and our own.",
    "popularity": 7832.06,
    "poster_path": "/v4uvGFAkKuYfyKLGZnYj6l47ERQ.jpg",
    "release_date": "2024-03-27",
    "title": "Godzilla x Kong: The New Empire",
    "video": false,
    "vote_average": 7.249,
    "vote_count": 1920
  }
]
```

## Methon2 (From VSCode)

### Initial Setup:

- Create an IAM user named 'demo user' and grant administrator access.
- Create Access Key and store them securely.

Ensure:
- AWS CLI is installed and configured in VSCode terminal.
- AWS Elastic Beanstalk CLI is installed in VSCode terminal.

### Initial Configuration:

Open a terminal and configure AWS CLI:

```bash
aws configure
```

Initialize Elastic Beanstalk:

```bash
eb init -p python-3.7 my-flask-app
```

### Deployment Steps:

#### Step 1: Create an Environment

```bash
eb create my-flask-env
```

#### Step 2: Deploy the Application

```bash
eb deploy --version-label v1.0.0
```

#### Step 3: Open the Application

```bash
eb open
```

### Testing the API

Using Postman:

- Testing the `/search` endpoint:
  - **URL**: `http://<your-env-url>.elasticbeanstalk.com/search`
  - **Method**: GET
  - **Parameters**:
    - `title`: Search for videos by title.
    - `description`: Search for videos by description.
    - `genre_ids`: Search for videos by genre IDs.

### Example Queries:

- **Search by Title**:
  - URL: `http://<your-env-url>.elasticbeanstalk.com/search?title=Godzilla`

- **Search by Description**:
  - URL: `http://<your-env-url>.elasticbeanstalk.com/search?description=showdown`

- **Search by Genre IDs**:
  - URL: `http://<your-env-url>.elasticbeanstalk.com/search?genre_ids=878&genre_ids=28`

- **Combined Search**:
  - URL: `http://<your-env-url>.elasticbeanstalk.com/search?title=Godzilla&description=showdown&genre_ids=878&genre_ids=28`

### Response:

The response is a JSON array of video objects that match the search criteria.

```json
[
  {
    "adult": false,
    "backdrop_path": "/j3Z3XktmWB1VhsS8iXNcrR86PXi.jpg",
    "genre_ids": [878, 28, 12],
    "id": 823464,
    "original_language": "en",
    "original_title": "Godzilla x Kong: The New Empire",
    "overview": "Following their explosive showdown, Godzilla and Kong must reunite against a colossal undiscovered threat hidden within our world, challenging their very existence – and our own.",
    "popularity": 7832.06,
    "poster_path": "/v4uvGFAkKuYfyKLGZnYj6l47ERQ.jpg",
    "release_date": "2024-03-27",
    "title": "Godzilla x Kong: The New Empire",
    "video": false,
    "vote_average": 7.249,
    "vote_count": 1920
  }
]
```

## Conclusion

This documentation provides a detailed overview of the Video Search API, including endpoint details, request parameters, response format, and usage examples. By following this guide, users can effectively query the video dataset based on their search criteria.
