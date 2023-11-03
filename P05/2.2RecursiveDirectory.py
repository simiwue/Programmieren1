import os
# Füge hier den Pfad zu deinem Ordner ein.
#  ACHTUNG: r muss vor dem string stehen bleiben.
path = r"<... Dateipfad ...>"

# Erstze alle \ mit / damit python nicht reklamiert
path.replace("\\", "/")

# Zeichen, welches vor jedem Ordner hinzugefügt wird.
prename = "|--"


# rekursive Funktion, welche sich selbst aufruft.
def drill(path, prename):
    # Der Name des Ordners wird herausgelesen und geprintet
    name = os.path.basename(os.path.normpath(path))
    print(prename + name)

    # Überprüfe ob es sich um einen Ordner handelt.
    if os.path.isdir(path):
        # prename wird vergrössert, damit der Name beim print eingerückt ist.
        prename = "|  " + prename

        # Erstelle eine Liste mit allen Dingen im Ordner
        files = os.listdir(path)

        # Erstelle einen neuen Pfad zu jeder Datei/Ordner der Liste
        for file in files:
            new_path = path + "/" + file

            # Ruf die Funktion drill nochmals auf, da es sich um einen Ordner handelt und kontrolliere was darin ist.
            drill(new_path, prename)




# Funktion wird zum ersten Mal aufgerufen
drill(path, prename)