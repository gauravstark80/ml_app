# ml_app

#Deployment Link:

[https://mlapp-70wj.onrender.com/](https://mlapp-70wj.onrender.com/)

#Learnings:

Make sure to configure the deployment properly with appropriate commands. While it may not be issue with dependencies, it may be issue with the commands on platform for Ex: I was using command "gunicorn run:app" instead of "gunicorn app:app" and it was throwing error in the cloud terminal as "No module found : run" untill I corrected it.
