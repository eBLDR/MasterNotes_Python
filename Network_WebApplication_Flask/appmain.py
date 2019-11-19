from app import app

if __name__ == '__main__':
    # Using host 0.0.0.0 app is available to local network
    app.run(host='0.0.0.0', port=4000)
