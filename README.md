# Tuto Vue.js et axios

## requirement
- Vue.js cdn : <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
- Axios cdn : <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
- Bootstrap
- documentation Vue.js: https://fr.vuejs.org/v2/guide/
- Utilisation axios dans Vue: https://fr.vuejs.org/v2/cookbook/using-axios-to-consume-apis.html
- Mon code : https://github.com/MJoshua25/first_projet.git

## Créer notre première Vue
  Pour ce créer notre première vue nous allons prendre pour base le template par défaut de bootstrap:
```html
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

    <title>Hello, world!</title>
  </head>
  <body>
    <h1>Hello, world!</h1>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
  </body>
</html>
```
  puis nous allons une div avec pour id: "app"
```html
<div id="app">
  {{ message }}
</div>
```
''{{  }}'' est le délimiteur par défaut de Vue.js
  Ensuite nous allons créer une vue après le script de Vue.js:
<<<<<<< Updated upstream
```javascript
=======

```javasrcipt
>>>>>>> Stashed changes
var app = new Vue({
  el: '#app', // Premet de précisé l'id de l'élément lié à la vue
  data: { // déclaration des différentes variables
    message: 'Hello Vue !'
  }
})
```
résultats: Vue1.html

Le code ci dessus permet d'afficher la variable message dans une vue


## affectation de propriété
  Afin de ne pas confondre le delimiteur de Vue.js avec celui de Jinja nous allons modifier celui de Vue.js en le faisan passer à: "${ }"
  syntaxe:
  ```javascript
  delimiters: ["${","}"],
  ```
  Pour affecter un variable à une propriété, l'on utilise "v-bind:nom_de_la_propriété='nom_de_la_variable'"
  Exemple
  Juste après notre variable message, nous allons ajouter la variable messages puis nous allons ajouter le code suivant dans notre div(app):
  ```html
<span v-bind:title="messages">
  Hover your mouse over me for a few seconds
  to see my dynamically bound title!
</span>
  ```
  resultats vue2.html
  
## suite
  pour la suite veuillez vous référer à la documentation et à mon code
