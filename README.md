# ATO - Version Alpha NumWorks 1

> ⚠️ **Attention !** Ce jeu sera publié dans sa version finale uniquement et est sous licence MIT.

Un jeu d'aventure 2D développé pour la calculatrice NumWorks avec un éditeur de niveaux intégré.

## 📋 Description

ATO est un jeu d'exploration en 2D où vous incarnez un personnage slime qui se déplace dans un monde généré procéduralement. Le projet inclut également un éditeur de niveaux pour créer vos propres cartes personnalisées.

## 🎮 Fonctionnalités

### Jeu Principal (`ato.py`)

- **Monde procédural** : Exploration d'un monde de 500x500 tuiles généré aléatoirement
- **Personnage slime** : Contrôle d'un personnage animé avec des effets de mouvement
- **Environnement varié** : Différents types de tuiles (herbe, arbres, rochers, etc.)
- **Bordure animée** : Bordure du monde avec animation en damier bleu et blanc
- **Système de caméra** : Caméra qui suit le joueur dans le monde
- **Affichage FPS** : Compteur de FPS pour le débogage

### Éditeur de Niveaux (`ato_levelmaker.py`) (indisponible pour le moment)

- **Grille éditable** : Création de niveaux sur une grille de 19x13 tuiles
- **7 types de tuiles** : Herbe, Chemin, Arbre, Rocher, Buisson, Fleur, Maison
- **Export hexadécimal** : Exportation des niveaux en format hexadécimal pour intégration dans le jeu
- **Interface visuelle** : Curseur de sélection et affichage du type de tuile actuel

## 🎯 Types de Tuiles

1. **Herbe (T_GRASS)** : Sol de base avec motif texturé
2. **Chemin (T_PATH)** : Sentier en terre
3. **Arbre (T_TREE)** : Arbre avec tronc et feuillage
4. **Rocher (T_ROCK)** : Obstacle rocheux
5. **Buisson (T_BUSH)** : Végétation basse
6. **Fleur (T_FLOWER)** : Décoration florale
7. **Maison (T_HOUSE)** : Bâtiment avec toit et porte

## 🕹️ Contrôles

### Jeu Principal

- **Flèches directionnelles** : Déplacer le personnage
- **0** : Quitter le jeu

### Éditeur de Niveaux

- **Flèches directionnelles** : Déplacer le curseur
- **OK** : Placer la tuile sélectionnée
- **BACK** : Changer le type de tuile
- **HOME** : Exporter le niveau en hexadécimal et quitter

## 📐 Spécifications Techniques

- **Résolution d'écran** : 320x240 pixels
- **Taille des tuiles** : 16x16 pixels
- **Taille du joueur** : 16x16 pixels
- **Vitesse de déplacement** : 5 pixels par frame
- **Taille du monde** : 500x500 tuiles
- **Taille de la bordure** : 10 tuiles

## 🚀 Installation

1. Transférez les fichiers `ato.py` et `ato_levelmaker.py` sur votre calculatrice NumWorks
2. Exécutez `ato.py` pour jouer ou `ato_levelmaker.py` pour créer des niveaux

## 📝 Notes de Version Alpha

Cette version alpha inclut :
- ✅ Génération procédurale de monde
- ✅ Système de mouvement et animation
- ✅ Éditeur de niveaux basique
- ✅ Export de niveaux en hexadécimal
- ⚠️ Pas de système de collision avec les obstacles
- ⚠️ Pas de système de sauvegarde/chargement de niveaux personnalisés (impossible sous NumWorks n°115 et n°120)
- ⚠️ Cette version n'est qu'un monde vide et un test expérimental, je vous prie de bien patienter les prochaines mises à jour de la version campagne (v1) pour y jouer.

## 🔧 Dépendances

- `kandinsky` : Bibliothèque graphique de NumWorks
- `ion` : Bibliothèque d'entrée de NumWorks
- `time` : Module standard Python

## 📄 Licence
- MIT

Ce projet est en développement actif. Version alpha - NumWorks 1.

