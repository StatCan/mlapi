## Machine Learning API (mlapi)

Template repo of machine learning model deployment with FastAPI, Docker, and Sphinx. 

This is a minimalistic build, and should be use only as a refence for deploying your 
machine learning project as a service.

### Quick Usage Guide 


#### 1. Build docker image 

```bash
cd src/mlapi
docker build -t mlapi . 
```

#### 2. Run the RestAPI (FastAPI) Container

```
docker run -d -p 8888:8888 --name ml-mlapi mlapi
```

#### 3. Try the RestAPI 

visit: http://localhost/8888/docs 


#### 4. Visit the Sphinx Documentation

visit:


#### 5. Generate Local API and Markdown Documentation

```bash
cd doc
make html
```

`open doc/__build/html/index.html`