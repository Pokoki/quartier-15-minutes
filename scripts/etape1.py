import csv
import math

RAYON_TERRE_M = 6_371_000

def distance_m(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Renvoie la distance en mètres entre deux points GPS (formule de haversine)."""
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)
    a = (
        math.sin(delta_phi / 2) ** 2
        + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2
    )
    distance = 2 * RAYON_TERRE_M * math.asin(math.sqrt(a))
    return distance


def charger_equipements(chemin):
    """Lit le CSV et renvoie une liste de dictionnaires, avec lat et lon en float."""
    pass


def equipements_proches(equipements, lat, lon, rayon_m):
    """Renvoie les équipements à moins de rayon_m mètres, avec une clé 'distance' ajoutée."""
    pass


if __name__ == "__main__":
    # Test de contrôle : doit afficher environ 5540
    print(distance_m(48.8919, 2.2385, 48.8584, 2.2945))

    # Ensuite : charger le CSV, chercher autour de (48.8840, 2.2390) dans un rayon de 500 m,
    # trier par distance et afficher le résultat
