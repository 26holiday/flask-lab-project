## Team Members and Roles

- **Member 1 (Backend)** – Works on Flask routes and backend logic  
- **Member 2 (Frontend)** – Works on HTML templates and connects frontend with backend  
- **Member 3 (DevOps)** – Handles Docker setup, testing, and CI/CD pipeline  

## Project Structure

```
flask-lab-project/
├── main/
│   ├── app.py              # Main Flask app
│   ├── requirements.txt    # Needed Python packages
│   ├── Dockerfile          # Docker setup
│   ├── tests/              # Tests
│   ├── templates/          # HTML files
│   └── static/             # CSS, JS, images
├── .github/workflows/
│   └── ci-cd.yml           # GitHub Actions file
├── member1_backend/
├── member2_frontend/
└── member3_devops/
```

## How to Run

### Requirements

- Python 3.11+
- Docker
- Git

### 1. Clone the Repo

```bash
git clone https://github.com/26holiday/flask-lab-project.git
cd flask-lab-project
```

### 2. Run Without Docker

```bash
cd main
pip install -r requirements.txt
python app.py
```

App runs at: `http://localhost:5000`

### 3. Run With Docker

```bash
cd main
docker build -t flask-lab-app .
docker run -p 5000:5000 flask-lab-app
```

Then open `http://localhost:5000`

## Testing

```bash
cd main
pytest tests/ -v
```

Expected output:

```
test_app.py::test_home PASSED
test_app.py::test_health PASSED
test_app.py::test_data_post PASSED
```

## API Endpoints

| Endpoint  | Method | What it does         |
| ---------- | ------- | ------------------- |
| `/`        | GET     | Shows homepage      |
| `/health`  | GET     | Health check route  |
| `/data`    | POST    | Accepts JSON data   |

Example:

```bash
curl http://localhost:5000/health
curl -X POST http://localhost:5000/data -H "Content-Type: application/json" -d '{"key":"value"}'
```

## CI/CD

GitHub Actions runs tests and builds Docker images automatically when someone pushes or makes a pull request to `main`.

Steps:
1. Test job – runs all tests  
2. Build job – builds Docker image  
3. Deploy job – checks if ready to deploy  

## Working Together

Each member has their own branch:

- `backend`
- `frontend`
- `devops`

### Steps to Contribute

```bash
git checkout -b backend   # or frontend/devops
# make changes
git add .
git commit -m "Added new feature"
git push origin backend
```

Then create a Pull Request on GitHub and ask for review.

## Docker Commands

```bash
docker build -t flask-lab-app .
docker run -p 5000:5000 flask-lab-app
docker stop flask-lab-app
docker rm flask-lab-app
docker logs flask-lab-app
```

## Adding New Packages

- Add them to `main/requirements.txt`
- Rebuild the Docker image

## Run Flask with Auto Reload

```bash
cd main
set FLASK_ENV=development  # Windows
export FLASK_ENV=development  # Linux/Mac
python app.py
```

## Dependencies

- Flask
- pytest

## Checklist

- Flask app with `/`, `/health`, `/data`
- Docker setup
- Tests with pytest
- CI/CD using GitHub Actions
- Team workflow with branches

## License

For learning use only.

## Contributing

1. Fork this repo  
2. Make changes  
3. Push to your branch  
4. Create a Pull Request  

**Repo:** https://github.com/26holiday/flask-lab-project
