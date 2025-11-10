from database.museo_DAO import MuseoDAO
from database.artefatto_DAO import ArtefattoDAO

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di MuseoDAO e ArtefattoDAO)
'''

class Model:
    def __init__(self):
        self._museo_dao = MuseoDAO()
        self._artefatto_dao = ArtefattoDAO()

        ##
        self._musei = self._museo_dao.get_all_musei()
        self._id_map_musei = {m.id_museo: m for m in self._musei}


    # --- ARTEFATTI ---
    def get_artefatti_filtrati(self, museo:str, epoca:str):
        """Restituisce la lista di tutti gli artefatti filtrati per museo e/o epoca (filtri opzionali)."""
        # TODO
        return self._artefatto_dao.get_filtered_artefatti(museo, epoca)

    def get_epoche(self):
        """Restituisce la lista di tutte le epoche."""
        # TODO
        return self._artefatto_dao.get_all_epoche()

    # --- MUSEI ---
    def get_musei(self):
        """ Restituisce la lista di tutti i musei."""
        # TODO
        return self._musei

###
    def get_museo_by_id(self, museo_id):
        """
        Restituisce un singolo oggetto Museo dalla cache usando il suo ID.
        Metodo helper utile per il controller/view.
        """
        return self._id_map_musei.get(museo_id)



