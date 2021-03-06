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
  
  
  
# Applications
Nous aurons 6 applications qui sont: entreprise, configuration,statistique,contact et restaurant.

## entreprise

#### Niveau
  * Presentation
  * Personnel
    * Social_ent
    * Poste
    
#### Models

```python
  class Presentation(Timemodels):
        """Model definition for Presentation."""
        
        nom = models.CharField(max_length=255)
        description = models.TextField()
        logo = models.ImageField(upload_to='logo', )
        working_hour = models.ManyToManyField('WorkingHour',related_name='working_config')
        license_site = models.CharField(max_length=255)

        class Meta:
            """Meta definition for Presentation."""

            verbose_name = 'Presentation'
            verbose_name_plural = 'Presentations'

        def __str__(self):
            """Unicode representation of Presentation."""
            return self.nom

  class Poste(Timemodels):
        nom = models.CharField(max_length=160)
        
        def __str__(self):
            return self.nom

        class Meta:
            verbose_name = 'Poste'
            verbose_name_plural = 'Postes'


    class Personnel(Timemodels):
        nom = models.CharField(max_length=160)
        prenom = models.CharField(max_length=160)
        photo = models.ImageField(upload_to='photo_presonnel')
        poste = models.ForeignKey(Poste, on_delete=models.CASCADE,related_name="poste_presonnel")
        social = models.ManyToManyField('Social',related_name='social_chef')
        
        def __str__(self):
            return self.nom+ " " + self.prenom

        class Meta:
            verbose_name = 'Cuisinier'
            verbose_name_plural = 'Cuisiniers'
            
    class Social_ent(Timemodels):
        # TODO: Define fields here
        icon = models.ManyToManyField('Social',related_name='social_icon')
        personnel = models.ForeignKey('Personnel', on_delete=models.CASCADE,related_name="presonnel_social")
        lien = models.URLField(max_length=200)
        
        def __str__(self):
            return '{}'.format(self.name)
    
```

## Configuration

#### Niveau
  Pas d'api
  la configuration se fait avec jinja
  
#### myfields.py
```python
    from django.utils.translation import ugettext as _
    from django.db.models import SmallIntegerField
    from django.db import models

    DAY_OF_THE_WEEK = {
        '1' : _(u'Monday'),
        '2' : _(u'Tuesday'),
        '3' : _(u'Wednesday'),
        '4' : _(u'Thursday'),
        '5' : _(u'Friday'),
        '6' : _(u'Saturday'),
        '7' : _(u'Sunday'),
    }

    class DayOfTheWeekField(models.CharField):
        def __init__(self, *args, **kwargs):
            kwargs['choices']=tuple(sorted(DAY_OF_THE_WEEK.items()))
            kwargs['max_length']=1
            super(DayOfTheWeekField,self).__init__(*args, **kwargs)
```
    
#### Models

```python
  class Timemodels(models.Model):
      statut = models.BooleanField(default=False)
      date_add =  models.DateTimeField(auto_now_add=True)
      date_update =  models.DateTimeField(auto_now=True)
      
      class Meta:
           abstract = True
           
   class WorkingHour(Timemodels):
      # TODO: Define fields here
      jour = myfields.DayOfTheWeekField(unique="True")
      start_hour = models.TimeField()
      end_hour = models.TimeField()
      class Meta:
          verbose_name = "WorkingHour"
          verbose_name_plural = "WorkingHours"

      def __str__(self):
          return '{}  {} - {}'.format(self.jour,self.start_hour,self.end_hour)
           
   class About(Timemodels):
        """Model definition for About."""

        nom = models.CharField(max_length=255)
        description = models.TextField()
        image = models.ImageField(upload_to='image_about', )

        class Meta:
            """Meta definition for About."""

            verbose_name = 'About'
            verbose_name_plural = 'Abouts'

        def __str__(self):
            """Unicode representation of About."""
            pass
            
    class Social(Timemodels):
        # TODO: Define fields here
        choice=[('FB','facebook'),('TW','twitter'),('INS','instagram'),('GOO','google')]
        name = models.CharField(max_length=100,choices=choice)

        @property
        def font(self):
            if self.name == 'FB':
                font = 'fab fa-facebook-f'
            elif self.name == 'TW':
                font ='fab fa-twitter'
            elif self.name == 'INS':
                font ='fab fa-instagram'
            elif self.name == 'GOO':
                font ='fab fa-google-plus-g'
            return font
        class Meta:
            verbose_name = "Social"
            verbose_name_plural = "Socials"

        def __str__(self):
            return '{}'.format(self.name)
            
           
    class ReserveConfiguration(Timemodels):
        """Model definition for ReserveConfiguration."""

        titre_formulaire = models.CharField(max_length=255)
        sous_titre_formulaire = models.CharField(max_length=255)
        image = models.ImageField(upload_to='resrvation_back')


        # TODO: Define fields here

        class Meta:
            """Meta definition for ReserveConfiguration."""

            verbose_name = 'ReserveConfiguration'
            verbose_name_plural = 'ReserveConfigurations'
            
    class About(Timemodels):
        """Model definition for About."""

        nom = models.CharField(max_length=255)
        description = models.TextField()
        image = models.ImageField(upload_to='image_about', )

        class Meta:
            """Meta definition for About."""

            verbose_name = 'About'
            verbose_name_plural = 'Abouts'

        def __str__(self):
            """Unicode representation of About."""
            return self.nom
```

## Contact

#### Niveau
  * Message
  * Newsletter
    
#### Models

```python
    class Message(Timemodels):
        """Model definition for Message."""
        nom = models.CharField(max_length=250)
        sujet = models.CharField(max_length=250)
        email = models.EmailField()
        message = models.TextField()


        # TODO: Define fields here

        class Meta:
            """Meta definition for Message."""

            verbose_name = 'Message'
            verbose_name_plural = 'Messages'
            
    class Newsletter(Timemodels):
        email = models.EmailField()
        def __str__(self):
            return self.email

        class Meta:
            verbose_name = 'Newsletter'
            verbose_name_plural = 'Newsletters'
```


## Menu

#### Niveau
  * Menu
    * category
      * plat
        * ingredients
    
#### Models

```python
    class Menu(Timemodels):
        nom =  models.CharField(max_length=255)
        jour = myfields.DayOfTheWeekField(unique="True")
        plats = models.ManyToManyField('Plat',related_name='menu_plat')
        
        def __str__(self):
        return self.nom
        
        class Meta:
            verbose_name = 'Category'
            verbose_name_plural = 'Categorys'

    class Category(Timemodels):
        nom =  models.CharField(max_length=255)
        
        def __str__(self):
        return self.nom
        
        class Meta:
            verbose_name = 'Category'
            verbose_name_plural = 'Categorys'


    class Ingredient(Timemodels):
        nom =  models.CharField(max_length=255)
        
        def __str__(self):
            return self.nom
        
        class Meta:
            verbose_name = 'Ingredient'
            verbose_name_plural = 'Ingredient'
            
            
    class Plat(Timemodels):
        categorie = models.ForeignKey(Category, on_delete=models.CASCADE,related_name="menu_plat")
        nom = models.CharField(max_length=160)
        description = models.TextField(null=True)
        prix = models.FloatField()
        ingredient = models.ManyToManyField(Ingredient,related_name="ingrediant_plat")
        image = models.ImageField(upload_to='restaurant/plat')
        speciale = models.BooleanField(default=False)
        def __str__(self):
            return self.nom

        class Meta:

            verbose_name = 'Plat'
            verbose_name_plural = 'Plats'
```

## clientele

#### Niveau
  * Reservation
  * Temoignage
    
#### Models

```python
    class Reservation(Timemodels):
        nom = models.CharField(max_length=160)
        email = models.EmailField()
        numero = models.CharField(max_length=160)
        date = models.DateField()
        heure = models.TimeField()
        personne = models.IntegerField()
        
        def __str__(self):
        return self.nom

        class Meta:
            verbose_name = 'Reservation'
            verbose_name_plural = 'Reservations'
            

    class Temoignage(Timemodels):
        nom = models.CharField(max_length=160)
        commentaire = models.TextField()
        job = models.CharField(max_length=255)
        
        def __str__(self):
            return self.nom

        class Meta:
            verbose_name = 'Temoignage'
            verbose_name_plural = 'Temoignages'
```

## Statistiques
```python
    class InfoUser(Timemodels):
    """Model definition for InfoUser."""

    ip = models.GenericIPAddressField()
    pays = models.CharField(max_length=50)
    ville = models.CharField(max_length=50)
    continent = models.CharField(max_length=50)
    longitude = models.FloatField()
    latitude = models.FloatField()
    reseau = models.CharField(max_length=50)

    def __str__(self):
        return self.ip 
```

# Page manquante
  * contact.html
  
