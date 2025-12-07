Create React App (Frontend)

If you want to use Vite (recommended for speed), use Option A.
If you want to use CRA (create-react-app), use Option B.

Option A —Using Vite (Recommended)
npm create vite@latest frontend -- --template react
cd frontend
npm install
To start the frontend:
npm run dev


Option B — Using Create React App
npx create-react-app frontend
cd frontend
npm run dev

Create FastAPI App (Backend)

Go back to main folder:

cd ..
mkdir backend
cd backend

Create a virtual environment:

python -m venv venv
source venv/Scripts/activate # Windows

Install FastAPI & Uvicorn:

pip install fastapi uvicorn

Create a backend file:

nano main.py

Run backend:

uvicorn main:app --reload --port 8000


now you can see result without creating an UI go to IP add
http://127.0.0.1:8000/docs