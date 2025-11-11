import flet as ft
from UI.alert import AlertManager

'''
    VIEW:
    - Rappresenta l'interfaccia utente
    - Riceve i dati dal MODELLO e li presenta senza modificarli
'''

class View:
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "Lab07"
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.DARK

        # Alert
        self.alert = AlertManager(page)

        # Controller
        self.controller = None

        self.txt_titolo = None
        self._dd_musei = None
        self._dd_epoca = None
        self.btn_mostra_artefatti = None
        self.lista_risultati_ricerca = None
        self.toggle_cambia_tema = None

    def show_alert(self, messaggio):
        self.alert.show_alert(messaggio)

    def set_controller(self, controller):
        self.controller = controller

    def update(self):
        self.page.update()

    def load_interface(self):
        """ Crea e aggiunge gli elementi di UI alla pagina e la aggiorna. """
        # --- Sezione 1: Intestazione ---
        self.txt_titolo = ft.Text(value="Musei di Torino", size=38, weight=ft.FontWeight.BOLD)

        # --- Sezione 2: Filtraggio ---
        # TODO
        self._dd_musei = ft.Dropdown(
            label = "Museo",
            hint_text = "Seleziona un museo",
            options = self.controller.popola_dropdown_musei(),
            on_change = self.controller.aggiorna_nome_museo,
            width = 350,
            value = None
        )
        self._dd_epoca = ft.Dropdown(
            label = "Epoca",
            hint_text = "Seleziona un'epoca'",
            options = self.controller.popola_dropdown_epoche(),
            on_change = self.controller.aggiorna_epoca,
            width = 350,
            value = None
        )

        # Sezione 3: Artefatti
        # TODO
        self.btn_mostra_artefatti = ft.ElevatedButton(
            text = "Mostra Artefatti",
            width = 200,
            on_click = self.controller.handle_mostra_artefatti,
        )

        self.lista_risultati_ricerca = ft.ListView(
            expand = True,
            spacing = 10,
            padding = 20,
        )

        # --- Toggle Tema ---
        self.toggle_cambia_tema = ft.Switch(label="Tema scuro", value=True, on_change=self.cambia_tema)

        # --- Layout della pagina ---
        self.page.add(
            self.toggle_cambia_tema,

            # Sezione 1
            self.txt_titolo,
            ft.Divider(),

            # Sezione 2: Filtraggio
            # TODO
            ft.Row(controls = [self._dd_musei, self._dd_epoca], alignment = ft.MainAxisAlignment.CENTER),
            ft.Divider(),

            # Sezione 3: Artefatti
            # TODO
            self.btn_mostra_artefatti,
            ft.Divider(),

            self.lista_risultati_ricerca,
            )

        self.page.scroll = "adaptive"
        self.page.update()

    def cambia_tema(self, e):
        """ Cambia tema scuro/chiaro """
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        self.page.update()

