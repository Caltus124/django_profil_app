# django_profil_app

Cette application est créée avec le freamwork <strong>Django</strong> et elle contient une base de données SQLite.
Les collaborateurs du projet sont: William, Arthur, Matteo et Enzo.  

<h1>Commandes</h1> 

<h2>Installer le projet sur votre PC avec:</h2>

```
git clone https://github.com/Caltus124/django_profil_app.git
cd django_profil_app
pip install -r requirements.txt
python3 manage.py runserver 0.0.0.0:8000
```

<h2>Commandes Git HUB pour les développeurs:</h2>

-Faire la mise à jour

```
git pull
```

Voir le status de git
```
git status
```
-Ajouter une modification dans .git
```
git add .
```
-Ajouter une description
```
git commit -m 'la description'
```
-Ajouter a github
```
git push
```
<h2>Image du projet</h2>

<p>login.html</p>

![alt text](https://github.com/Caltus124/django_profil_app/blob/master/img/login.png)

<h2>Code projet</h2>

<p>login.html</p>

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Login</title>
    <meta name="description" content="Login - Register Template">
    <meta name="author" content="Lorenzo Angelino aka MrLolok">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <link rel="stylesheet" href="main.css">
    {% load static %}
    <link rel="stylesheet" type="text/css" href="{% static 'main.css' %}">
</head>
<body>
    <h1 style="text-align: center; margin-top: 80px; margin-bottom: 50px;">BIENVENU SUR PROFIL</h1>
    <div id="container-login">
        <div id="title">
            <i class="material-icons lock">lock</i> Login
        </div>
        {% block content %}
        <form method="post" action="/login/">
            <div class="input">
                {% csrf_token %}
                {{ form.as_p }}
            </div><br>

            <div class="clearfix"></div>

            <input type="submit" value="Log In" />
        </form>
        {% endblock %}

        <div class="privacy">
            <a href="#">Privacy Policy</a>
        </div>

    </div>



</body>
</html>
```
