# 100daysofpythonpraticesangelayu
code et project python pour la formation 100 jour de code en python de Angela Yu sur udemy
in this first class of poo mais cette partie est un exercie personnel sur la poo en python,
 ### Voici un exercice de TD en Python qui te permettra

- de créer une classe Voiture en utilisant la Programmation Orientée Objet (POO).

# Consigne :
### Tu dois concevoir une classe Voiture avec les attributs suivants :
- marque (str) : la marque de la voiture
- modele (str) : le modèle de la voiture
- annee (int) : l'année de fabrication
- vitesse (int) : la vitesse actuelle


Et les méthodes suivantes :
- accelerer(augmentation: int): augmente la vitesse de la voiture
- freiner(diminution: int): diminue la vitesse de la voiture
- afficher_info(): affiche les détails de la voiture

Solution possible :


```python
class Voiture:
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.vitesse = 0  # Initialisation de la vitesse à 0

    def accelerer(self, augmentation):
        self.vitesse += augmentation
        print(f"La voiture accélère. Nouvelle vitesse : {self.vitesse} km/h")

    def freiner(self, diminution):
        self.vitesse -= diminution
        if self.vitesse < 0:
            self.vitesse = 0
        print(f"La voiture freine. Nouvelle vitesse : {self.vitesse} km/h")

    def afficher_info(self):
        print(f"Marque : {self.marque}, Modèle : {self.modele}, Année : {self.annee}, Vitesse actuelle : {self.vitesse} km/h")

# Exemple d'utilisation
ma_voiture = Voiture("Tesla", "Model S", 2022)
ma_voiture.afficher_info()
ma_voiture.accelerer(30)
ma_voiture.freiner(10)
ma_voiture.afficher_info()
```
# Rendons nos class plus performant
- on va rendre cette classe Voiture encore plus sophistiquée!🚗
# Ajouts possibles :
- Gestion du type de carburant et du niveau de charge (pour une voiture électrique).
- Mode conduite automatique (pour simuler un véhicule autonome).
- Indicateur d'entretien (pour suivre l'usure et prévoir la maintenance).

# nos code 
```python
class Voiture:
    def __init__(self, marque, modele, annee, carburant="essence", autonomie=100):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.vitesse = 0
        self.carburant = carburant  # Essence, Diesel, Électrique
        self.autonomie = autonomie  # Niveau de charge pour les électriques
        self.mode_autonome = False  # Mode conduite automatique désactivé par défaut
        self.kilometrage = 0  # Pour suivre l'entretien
        self.passagers = []  # Liste des occupants

    def accelerer(self, augmentation):
        self.vitesse += augmentation
        self.kilometrage += augmentation * 0.1  # Augmenter le kilométrage
        print(f"La voiture accélère. Vitesse actuelle : {self.vitesse} km/h")

    def freiner(self, diminution):
        self.vitesse = max(0, self.vitesse - diminution)
        print(f"La voiture freine. Vitesse actuelle : {self.vitesse} km/h")

    def activer_mode_autonome(self):
        self.mode_autonome = not self.mode_autonome
        etat = "activé" if self.mode_autonome else "désactivé"
        print(f"Mode autonome {etat}.")

    def ajouter_passager(self, nom):
        self.passagers.append(nom)
        print(f"{nom} a pris place dans la voiture.")

    def afficher_info(self):
        print(f"Marque : {self.marque}, Modèle : {self.modele}, Année : {self.annee}, Vitesse : {self.vitesse} km/h")
        print(f"Carburant : {self.carburant}, Autonomie : {self.autonomie}%")
        print(f"Mode autonome : {'Activé' if self.mode_autonome else 'Désactivé'}")
        print(f"Kilométrage : {self.kilometrage} km")
        print(f"Passagers : {', '.join(self.passagers) if self.passagers else 'Aucun'}")

# Exemple d'utilisation
voiture_avancee = Voiture("Tesla", "Model X", 2024, carburant="électrique", autonomie=90)
voiture_avancee.afficher_info()
voiture_avancee.accelerer(50)
voiture_avancee.ajouter_passager("Tarik")
voiture_avancee.activer_mode_autonome()
voiture_avancee.afficher_info() 
```

### On peu encore ameliore 
