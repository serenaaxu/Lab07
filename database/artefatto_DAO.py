from database.DB_connect import ConnessioneDB
from model.artefattoDTO import Artefatto

"""
    ARTEFATTO DAO
    Gestisce le operazioni di accesso al database relative agli artefatti (Effettua le Query).
"""

class ArtefattoDAO:
    def __init__(self):
        pass

    # TODO
    def get_all_epoche(self):
        cnx = ConnessioneDB.get_connection()
        result = []
        if cnx is None:
            print("Errore nella connessione al database")
            return result

        cursor = cnx.cursor()
        query = "SELECT DISTINCT epoca FROM artefatto ORDER BY epoca"
        try:
            cursor.execute(query)
            for (epoca,) in cursor.fetchall():
                result.append(epoca)
        except Exception as e:
            print(f"Errore durante l'esecuzione della query: {e}")
        finally:
            cursor.close()
            cnx.close()
        return result

    def get_filtered_artefatti(self, museo_id, epoca):
        cnx = ConnessioneDB.get_connection()
        result = []
        if cnx is None:
            print("Errore nella connessione al database")
            return result

        cursor = cnx.cursor(dictionary=True)
        query = (" SELECT a.* FROM artefatto a "
                " WHERE a.id_museo = COALESCE(%s, a.id_museo))"
                " AND a.epoca = COALESCE(%s, a.epoca))")

        try:
            cursor.execute(query, (museo_id, epoca))
            for row in cursor.fetchall():
                result.append(ArtefattoDTO(
                    row['nome'],
                    row['tipologia'],
                    row['epoca'],
                    row['id_museo'],
                 ))
        except Exception as e:
            print(f"Errore durante la query: {e}")
        finally:
            cursor.close()
            cnx.close()
        return result



