from src.app import app

if __name__ == "__main__":
    import uvicorn #web server to serve our fastAPI app
    uvicorn.run(app, host="0.0.0.0", port=8000)
    