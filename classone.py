import random

class Voiture:
    def __init__(self, marque, modele, annee, carburant="essence", autonomie=100):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.vitesse = 0
        self.carburant = carburant
        self.autonomie = autonomie
        self.mode_autonome = False
        self.kilometrage = 0
        self.passagers = []
        self.destination = None
        self.distance_restante = 0

    def accelerer(self, augmentation):
        self.vitesse += augmentation
        self.kilometrage += augmentation * 0.1
        print(f"La voiture accélère. Vitesse actuelle : {self.vitesse} km/h")

    def freiner(self, diminution):
        self.vitesse = max(0, self.vitesse - diminution)
        print(f"La voiture freine. Vitesse actuelle : {self.vitesse} km/h")

    def activer_mode_autonome(self):
        self.mode_autonome = not self.mode_autonome
        etat = "activé" if self.mode_autonome else "désactivé"
        print(f"Mode autonome {etat}.")

    def definir_destination(self, destination, distance):
        """ Définit une destination et une distance estimée. """
        self.destination = destination
        self.distance_restante = distance
        print(f"Destination définie : {self.destination} ({self.distance_restante} km restants)")

    def se_deplacer(self):
        """ Simule le déplacement en réduisant la distance restante. """
        if self.destination:
            progression = min(self.vitesse * random.uniform(0.2, 0.5), self.distance_restante)
            self.distance_restante -= progression
            print(f"En route vers {self.destination}. Distance restante : {self.distance_restante:.1f} km")
            if self.distance_restante <= 0:
                print(f"Arrivé à {self.destination} ! 🚗✨")
                self.destination = None
        else:
            print("Aucune destination définie.")

    def afficher_info(self):
        print(f"Marque : {self.marque}, Modèle : {self.modele}, Année : {self.annee}, Vitesse : {self.vitesse} km/h")
        print(f"Carburant : {self.carburant}, Autonomie : {self.autonomie}%")
        print(f"Mode autonome : {'Activé' if self.mode_autonome else 'Désactivé'}")
        print(f"Kilométrage : {self.kilometrage} km")
        print(f"Passagers : {', '.join(self.passagers) if self.passagers else 'Aucun'}")
        if self.destination:
            print(f"Destination en cours : {self.destination}, Distance restante : {self.distance_restante:.1f} km")
        else:
            print("Aucune destination en cours.")

# Exemple d'utilisation
voiture_gps = Voiture("Tesla", "Model X", 2024, carburant="électrique", autonomie=90)
voiture_gps.definir_destination("Paris", 400)  # Définir la destination
voiture_gps.accelerer(80)  # Augmenter la vitesse
voiture_gps.se_deplacer()  # Simuler le déplacement
voiture_gps.se_deplacer()  # Simuler le déplacement
voiture_gps.afficher_info()