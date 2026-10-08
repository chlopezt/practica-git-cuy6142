import requests

while True:
    nombre = input(
        "\nPokémon a consultar (Enter para salir): "
    ).strip().lower()

    if not nombre:
        break

    url = f"https://pokeapi.co/api/v2/pokemon/{nombre}"

    try:
        respuesta = requests.get(url, timeout=10)
        print(f"Código HTTP: {respuesta.status_code}")

        if respuesta.status_code == 404:
            print(f"No existe un Pokémon llamado '{nombre}'.")
            continue

        respuesta.raise_for_status()
        datos = respuesta.json()

        print(f"Nombre: {datos['name'].title()}")
        print(f"Peso: {datos['weight']} hectogramos")
        print("Habilidades:")

        for habilidad in datos["abilities"]:
            print(f" - {habilidad['ability']['name']}")

    except requests.exceptions.RequestException:
        print("No se pudo consultar la API. Revisa tu conexión.")
