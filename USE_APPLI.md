# Utilisation de l'application KMAmossys

Dans cette partie nous expliquons à l'auditeur comment se servir de l'application (sans se soucier du code).

1. Recherche d'une **Vulnerabilite**

	Ouvrir l'URL racine du site. Vous avez 3 champs de recherches optionnels à votre disposition. Les vulnérabilités trouvées s'affichent sous les champs de recheche. Cliquez sur une vulnérabilité pour afficher son détail.

	 * Les mots clefs : vous pouvez en sélectionner plusieurs. Pour affiner votre recherche sélectionnez-en plus.
	 * Recherche dans la description de la vulnérabilité : filtre les résultats en recherchant un mot dans la description de la vulnérabilité.
	 * Recherche selon les activités d'audit. Après avoir sélectionner **Test d'intrusion** vous pourrez choisir entre *Test d'intrusion interne* et *Test d'intrusion externe* **SI** votre vulnérabilité est spécifique à l'un ou l'autre.

	Une fois que vous avez sélectionné une vulnérabilité vous avez accés à sa définition, description, recommandations associées etc...
	Pour plus d'information sur la signification des champs, veuillez vous reporter aux cahier des charges (fichier pdf non versionné). 

2. Recherche d'une **Recommandation**

	Ouvrir l'URL /vuln/recos/. Vous avez 2 champs de recherches optionnels à votre disposition. Les recommandations trouvées s'affichent sous les champs de recheche. Cliquez sur une recommandation pour afficher son détail.

	 * Les thèmes : vous pouvez en sélectionner plusieurs. Pour affiner votre recherche sélectionnez-en plus.
	 * Recherche dans l'explication de la recommandation : filtre les résultats en recherchant un mot dans la explication de la recommandation.

	 Une fois que vous avez sélectionné une recommandation vous avez accés à son explication, sa vulnérabilité associée etc...
	 Pour plus d'information sur la signification des champs, veuillez vous reporter aux cahier des charges (fichier pdf non versionné). 

3. Ajout d'une **Vulnerabilite**

	Ouvrir l'URL racine du site. Sous le formulaire il y a un lien vers */admin/vuln/vulnerabilite/add/*. Cliquer dessus. Sur cette page (contexte administrateur) vous pouvez ajouter des vulnérabilités. Notez que vous pouvez ajouter dynamiquement des mots clefs, rapports, activité d'audit... avec le **+** à droite du champ. De même vous pouvez ajouter des Recommandations en bas de la page qui seront liées à cette Vulnerabilite.

	Pour plus d'information sur la signification des champs, veuillez vous reporter aux cahier des charges (fichier pdf non versionné). 
	
4. Ajout d'une **Recommandation**
	
	Ouvrir l'URL /vuln/recos/. Sous le formulaire il y a un lien vers */admin/vuln/recommandation/add/*. Cliquer dessus. Sur cette page (contexte administrateur) vous pouvez ajouter des Recommandation. Notez que vous pouvez ajouter dynamiquement des mots clefs (thèmes), rapports... avec le **+** à droite du champ.

	Pour plus d'information sur la signification des champs, veuillez vous reporter aux cahier des charges (fichier pdf non versionné). 