# SKT-Project

SKT FLYAI 프로젝트

Python backend (ML)  
React frontend

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)

## Usage

The complete guide to use this repository: <https://towardsdatascience.com/create-a-complete-machine-learning-web-application-using-react-and-flask-859340bddb33>

## Local development (Python3 Windows)

Create venv

```sh
python -m venv env
```

Access issues

```sh
Set-ExecutionPolicy Unrestricted -Scope Process
```

Run venv

```sh
.\env\Scripts\activate.ps1
```

## Run server (on backend path)

```sh
python -m flask run
```

Server should be running on <http://127.0.0.1:5000/>

## Run UI (on frontend path)

Make sure node js is previously installed. (Version v16.13.0)

```sh
npm install
```

```sh
npm start
```

UI should be running on <http://localhost:3000/>

## Run Streamlit UI (on streamlit path)

```sh
python -m streamlit run gui.py
```

Streamlit UI should be running on <http://localhost:8501/>

## Common mistakes

- Make sure all libraries are installed prior.
- If the model is updated, it should be run before running the server.
- The server should be running before the client is launched.
- Check the version of node js

## Postman API  
![image](https://user-images.githubusercontent.com/104475739/214767265-a973e981-841b-497b-8a4d-a9429f521fa4.png)  

