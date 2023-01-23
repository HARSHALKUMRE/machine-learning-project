## Start Machine Learning Project

### Software and Account Requirement

1. [GitHub Account](https://github.com)
2. [Heroku Account](https://dashboard.heroku.com/login)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT CLI](https://git-scm.com/downloads)
5. [Git Documentation](https://git-scm.com/docs/gittutorial)

Create the conda environment
```
conda create -p venv python==3.8 -y
```

To activate the conda environment
```
conda activate venv/
```

Now to create a requirement file

Install the requirements file using this command
```
pip install -r requirements.txt
```

To add files to git repositories
```
git add .
```

OR
```
git add <file_name>
```

> Note: To ignore file on folder from git we can write name of file/folder in .gitignore file

To check the git status
```
git status
```

To check all version maintained by git
```
git log
```

To create version/commit all changes by git
```
git commit -m "message"
```

To send version/changes to github
```
git push origin main
```

To check remote url
```
git remote -v
```
To setup CI/CD pipeline in heroku we need 3 information

1. HEROKU_EMAIL = 
2. HEROKU_API_KEY = 
3. HEROKU_APP_NAME = 

Build docker image
```
docker build -t <image_name>:<tagname> .
```
> Note: Image name for docker must be lowercase

List the docker images
```
docker images
```

Run docker images
```
docker run -p 5001:5001 -e PORT=5001 7e16524f185c
```

To check running container in docker
```
docker ps
```

To stop docker container
```
docker stop <container_id>
```