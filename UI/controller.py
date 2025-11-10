import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.museo_selezionato = None
        self.epoca_selezionata = None

    # POPOLA DROPDOWN
    # TODO
    def popola_dropdowns(self):
        try:
            musei = self._model.get_musei()
            self._view.popola_dd_museo(musei)

            epoche = self._model.get_epoche()
            self._view.popola_dd_epoca(epoche)
        except Exception as e:
            print(f"Errore nel popolamento dei dropdown: {e}")
            self._view.show_alert(f"Errore nel caricamento dei filtri: {e}")

    # AZIONE: MOSTRA ARTEFATTI
    # TODO
    def handle_mostra_artefatti(self,e):
        museo_id_selezionato = self._view._dd_musei.value
        epoca_selezionata = self._view._dd_epoca.value

        try:
            artefatti_filtrati = self._model.get_artefatti_filtrati(
                museo_id_selezionato,
                epoca_selezionata
            )
            self._view.aggiorna_risultati(artefatti_filtrati)

            if not artefatti_filtrati:
                self._view.show_alert("Nessun artefatto trovato con i filtri selezionati.")

        except Exception as e:
            print(f"Errore durante il filtraggio: {e}")
            self._view.show_alert(f"Errore: {e}")


    # metodo helper

    def get_museo_by_id(self, museo_id):
        return self._model.get_museo_by_id(museo_id)



