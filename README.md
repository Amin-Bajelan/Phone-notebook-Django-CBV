<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">

</head>
<body>
  <h1>📱 Contacts Management App with Django and REST API</h1>
  <p>This project allows users to <strong>register</strong>, <strong>log in</strong>, and <strong>manage contact information</strong> such as phone numbers and emails. It also includes <strong>Swagger documentation</strong> for testing and interacting with the API.</p>

  <h2>🚀 Setup Instructions</h2>
  <ol>
    <li>Clone repo: <code>git clone https://github.com/your-username/contacts-app.git</code></li>
    <li>Install dependencies: <code>pip install -r requirements.txt</code></li>
    <li>Run migrations: <code>python manage.py migrate</code></li>
    <li>Start server: <code>python manage.py runserver</code></li>
    <li>Access Swagger UI: <code>/swagger/</code> (in browser)</li>
    <h3>Docker Usage:</h3>
    <li>Build containers: <code>docker-compose build</code></li>
    <li>Start containers: <code>docker-compose up -d</code></li>
    <li>Run migrations in container: <code>docker-compose exec backend python manage.py migrate</code></li>
  </ol>

  <h2>🔧 Features</h2>
  <ul>
    <li>User registration and authentication</li>
    <li>Add, edit, and manage contacts</li>
    <li>Fields: <code>Name</code>, <code>Phone Number</code>, <code>Email</code></li>
    <li>Secure access with session or token authentication</li>
    <li>Real-time API testing with Swagger</li>
  </ul>

  <h2>🐳 Docker Support</h2>
  <ul>
    <li>Includes <code>Dockerfile</code> and <code>docker-compose.yml</code></li>
    <li>Supports PostgreSQL or SQLite backend</li>
    <li>Optimized for local development and cloud deployment</li>
  </ul>

  <h2>📜 API Documentation</h2>
  <ul>
    <li>Swagger UI available at <code>/swagger/</code></li>
    <li>Contact endpoints: <code>/api/contacts/</code></li>
    <li>Methods: <code>GET</code>, <code>POST</code>, <code>PUT</code>, <code>DELETE</code></li>
  </ul>

  <h2>👨‍💻 Developer</h2>
  <p>Create by <strong>Amin</strong></p>
</body>
</html>
