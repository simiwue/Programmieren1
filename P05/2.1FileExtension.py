import os

# Gib hier den Pfad zu deinen Dateien an.
path = r"<Dateipfad...>"

# Ersetze alle \ mit /. Ansonsten gibt es in SyntaxError, weil \ als Escape in Strings benutzt wird.
path.replace("\\", "/")



# Mache eine Liste mit allen Dateien in deisem Ordner
files = os.listdir(path)

# Gehe durch die Liste ändere den Namen der files
for name in files:
    # schneide die letzten drei Buchstaben weg
    new_name = name[:-3]
    # füge MP3 am Ende dazu
    new_name += "MP3"
    # Ersetzte den Pfad der Datei mit einem fast gleichen Pfad
    os.rename(path+name, path+new_name)

           
