import React from 'react';
import axios from 'axios';
import * as constants from '../../constants';
// import { Row, Button, Table, Pagination } from 'react-materialize'

const MatHome = (props) => {
    return (
        <>
        <h2 className="center-align row">Car Scrapping Tool - Beta Version</h2>
        <h6 className="center-align row">Outil de scrapping a destination d'Aramis Auto - Version Béta uniquement</h6>
        <br/><br/>
        <div className="container">
            <p style={{textAlign:'justify'}}>La version béta de cette app a pour but de vous présenter quelques-unes des possibilités que l'on peut vous offrir autour du scrapping de listes de véhicules sur votre site et celui des acteurs majeurs du domaine, en France, en Europe et dans le monde.</p>
            <h5>Philosophie du projet :</h5>
            <p style={{textAlign:'justify'}}>Vous offrir une visibilité quotidienne sur une partie du marché de la vente de véhicule en ligne en automatisant votre veille concurrentielle et en proposant, de façon visuelle, une analyse de la donnée qui en est extraite.</p>
            <h5>But de l'application :</h5>
            <p style={{textAlign:'justify'}}>Proposer sous une même interface de <b>scraper, afficher, trier et rapporter</b> les données issues de cette veille concurrentielle. L'utilisateur pourra lui même lancer le scrapping des sites, y accéder à tout moment et avoir une vision d'ensemble des concurrents.</p>
            <h5>Cette version de l'application :</h5>
            <p style={{textAlign:'justify'}}>Nous nous proposons de développer cette application autour de vos besoins. La version présentée ici est une version bétâ, première preuve de notre champ d'action. Une fois cette démonstration effectuée, nous circonscrirons vos besoins et développerons spécifiquement l'outil pour y répondre.</p>
            <p style={{textAlign:'justify'}}>Dans sa version actuelle, les parties fonctionnelles de l'application sont :</p>
            <ol style={{
                listStyle: 'square'
            }}>
                <li>scraping des sites internet (<i>scraping partiel pour la centrale</i>) : 
                    <ol>
                        <li><a target="_blank" href="https://aramisauto.com/achat/">https://aramisauto.com</a></li>
                        <li><a target="_blank" href="https://lacentrale.fr">https://lacentrale.fr</a></li>
                        <li><a target="_blank" href="https://goodbuyauto.it">https://goodbuyauto.it</a></li>
                    </ol>
                </li>
                <li>Gestion de la base de données et data-cleaning des champs principaux ;</li>
                <li>Présentation des données formatées dans un tableau récapituatif (<a target="_blank" href='/table/'>cliquer ici</a>);</li>
                <li>2 types de graphique pour permettant l'analyse de la donnée (<a target="_blank" href='/chart/'>cliquer ici</a>);</li>
                <li>Téléchargement de la donnée (<a target="_blank" href='/table/'>cliquer ici</a>).</li>
            </ol>
            <h5> Les développements à venir :</h5>
            <p>Dans une V2 et une fois la validation des besoins effectuée, nous améliorerons la présente application pour y ajouter les fonctionnalités suivantes. Ces fonctionnalités constituerons les fonctionnalités de base de l'application :</p>
            <ol style={{
                listStyle: 'square'
            }}>
                <li><b>Réactivité avec un retour dans les 2 jours ouvrés ;</b></li>
                <li><b>Engagement sur un taux de fiabilité supérieur à 95% au total et 90% par vendeur* ;</b></li>
                <li>Scraping automatique et quotidien de l'ensemble des sites ;</li>
                <li>Accès via login à la donnée scrapée ;</li>
                <li>Visibilité des différentes informations de scrapping (fraicheur de la donnée, taux de fiabilité, nombres de voitures scrapées ...) ;</li>
                <li>Page tableau comprenant les champs principaux préalablement choisi ;</li>
                <li>Bouton pour lancer le scraping manuellement ;</li>
                <li>Possibilité de filtrer et trier les données principales directement dans l'application ;</li>
                <li>Quelques données d'historique (tendance sur le nombre de voiture scrapée et le prix moyen par rapport au scrapping précédent) ;</li>
                <li>Bouton pour lancer le scraping manuellement ;</li>
                <li>Gestion d'une DB de 20 000 lignes.</li>
            </ol>
            <i>*la fiabilité correspond au taux de voitures scrapées entièrement et intégrant la base de donnée sur le nombre de voitures totales du site (voiture rejetée).</i>
            <h5> Les options possibles :</h5>
            <p>L'application sera développée en accord avec les besoins ciblés. Cependant nous avons déjà pensé à quelques options de développement tant sur la partie scraping que sur la partie visualisation de données :</p>
            <ol>
                <li>Augmenter le nombre de sites scrapés (France, Europe) ;</li>
                <li>Augmenter le nombre de sites scrapés (Zone Monde) ;</li>
                <li>Possibilité d'intégrer des rapports automatisés aux décideurs ;</li>
                <li>Proposer d'autres types de graphiques et d'outils visuels pour améliorer la compréhension de la donnée ;</li>
                <li><b>Stocker sur un temps donné les données issues du scrapping pour intégrer des facteurs historiques et comparatifs ;</b></li>
                <li>Augmenter le nombre de données recueillies (ex banque d'images) ;</li>
                <li>Proposer des outils d'analyse automatique (voiture la plus vendu, prix moyens ...).</li>
            </ol>
        </div>
        </>
    );
}

export default MatHome;