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
<h1>Le projet</h1> 

<h2>Image du projet</h2>

<p>login.html</p>

![alt text](https://github.com/Caltus124/django_profil_app/blob/master/img/login.png)

<p>politique.html</p>

![alt text](https://github.com/Caltus124/django_profil_app/blob/master/img/politique.png)

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

<p>typed.js</p>

```js
var typed = new Typed('.element', {
  strings: ['BIENVENUE SUR PROFIL',"L'APPLICATION DE GESTION DE PROFIL"],
  typeSpeed: 100,
  backSpeed: 60,
  loop: true
});
```
