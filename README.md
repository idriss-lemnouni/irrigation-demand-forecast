# Prévision de l’ET0 à un jour

Télécharger le [CSV source](https://raw.githubusercontent.com/idriss-lemnouni/crop-water-demand/main/reports/daily-water-demand.csv) puis exécuter `python forecast.py daily-water-demand.csv`. La régression utilise les trois premiers quarts des paires chronologiques par site. Le dernier quart sert à comparer la MAE avec la persistance.

L’entrée reprend le [rapport journalier FAO-56](https://github.com/idriss-lemnouni/crop-water-demand/blob/main/reports/daily-water-demand.csv), calculé à partir de [NASA POWER](https://power.larc.nasa.gov/). L’ET0 est une estimation. Une seule année est disponible.
