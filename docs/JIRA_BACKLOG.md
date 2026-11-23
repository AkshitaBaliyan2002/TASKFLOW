# JIRA Backlog (project key TF, Scrum template)

Sprint 1: 23 Nov – 28 Nov 2026. Goal: "Deliver a tested, containerized, deployed TaskFlow API."

| Key | Type | Summary | Assignee | Points |
|---|---|---|---|---|
| TF-1 | Epic | Core task API | – | – |
| TF-2 | Story | As a user I can create a task | Member B | 3 |
| TF-3 | Story | As a user I can list and view tasks | Member B | 2 |
| TF-4 | Story | As a user I can update or complete a task | Member B | 3 |
| TF-5 | Story | As a user I can delete a task | Member B | 1 |
| TF-6 | Story | As a user I can filter tasks by done status | Member B | 2 |
| TF-7 | Epic | Quality and DevOps | – | – |
| TF-8 | Task | Write pytest test cases and test document | Member C | 5 |
| TF-9 | Task | Set up GitHub Actions CI pipeline | Member A | 3 |
| TF-10 | Task | Containerize app with Docker | Member A | 2 |
| TF-11 | Task | Write Kubernetes manifests and roll out | Member A | 3 |
| TF-12 | Task | Compile practical file with screenshots | Member C | 3 |

Suggested git split: Member B owns TF-2..6 (app code), Member C owns TF-8 and TF-12 (tests/docs), Member A owns TF-9..11 (CI, Docker, k8s). Do the work through branches + PRs so all three show commits.

## CSV for bulk import
Save the block below as `jira.csv`, then in JIRA: Project settings -> Import issues -> CSV. Map the columns, and add the Epic Link / Parent manually if the mapping asks. If import is fiddly, just create the issues by hand; it takes about 10 minutes.

```csv
Summary,Issue Type,Description,Story Points
Core task API,Epic,Epic for the task endpoints,
Create a task,Story,As a user I can create a task,3
List and view tasks,Story,As a user I can list and view tasks,2
Update or complete a task,Story,As a user I can update or complete a task,3
Delete a task,Story,As a user I can delete a task,1
Filter tasks by status,Story,As a user I can filter tasks by done status,2
Quality and DevOps,Epic,Epic for testing and deployment,
Write pytest tests and test doc,Task,12 automated test cases plus document,5
Set up GitHub Actions CI,Task,Test then build then deploy,3
Containerize with Docker,Task,Dockerfile and smoke test,2
Kubernetes manifests and rollout,Task,Deployment and Service on minikube,3
Compile practical file,Task,Screenshots and write-up,3
```
