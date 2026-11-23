# Test Case Document – TaskFlow API

Tool: pytest 9 with Flask test client. Run: `pytest -v`
Environment: Python 3.12, Flask 3.1

| ID | Requirement | Test function | Input | Expected result | Status |
|---|---|---|---|---|---|
| TC01 | Health check | test_health | GET /health | 200, `{"status":"ok"}` | Pass |
| TC02 | Create task | test_create_task | POST /tasks `{"title":"Write report"}` | 201, task with id 1, done=false | Pass |
| TC03 | Reject missing title | test_create_task_missing_title | POST /tasks `{}` | 400 | Pass |
| TC04 | Reject blank title | test_create_task_blank_title | POST /tasks `{"title":"   "}` | 400 | Pass |
| TC05 | List tasks | test_list_tasks | Create A, B; GET /tasks | 200, 2 items | Pass |
| TC06 | Get task by id | test_get_task | GET /tasks/1 | 200, title "A" | Pass |
| TC07 | Get missing task | test_get_task_not_found | GET /tasks/99 | 404 | Pass |
| TC08 | Mark task done | test_update_task_done | PUT /tasks/1 `{"done":true}` | 200, done=true | Pass |
| TC09 | Reject empty title on update | test_update_task_empty_title | PUT /tasks/1 `{"title":""}` | 400 | Pass |
| TC10 | Delete task | test_delete_task | DELETE /tasks/1, then GET | 204, then 404 | Pass |
| TC11 | Delete missing task | test_delete_task_not_found | DELETE /tasks/42 | 404 | Pass |
| TC12 | Filter by done flag | test_filter_by_done | GET /tasks?done=true / false | Only matching tasks returned | Pass |

Types covered: positive, negative (invalid input), boundary (blank/whitespace), state-based (create -> update -> delete -> verify).
