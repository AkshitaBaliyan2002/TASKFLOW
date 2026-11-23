# ITDSE14 Practical – Step-by-Step Guide (target: finish by Sat 28 Nov 2026)

Deadline to show: **Mon 30 Nov 2026**. Team of 3. Replace the names below.

Team: **Member A** (Scrum Master / DevOps), **Member B** (Developer), **Member C** (Tester / Docs).

## Day plan
| Day | Do |
|---|---|
| Mon 23 | Create GitHub repo + JIRA project, add all 3 members, create backlog + Sprint 1 |
| Tue 24 | Everyone clones, works on branches, raises PRs (real commits from each member) |
| Wed 25 | CI pipeline green in GitHub Actions |
| Thu 26 | Docker + Kubernetes (minikube) rollout |
| Fri 27 | Test cases run, screenshots taken, close sprint in JIRA |
| Sat 28 | Compile practical file, rehearse demo |

---
## 1. Version control (GitHub)
1. One member creates a repo `taskflow` on GitHub; add the other two as collaborators.
2. Push this project:
   ```bash
   git add . && git commit -m "TF-1 initial project" 
   git branch -M main
   git remote add origin https://github.com/<user>/taskflow.git
   git push -u origin main
   ```
3. **Branch rule:** one branch per JIRA ticket, e.g. `feature/TF-5-filter-tasks`. Commit messages start with the key (`TF-5 add done filter`). Open a Pull Request; another member reviews and merges.
4. Each member must have at least a few commits/PRs (split tickets as in `JIRA_BACKLOG.md`).

**Screenshots:** commit history, a merged PR, branch list.

## 2. JIRA
1. Go to atlassian.com -> sign up for the free plan -> create project, template **Scrum**, key `TF`.
2. Invite the other two members.
3. Create the epics/stories from `docs/JIRA_BACKLOG.md` (can bulk-import the CSV there: Project settings -> Import issues from CSV).
4. Create **Sprint 1**, drag all stories in, set dates (23-28 Nov), **Start sprint**.
5. Move tickets To Do -> In Progress -> Done as you work.
6. Optional but impressive: Project settings -> Apps/Integrations -> **GitHub for Jira**, so commits/PRs with `TF-n` appear on tickets.

**Screenshots:** Backlog, active Sprint board (mid-sprint), Burndown chart (Reports), completed sprint.

## 3. CI/CD (GitHub Actions)
Workflow is already in `.github/workflows/ci.yml`. Push to `main` or open a PR -> Actions tab shows the run.

**Screenshots:** Actions run overview with 3 green jobs, expanded `Test` job showing pytest output + coverage, `Deploy to Kubernetes` job output (`kubectl get pods`).

## 4. Docker
```bash
docker build -t taskflow:local .
docker run -d -p 5000:5000 --name tf taskflow:local
curl localhost:5000/health
curl -X POST localhost:5000/tasks -H "Content-Type: application/json" -d '{"title":"demo"}'
curl localhost:5000/tasks
docker ps
```
**Screenshots:** build output, `docker images`, `docker ps`, curl responses.

## 5. Kubernetes (minikube)
```bash
minikube start
minikube image load taskflow:local
kubectl apply -f k8s/
kubectl get deployments,pods,svc
kubectl rollout status deployment/taskflow
minikube service taskflow --url
```
Show a rolling update too (good for viva):
```bash
# edit something small, rebuild as taskflow:v2
docker build -t taskflow:v2 . && minikube image load taskflow:v2
kubectl set image deployment/taskflow taskflow=taskflow:v2
kubectl rollout status deployment/taskflow
kubectl rollout undo deployment/taskflow      # rollback
```
**Screenshots:** `kubectl get pods` (2 Running), service URL working in browser/curl, rollout + rollback.

## 6. Testing
Tool: **pytest** (+ pytest-cov). 12 automated test cases are in `tests/test_api.py`, documented in `docs/TEST_CASES.md`.
```bash
pytest -v --cov=app --cov-report=term-missing
```
**Screenshots:** terminal with 12 passed + coverage %, plus the CI run.

## 7. Practical file structure (what to submit)
1. Title page, team members, roll numbers
2. Problem statement & project overview (TaskFlow API)
3. Agile approach: roles, user stories, sprint plan (JIRA screenshots)
4. Version control (GitHub screenshots)
5. CI/CD pipeline (workflow explanation + screenshots)
6. Docker (Dockerfile explained line by line + screenshots)
7. Kubernetes (manifests explained + screenshots)
8. Testing (test case table + pytest screenshot)
9. Conclusion, learnings, challenges

## Likely viva questions
- Scrum vs Waterfall? Roles, ceremonies, artifacts?
- What is CI vs CD? What does each job in your pipeline do?
- Image vs container? Why slim base, non-root user, `.dockerignore`?
- Pod vs Deployment vs Service? What do readiness/liveness probes do?
- Why a single gunicorn worker? (in-memory storage)
- Unit vs integration testing; what is code coverage?
