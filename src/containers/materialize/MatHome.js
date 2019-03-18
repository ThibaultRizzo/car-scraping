import React from 'react';
import axios from 'axios';
import * as constants from '../../constants';
import { Parallax, Row } from 'react-materialize'

const MatHome = (props) => {
    return (
        <>  
            <div className="container">
                <h2 className="col s12 center-align row">Car Scrapping Tool - Aramis Auto - Beta Version</h2>
                <p style={{ textAlign: 'justify' }}>La version béta de cette app a pour but de vous présenter quelques-unes des possibilités que l'on peut vous offrir autour du scrapping de listes de véhicules sur votre site et celui des acteurs majeurs du domaine, en France, en Europe et dans le monde.</p>
                <h5>Philosophie du projet :</h5>
                <p style={{ textAlign: 'justify' }}>Vous offrir une visibilité quotidienne sur une partie du marché de la vente de véhicule en ligne en automatisant votre veille concurrentielle et en proposant, de façon visuelle, une analyse de la donnée qui en est extraite. Cette analyse de la donnée est construite ensemble, pour vous proposer un outil entièrement adapté à vos besoins.</p>
                <h5>Equipe du projet :</h5>
                <p style={{ textAlign: 'justify' }}><a target="_blank" href="http://team-pack.fr/">Pack.</a> est un cabinet de conseil qui accompagne ses clients dans leur stratégie de croissance et d'innovation, autour des trois grands axes qui constitue une entreprise :</p>
                <ol style={{
                    listStyle: 'square'
                }}>
                    <li>Produits et services ;</li>
                    <li>Relation client ;</li>
                    <li>Organisation ;</li>
                </ol>
                <p style={{ textAlign: 'justify' }}>Une telle application s'inscrit dans cette dynamique puisque notre volonté est de vous apporter des chiffres pour votre veille concurrentielle, mais surtout de pouvoir analyser la donnée, pour qu'elle puisse être au service de votre croissance.</p>
                <p style={{ textAlign: 'justify' }}>L'application n'est qu'un vecteur pour vous aider, au quotidien, à penser plus largement votre stratégie de croissance.</p>
                <p style={{ textAlign: 'justify' }}>Ainsi nous ne voulons pas créer une application propriétaire, avec les lourdeurs que cela comprend, mais vous proposer une manière innovante et en rupture d'accéder aux données clées dans votre secteur d'activité.</p>
                <h5>But de l'application :</h5>
                <p style={{ textAlign: 'justify' }}>Proposer sous une même interface de <b>scraper, afficher, trier et rapporter</b> les données issues de cette veille concurrentielle. L'utilisateur pourra lui même lancer le scrapping des sites, y accéder à tout moment et avoir une vision d'ensemble des concurrents.</p>
                <h5>Cette version de l'application :</h5>
                <p style={{ textAlign: 'justify' }}>Nous nous proposons de développer cette application autour de vos besoins. La version présentée ici est une version bétâ, première preuve de notre champ d'action. Une fois cette démonstration effectuée, nous circonscrirons vos besoins et développerons spécifiquement l'outil pour y répondre.</p>
                <p style={{ textAlign: 'justify' }}>Dans sa version actuelle, les parties fonctionnelles de l'application sont :</p>
                <ol style={{
                    listStyle: 'square'
                }}>
                    <li>scraping des sites internet (<i>scraping partiel pour la centrale</i>) :
                    <ol>
                            <li><a target="_blank" rel="noopener noreferrer" href="https://aramisauto.com/achat/">https://aramisauto.com</a></li>
                            <li><a target="_blank" rel="noopener noreferrer" href="https://lacentrale.fr">https://lacentrale.fr</a></li>
                            <li><a target="_blank" rel="noopener noreferrer" href="https://goodbuyauto.it">https://goodbuyauto.it</a></li>
                        </ol>
                    </li>
                    <li>Gestion de la base de données et data-cleaning des champs principaux ;</li>
                    <li>Présentation des données formatées dans un tableau récapituatif (<a target="_blank" href='/table/'>cliquer ici</a>);</li>
                    <li>2 types de graphique pour permettant l'analyse de la donnée (<a target="_blank" href='/chart/'>cliquer ici</a>);</li>
                    <li>Téléchargement de la donnée (<a target="_blank" href='/table/'>cliquer ici</a>).</li>
                </ol>
                <p style={{ textAlign: 'justify' }}><b>NB :</b> Les lenteurs de chargements sont liés au stade de développement bétâ de l'application.</p>
                <h5> Les développements à venir :</h5>
                <p>Dans une V2 et une fois la validation des besoins effectuée, nous améliorerons la présente application pour y ajouter les fonctionnalités suivantes. Ces fonctionnalités constituerons les fonctionnalités de base de l'application :</p>
                <ol style={{
                    listStyle: 'square'
                }}>
                <b>
                    <li>Réactivité avec un retour dans les 2 jours ouvrés ;</li>
                    <li>Engagement sur un taux de fiabilité supérieur à 95% au total et 90% par vendeur* ;</li>
                    <li>Scraping automatique et quotidien de l'ensemble des sites ;</li>
                    <li>Accès via login à la donnée scrapée ;</li>
                    <li>Visibilité des différentes informations de scrapping (fraicheur de la donnée, taux de fiabilité, nombres de voitures scrapées ...) ;</li>
                    <li>Page tableau comprenant les champs principaux préalablement choisi ;</li>
                    <li>Bouton pour lancer le scraping manuellement ;</li>
                    <li>Possibilité de filtrer et trier les données principales directement dans l'application ;</li>
                    <li>Quelques données d'historique (tendance sur le nombre de voiture scrapée et le prix moyen par rapport au scrapping précédent) ;</li>
                    <li>Bouton pour lancer le scraping manuellement ;</li>
                    <li>Gestion d'une DB de 20 000 lignes.</li>
                </b> 
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
                <h5> Contact :</h5>
                <p style={{ textAlign: 'center' }}><b>Mathieu SCHMITT</b></p>
                <p style={{ textAlign: 'center' }}> Mail : <a href="mailto:mathieu.schmitt@team-pack.fr">mathieu.schmitt@team-pack.fr</a><br/>Tel: 0669910053
                </p>
            </div>
        </>
    );
}

export default MatHome;