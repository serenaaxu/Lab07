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

        ###
        self._dd_musei = None
        self._dd_epoca = None
        self._btn_mostra_artefatti = None
        self._lv_risultati = None
        self.txt_titolo = None
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
            options = [ft.dropdown.Option(key=None, text="Nessun filtro")],
            width = 350,
            value = None
        )
        self._dd_epoca = ft.Dropdown(
            label = "Epoca",
            hint_text = "Seleziona un'epoca'",
            options = [ft.dropdown.Option(key=None, text="Nessun Filtro")],
            width = 350,
            value = None
        )

        # Sezione 3: Artefatti
        # TODO
        self._btn_mostra_artefatti = ft.ElevatedButton(
            text = "Mostra Artefatti",
            on_click = self.controller.handle_mostra_artefatti,
            # icon = ft.icons.SEARCH
        )

        self._lv_risultati = ft.ListView(
            expand = 1,
            spacing = 10,
            padding = 20,
            auto_scroll = True
        )

        container_risultati = ft.Container(
            content=self._lv_risultati,
            border=ft.border.all(1, "grey"),
            border_radius=ft.border_radius.all(5),
            height=400,
            padding=10
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
            ft.Row(controls = [self._btn_mostra_artefatti], alignment = ft.MainAxisAlignment.CENTER), container_risultati
            )

        self.page.scroll = "adaptive"
        self.page.update()

    def cambia_tema(self, e):
        """ Cambia tema scuro/chiaro """
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        self.page.update()



    ###
    def popola_dd_museo(self, musei):
        self._dd_musei.options.clear()
        self._dd_musei.options.append(ft.dropdown.Option(key=None, text="Nessun filtro"))
        for museo in musei:
            self._dd_musei.options.append(
                ft.dropdown.Option(
                    key=museo.id_museo,  # La chiave è l'ID
                    text=museo.nome  # Il testo è il nome
                )
            )
        self.update()

    def popola_dd_epoca(self, epoche):
        self._dd_epoca.options.clear()
        self._dd_epoca.options.append(ft.dropdown.Option(key=None, text="Nessun filtro"))
        for epoca in epoche:
            self._dd_epoca.options.append(
                ft.dropdown.Option(
                    key=epoca,  # Sia chiave che testo sono la stringa 'epoca'
                    text=epoca
                )
            )
        self.update()

    def aggiorna_risultati(self, artefatti):
        self._lv_risultati.controls.clear()
        if not artefatti:
            self._lv_risultati.controls.append(ft.Text("Nessun artefatto trovato."))
        else:
            self._lv_risultati.controls.append(
                ft.Text(f"Trovati {len(artefatti)} artefatti:", weight=ft.FontWeight.BOLD))
            for artefatto in artefatti:
                # Recupero il nome del museo tramite il controller
                museo = self.controller.get_museo_by_id(artefatto.id_museo)
                nome_museo = museo.nome if museo else "Museo Sconosciuto"

                self._lv_risultati.controls.append(
                    ft.Text(f"[{artefatto.epoca}] {artefatto.nome} - {nome_museo}")
                )
        self.update()


