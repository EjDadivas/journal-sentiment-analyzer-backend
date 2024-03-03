"# journal-sentiment-analyzer-backend" 

# Setup Guide

## Step 1: Create MongoDB and Get Connection String

1. Go to the [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) website.
2. Create a new account or sign in to your existing account.
3. Create a new cluster.
4. Once your cluster is set up, click on "CONNECT".
5. Add your current IP address to the IP whitelist and create a MongoDB user.
6. Choose "Connect your application".
7. Copy the connection string and replace `<password>` with your MongoDB user's password.

## Step 2: Set Up Environment Variables

Create a new file named `.env` in the root directory of your project and add the following line:

```env
MONGODB_URL=<Your MongoDB Connection String>
```
Replace `<Your MongoDB Connection String>` with the connection string you got from MongoDB Atlas.
## Step 3: Clone the Repository
Run the following command in your terminal to clone the repository:

```bash
git clone <repository-url>
```
Replace `<repository-url> `with the URL of the repository you want to clone.

## Step 4: Create and Activate a Virtual Environment
Navigate to the project directory and run the following commands to create and activate a virtual environment:
```bash
python -m venv venv
venv/Scripts/activate
```
## Step 5: Install the Requirements
Run the following command to install the requirements from requirements.txt:
```bash
pip install -r requirements.txt
```

## Step 6: Run the Server
Run the following command to start the Uvicorn server:
```bash
uvicorn app.main:app --reload
```
Replace main with the name of your Python file and app with the name of your FastAPI application.

## Step 7: Go to the Documentation
Open your web browser and go to http://127.0.0.1:8000/docs to view the Swagger UI documentation for your API.