# TaskFlow – To-Do REST API

Small Flask API used for the ITDSE14 practical (Software Engineering & Agile Development).

| Method | Endpoint | Purpose |
|---|---|---|
| GET | /health | Liveness check |
| GET | /tasks?done=true\|false | List / filter tasks |
| POST | /tasks | Create `{ "title": "..." }` |
| GET | /tasks/{id} | Get one |
| PUT | /tasks/{id} | Update `title` / `done` |
| DELETE | /tasks/{id} | Delete |

## Run locally
```bash
pip install -r requirements-dev.txt
python wsgi.py            # http://localhost:5000
pytest -v                 # run tests
```

## Docker
```bash
docker build -t taskflow:local .
docker run -p 5000:5000 taskflow:local
curl localhost:5000/health
```

## Kubernetes (minikube)
```bash
minikube start
minikube image load taskflow:local     # or: eval $(minikube docker-env) then docker build
kubectl apply -f k8s/
kubectl rollout status deployment/taskflow
kubectl get pods,svc
minikube service taskflow --url        # open this URL, add /health
```

## CI/CD
GitHub Actions (`.github/workflows/ci.yml`): test -> docker build + smoke test -> deploy to a kind cluster.
