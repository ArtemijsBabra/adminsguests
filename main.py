# main.py
# Programma: Datu apvienošana un analīze

# --- 1. Nolasām failus ---
with open("admin.txt", "r", encoding="utf-8") as f:
    admin_dati = f.readlines()

with open("viesis.txt", "r", encoding="utf-8") as f:
    viesu_dati = f.readlines()

# --- 2. Apvienojam datus ---
visi_dati = admin_dati + viesu_dati

# --- 3. Pārveidojam uz strukturētu formu ---
personas = []
for rinda in visi_dati:
    vardi = rinda.strip().split()
    if len(vardi) == 4:
        persona = {
            "vards": vardi[0],
            "uzvards": vardi[1],
            "loma": vardi[2],
            "vecums": int(vardi[3])
        }
        personas.append(persona)

# --- 4. Izdrukā visus datus ---
print("==== VISI LIETOTĀJI ====")
for p in personas:
    print(f"{p['vards']} {p['uzvards']} - {p['loma']} ({p['vecums']} gadi)")

# --- 5. Aprēķinām administratoru statistiku ---
admini = [p for p in personas if p["loma"].lower() == "administrators"]
viesi = [p for p in personas if p["loma"].lower() == "viesis"]

if admini:
    videjais_vecums = sum(p["vecums"] for p in admini) / len(admini)
    vecakais = max(admini, key=lambda x: x["vecums"])
    jaunakais = min(admini, key=lambda x: x["vecums"])

    print("\n==== ADMINISTRATORU STATISTIKA ====")
    print(f"Vidējais vecums: {videjais_vecums:.1f}")
    print(f"Vecākais: {vecakais['vards']} {vecakais['uzvards']} ({vecakais['vecums']} gadi)")
    print(f"Jaunākais: {jaunakais['vards']} {jaunakais['uzvards']} ({jaunakais['vecums']} gadi)")

# --- 6. Saskaitām lomas ---
print("\n==== KOPSAVILKUMS ====")
print(f"Administratoru skaits: {len(admini)}")
print(f"Viesu skaits: {len(viesi)}")
