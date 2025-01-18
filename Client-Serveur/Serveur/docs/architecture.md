# Architecture du Système

Le système est basé sur une architecture microservices où chaque service gère un aspect spécifique du processus d'achat et de paiement. Les composants principaux sont :

- **API RESTful** : Permet aux utilisateurs de se connecter et d'interagir avec le système.
- **gRPC** : Utilisé pour la communication entre les magasins et le serveur central pour la gestion du crédit.
- **HSM** : Utilisé pour la gestion des clés de sécurité, notamment pour le chiffrement des jetons JWT.

## Diagramme d'Architecture
![Architecture Diagram](images/Diagrame_Architechture_Protocole_CGSIM.png)
