from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, Date, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import date

# Création de la base de données SQLite
engine = create_engine('sqlite:///patients.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

# Définition de la classe Contact pour mapper la table "contact"


class Contact(Base):
    __tablename__ = 'patient'
    id = Column(Integer, primary_key=True)
    nom = Column(String)
    prenom = Column(String)
    telphone = Column(String)
    operation = Column(String)
    prix=Column(Float)
    paye=Column(Float)
    date=Column(Date)


# Création de la table "contact" dans la base de données
Base.metadata.create_all(engine)

# Fonctions pour ajouter, modifier et supprimer un contact


def ajouter_operation(nom, prenom,telphone, operation, prix,paye,date):
    try:
        engine = create_engine('sqlite:///patients.db', echo=True)
        Session = sessionmaker(bind=engine)
        session = Session()
        operationN = Contact(nom=nom, prenom=prenom,telphone=telphone, operation=operation,prix=prix,paye=paye,date=date)
        session.add(operationN)
        session.commit()
        print("operation ajouté avec succès.")
        return True
    except:
        return False
    


def modifier_operation(contact_id, nom, prenom,telphone, operation, prix,paye,date):
    engine = create_engine('sqlite:///patients.db', echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    oper = session.query(Contact).get(contact_id)
    if oper:
        oper.nom = nom
        oper.prenom = prenom
        oper.telphone=telphone
        oper.operation = operation
        oper.prix = prix
        oper.paye = paye
        oper.date = date
        session.commit()
        print("Operation modifié avec succès.")
    else:
        print("Operation introuvable.")


def supprimer_operation(contact_id):
    engine = create_engine('sqlite:///patients.db', echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    oper = session.query(Contact).get(contact_id)
    if oper:
        session.delete(oper)
        session.commit()
        print("operation supprimé avec succès.")
    else:
        print("Contact introuvable.")


def lire_certificat(contact_id):
    engine = create_engine('sqlite:///contacts.db', echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    contact = session.query(Contact).get(contact_id)
    element = str(contact.id)+'|'+contact.nom+'|'+contact.prenom+'|'+contact.certificat_num
    return element
    
        
'''
def lire_certificat(contact_id):
    engine = create_engine('sqlite:///contacts.db', echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    contact = session.query(Contact).get(contact_id)
    if contact:
        certificat_num = contact.certificat_num
        with open("certificate.pem", "w") as file:
            file.write(certificat_num)
        element = str(contact.id)+'|'+contact.nom+'|'+contact.prenom
        with open("contact", "w") as file:
            file.write(element)
        return certificat_num
        print(
            f"Certificat numérique du contact avec ID {contact_id}: {certificat_num}")
    else:
        return None
        print("Contact introuvable.")
'''
def lire_operations():
    engine = create_engine('sqlite:///patients.db', echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    operations = session.query(Contact).all()
    if operations:
        result = []
        for oper in operations:
            contact_info = {
                "id": oper.id,
                "nom": oper.nom,
                "prenom": oper.prenom,
                "telphone":oper.telphone,
                "operation": oper.operation,
                "prix": oper.prix,
                "paye": oper.paye,
                "date": str(oper.date)
                

            }
            result.append(contact_info)
        return result
    else:
        return "Aucun contact trouvé."


# Exemple d'utilisation des fonctions

# lire_certificat(1)
# print(lire_contacts())
#ajouter_contact("Doe", "John", "123456789")
#modifier_contact(1, "Doe", "Jane", "987654321")
# supprimer_contact(1)



#ajouter_operation('Doe', 'John', '0123456789','tahyad darssa',  100.0, 70,date.today())
#ajouter_operation('jane', 'brown', '0123456789',' darssa',  200.0, 170,date.today())
#print(lire_operations())