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
        self._dd_musei = ft.Dropdown(label="Musei",
                                     options=[ft.dropdown.Option(1,"Museo Egizio"),
                                              ft.dropdown.Option(2,"Museo Nazionale del Cinema"),
                                              ft.dropdown.Option(2, "Museo d’Arte Orientale (MAO)"),
                                              ft.dropdown.Option(2, "GAM - Galleria Civica d’Arte Moderna e Contemporanea"),
                                              ft.dropdown.Option(2, "Museo Nazionale dell’Automobile"),
                                              ft.dropdown.Option(2, "Museo Nazionale del Risorgimento Italiano"),
                                              ft.dropdown.Option(2, "Museo della Montagna Duca degli Abruzzi"),
                                              ft.dropdown.Option(2, "Museo Pietro Micca e dell’Assedio di Torino del 1706"),
                                              ft.dropdown.Option(2, "Museo di Anatomia Umana Luigi Rolando"),
                                              ft.dropdown.Option(2, "Museo di Antropologia Criminale Cesare Lombroso"),
                                              ft.dropdown.Option(2, "Pinacoteca dell’Accademia Albertina"),
                                              ft.dropdown.Option(2, "Museo della Sindone"),
                                              ft.dropdown.Option(2, "Museo Ferroviario Piemontese"),
                                              ],
                                     width = 300,
                                     hint_text = "Seleziona Museo")

        self._dd_epoca = ft.Dropdown(label="Epoca",
                                     options=[ft.dropdown.Option(1,"Epoca"),])
        # Sezione 3: Artefatti
        # TODO

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
            ft.Row(controls = [self._dd_musei, self._dd_epoca], alignment = ft.MainAxisAlignment.CENTER)

            # Sezione 3: Artefatti
            # TODO
        )

        self.page.scroll = "adaptive"
        self.page.update()

    def cambia_tema(self, e):
        """ Cambia tema scuro/chiaro """
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        self.page.update()
