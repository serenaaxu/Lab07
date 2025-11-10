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
    def get_all_musei(self):
        # recupera tutti i musei e li restituisce come lista
        cnx = ConnessioneDB.get_connection()
        result = []
        if cnx is None:
            print("Errore nella connessione al datatbase")
            return result

        cursor = cnx.cursor(dictionary=True)
        query = "SELECT id AS id_museo, nome FROM museo ORDER BY nome"
        try:
            cursor.execute(query)
            for row in cursor.fetchall():
                result.append(MuseoDTO(
                    row['id_museo'],
                    row['nome'],
                ))
        except Exception as e:
            print(f"Errore durante l'esecuzione della query: {e}")
        finally:
            cursor.close()
            cnx.close()
        return result

