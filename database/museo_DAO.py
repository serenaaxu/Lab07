from database.DB_connect import ConnessioneDB
from model.museoDTO import Museo

"""
    Museo DAO
    Gestisce le operazioni di accesso al database relative ai musei (Effettua le Query).
"""

class MuseoDAO:
    def __init__(self):
        pass

    # TODO
    def leggi_musei(self):
        # recupera tutti i musei e li restituisce come lista
        results = []
        cnx = ConnessioneDB.get_connection()

        if cnx is None:
            print("Errore nella connessione al database")
            return None
        else:
            cursor = cnx.cursor(dictionary=True)
            cursor.execute("SELECT * FROM museo")
            for row in cursor:
                museo = Museo(row["id"], row["nome"], row["tipologia"])
                results.append(museo)
            cursor.close()
            cnx.close()
            return results

