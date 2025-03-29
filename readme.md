README - Système de Gestion Hospitalière

Description du Projet

Ce projet est une application de gestion hospitalière permettant d'optimiser la gestion des patients, du personnel médical et des ressources hospitalières. Le système repose sur une architecture N-tiers pour assurer une séparation claire des responsabilités et garantir la scalabilité et la sécurité des données sensibles.

Architecture Implémentée

L'architecture N-tiers adoptée se compose des trois couches suivantes :

Couche Présentation :

Interface utilisateur développée avec Django et Django REST Framework.

Accès sécurisé via authentification par rôles.

Interface adaptée aux différents utilisateurs (médecin, infirmier, administrateur).

Couche Métier :

Contient la logique métier et les règles hospitalières (gestion des rendez-vous, prescriptions, disponibilités).

Utilisation des DTOs pour structurer les données en entrée/sortie.

Gestion des exceptions spécifiques au domaine médical.

Couche Données :

Base de données PostgreSQL pour le stockage des dossiers patients, médicaux et hospitaliers.

Mise en place des relations et contraintes d'intégrité.

Gestion des données historiques et sensibles.

Diagrammes UML

Diagramme de Classes

Le diagramme de classes représente les entités principales du système et leurs relations :

Patient : Contient les informations personnelles et l'historique médical.

Médecin : Spécialiste avec un planning de rendez-vous.

Consultation : Association entre un patient et un médecin, avec diagnostic et prescriptions.

Chambre : Indique les lits disponibles et les patients hospitalisés.

Diagramme de Séquence

Ce diagramme illustre les interactions entre les couches pour un scénario typique, par exemple la prise de rendez-vous :

Un patient demande un rendez-vous via l’interface utilisateur.

La requête est transmise à la couche métier pour validation des disponibilités.

Si une disponibilité est trouvée, le rendez-vous est enregistré en base de données.

Une confirmation est envoyée au patient.

Patterns de Conception Utilisés

Repository Pattern : Encapsule l'accès aux données et sépare la logique de la couche métier.

DTO (Data Transfer Object) : Utilisé pour structurer les données envoyées aux API REST.

Singleton : Pour gérer certaines configurations critiques comme la connexion à la base de données.

Exception Handling Pattern : Implémenté pour gérer les erreurs métier et assurer une gestion robuste des exceptions.

Instructions d'installation et d'utilisation

Prérequis

Python 3.8+

PostgreSQL

Django et Django REST Framework

Installation

Cloner le dépôt :

git clone https://github.com/utilisateur/gestion-hospitaliere.git
cd gestion-hospitaliere

Installer les dépendances :

pip install -r requirements.txt

Configurer la base de données PostgreSQL dans settings.py.

Appliquer les migrations :

python manage.py migrate

Démarrer le serveur :

python manage.py runserver

API REST

L'API REST permet aux applications mobiles du personnel médical d'accéder aux données hospitalières en toute sécurité.

Endpoints principaux :

/api/patients/ : Gérer les patients

/api/consultations/ : Suivi des consultations

/api/personnel/ : Planifier et gérer les rendez-vous

/api/planning/ : Gestion des chambres et disponibilités

Tests et Documentation

Tests unitaires et d'intégration : Exécutables via pytest.

Documentation API : Générée avec drf-yasg et accessible via /swagger/.

Patterns de Conception Utilisés

Repository Pattern : Encapsule l'accès aux données et sépare la logique de la couche métier.

DTO (Data Transfer Object) : Utilisé pour structurer les données envoyées aux API REST.

Singleton : Pour gérer certaines configurations critiques comme la connexion à la base de données.

Exception Handling Pattern : Implémenté pour gérer les erreurs métier et assurer une gestion robuste des exceptions.

Technologies Utilisées

Backend : Django & Django REST Framework

Base de données : PostgreSQL

Authentification : JWT avec gestion des rôles

Frontend : (Possibilité d'intégration future avec une application mobile)

Tests : Pytest

Architecture N-tiers

L'application est divisée en trois couches principales :

Couche Présentation : Interface utilisateur et API REST

Couche Métier : Gestion des règles métier et logique applicative

Couche Données : Modélisation des entités et accès à la base de données

Installation et Exécution

Prérequis

Python 3.x

PostgreSQL

Pip & Virtualenv

Instructions

Cloner le dépôt

git clone https://github.com/nom_utilisateur/gestion_hopital.git
cd gestion_hopital

Installer les dépendances

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

Configurer la base de données
Modifier le fichier settings avec vos paramètres PostgreSQL.

DATABASE_URL=postgres://user:password@localhost:5432/hopital_db

Appliquer les migrations

python manage.py migrate

Lancer le serveur

python manage.py runserver

Tests unitaires

pytest

Fonctionnalités Principales

Gestion des patients et dossiers médicaux

Gestion du personnel médical (médecins, infirmiers)

Planification des rendez-vous

Suivi des traitements et prescriptions

Gestion des chambres et lits d'hospitalisation

Tableau de bord analytique

API REST sécurisée