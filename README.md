
# FTM OTT Genie

FTM OTT Genie is a web application that allows users to download OTT platform videos by providing the video link. The app is built using Flask for the backend and HTML/CSS/JS for the frontend.

## Features
- Download videos from free OTT platforms by providing the link.
- Custom file name and progress bar for download tracking.

## Installation

To run the app locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/ftmowner/FTM-OTT-GENIE.git
   cd FTM-OTT-GENIE
   ```
2. Create a virtual environment and install dependencies:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r backend/requirements.txt
```

3. Run the Flask application:
```bash
python backend/app.py
```

4. Open a browser and go to http://127.0.0.1:5000 to access the application.



### Deploying to Render

You can deploy the FTM OTT Genie application with Render by clicking the button below:

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/ftmowner/FTM-OTT-GENIE)


### Manual Deployment on Render

1. Fork or clone this repository.

2. Create a new web service on Render.

3. Choose your repository and branch (main).

4. Define the Build Command:
  ```bash pip install -r backend/requirements.txt.
  ```

5.Define the Start Command: gunicorn backend.app:app.

6. Click Create Web Service to deploy.
 
