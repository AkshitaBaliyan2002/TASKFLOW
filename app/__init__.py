from flask import Flask, jsonify, request


def create_app():
    app = Flask(__name__)
    tasks = {}
    counter = {"next": 1}

    @app.get("/health")
    def health():
        return jsonify(status="ok")

    @app.get("/tasks")
    def list_tasks():
        done = request.args.get("done")
        items = list(tasks.values())
        if done is not None:
            want = done.lower() == "true"
            items = [t for t in items if t["done"] == want]
        return jsonify(items)

    @app.post("/tasks")
    def create_task():
        data = request.get_json(silent=True) or {}
        title = (data.get("title") or "").strip()
        if not title:
            return jsonify(error="title is required"), 400
        task = {"id": counter["next"], "title": title, "done": False}
        tasks[task["id"]] = task
        counter["next"] += 1
        return jsonify(task), 201

    @app.get("/tasks/<int:task_id>")
    def get_task(task_id):
        task = tasks.get(task_id)
        if not task:
            return jsonify(error="not found"), 404
        return jsonify(task)

    @app.put("/tasks/<int:task_id>")
    def update_task(task_id):
        task = tasks.get(task_id)
        if not task:
            return jsonify(error="not found"), 404
        data = request.get_json(silent=True) or {}
        if "title" in data:
            title = (data["title"] or "").strip()
            if not title:
                return jsonify(error="title cannot be empty"), 400
            task["title"] = title
        if "done" in data:
            task["done"] = bool(data["done"])
        return jsonify(task)

    @app.delete("/tasks/<int:task_id>")
    def delete_task(task_id):
        if task_id not in tasks:
            return jsonify(error="not found"), 404
        del tasks[task_id]
        return "", 204

    return app
