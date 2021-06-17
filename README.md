WOAH WOAH THIS IS ALL WRONG!

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


#### 4. Visit the Sphinx Documentationaw. 

visit: https://asolism.gitlab.io/mlapi/


#### 5. Generate Local API and Markdown Documentation

```bash
cd doc
make html
```

`open doc/__build/html/index.html`

### Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md)

### License

Unless otherwise specified, the source code of this project is covered under Crown Copyright, Government of Canada, and is distributed under the [MIT License](LICENSE).

The Canada wordmark and related graphics associated with this distribution are protected under trademark law and copyright law. No permission is granted to use them outside the parameters of the Government of Canada's corporate identity program. For more information, see [https://www.canada.ca/en/treasury-board-secretariat/topics/government-communications/federal-identity-requirements.html](Federal identity requirements).

______________________

#TODO: translate instructions to French

### Comment contribuer

Voir [CONTRIBUTING.md](CONTRIBUTING.md)

### License

Sauf indication contraire, le code source de ce projet est protégé par le droit de la Couronne du gouvernement du Canada et distribué sous la [LICENSE](license MIT).

Le mot-symbole « Canada » et les éléments graphiques connexes liés à cette distribution sont protégés en vertu des lois portant sur les marques de commerce et le droit d'auteur. Aucune autorisation n'est accordée pour leur utilisation à l'extérieur des parametres du programme de coordination de l'image de marque du gouvernement du Canada. Pour obtenir davantage de renseignement à ce sujet, veuillez consulter le [https://www.canada.ca/fr/secretariat-conseil-tresor/sujets/communications-gouvernementales/exigences-image-marque.html](Exigences pour l'image de marque).
