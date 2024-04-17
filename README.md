# supreme-parakeet

This submission was completed with Python 3.10. The required dependencies are available in ```requirements.txt```.

## To set up virtual environment
```bash
# Create virtual environment named .venv
python -m venv .venv

# Activate virtual environment
source .venv/bin/activate

# Install the required libraries
pip install -r requirements.txt
```

## Task 2
### To build the Docker image
```bash
docker build -t asr-api .
```

### To run the Docker image
```bash
docker run -p 8001:8001 asr-api
```

