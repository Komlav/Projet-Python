from User import User
from Classe import Classe
from Chargé import Chargé
from Etudiant import Etudiant
from ResponsableAdmin import ResponsableAdmin

class Admin(User):
    def __init__(self, matricule: str, nom: str, prénom: str, mail: str, téléphone: int, login: str, password: str, typeP: str, etudiants:list = [], chargés:list = [], responsableAdmin:list = []) -> None:
        super().__init__(matricule, nom, prénom, mail, téléphone, login, password, typeP)
        self.etudiants = etudiants
        self.chargés = chargés
        self.responsableAdmins = responsableAdmin
        
    # Setters
    def setEtudiant(self, newEtudiant:Etudiant) -> None:
        self.etudiants.append(newEtudiant)
        
    def setChargé(self, newChargé:Chargé) -> None:
        self.chargés.append(newChargé)
        
    def setResponsableAdmin(self, newResponsableAdmin:ResponsableAdmin) -> None:
        self.responsableAdmins.append(newResponsableAdmin)
        
    # Getters
    def getEtudiant(self) -> list:
        return self.etudiants
        
    def getChargé(self) -> list:
        return self.chargés
        
    def getResponsableAdmin(self) -> list:
        return self.responsableAdmins
        