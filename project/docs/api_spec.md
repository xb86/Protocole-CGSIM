# API Specification

## Routes

### POST /user/login
- **Description** : Authentifie un utilisateur.
- **Paramètres** :
  - `username` (string) : Nom d'utilisateur.
  - `password` (string) : Mot de passe.
- **Réponse** : 
  - `200 OK` : Connexion réussie, retourne le jeton JWT.
  - `400 Bad Request` : Erreur de validation des paramètres.
  - `401 Unauthorized` : Identifiants incorrects.

### GET /user/{id}
- **Description** : Récupère les informations d'un utilisateur.
- **Paramètres** :
  - `id` (int) : ID de l'utilisateur à récupérer.
- **Réponse** : 
  - `200 OK` : Informations de l'utilisateur.
  - `404 Not Found` : Utilisateur non trouvé.

## Authentification

L'authentification se fait via un jeton JWT dans l'en-tête Authorization.
