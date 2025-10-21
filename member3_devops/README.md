# Member 3 - DevOps Engineer

## Responsibilities
- Handle Docker configuration
- Set up CI/CD pipeline
- Manage testing infrastructure
- Configure deployment environments

## Work Area
This directory contains DevOps-specific development work.

## Tasks Completed
- ✅ Created Dockerfile for containerization
- ✅ Set up GitHub Actions CI/CD pipeline
- ✅ Configured automated testing
- ✅ Implemented Docker build and push workflow

## CI/CD Pipeline Details

### Workflow Triggers
- Push to `main` branch
- Pull requests to `main` branch

### Pipeline Jobs
1. **Test Job**
   - Runs unit tests with pytest
   - Validates code quality
   
2. **Build Job**
   - Builds Docker image
   - Tests container functionality
   - Optionally pushes to Docker Hub

3. **Deploy Job**
   - Confirms deployment readiness

## Docker Configuration

### Build Image
```bash
docker build -t flask-lab-app:latest -f main/Dockerfile .
```

### Run Container
```bash
docker run -d -p 5000:5000 flask-lab-app:latest
```

### Test Container
```bash
curl http://localhost:5000/health
```

## Docker Hub Setup (Optional)
Add GitHub Secrets:
- `DOCKER_USERNAME`: Your Docker Hub username
- `DOCKER_PASSWORD`: Your Docker Hub password or access token

## Future Enhancements
- Add container orchestration (Kubernetes)
- Implement staging environment
- Add performance monitoring
- Set up automated backups
