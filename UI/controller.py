import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._listYear = []
        self._listCountry = []

    def fillDD(self):
        self._model.fillDD()
        self._listYear=self._model.getYears()
        self._listCountry=self._model.getCountries()
        for year in self._listYear:
            self._view.ddyear.options.append(ft.dropdown.Option(year))
        for country in self._listCountry:
            self._view.ddcountry.options.append(ft.dropdown.Option(country))
        self._view.update_page()


    def handle_graph(self, e):
        self._view.txt_result.controls.clear()
        country=self._view.ddcountry.value
        year=self._view.ddyear.value
        self._model.create_graph(country,year)
        self._view.txt_result.controls.append(ft.Text(f"Numero di vertici: {self._model.getNumNodes()} Numero di archi: {self._model.getNumEdges()}"))
        self._view.update_page()


    def handle_volume(self, e):
        self._view.txtOut2.controls.clear()
        volumi = self._model.getVolumi()
        volumi.sort(key=lambda x: x[1], reverse=True)
        for i in volumi:
            self._view.txtOut2.controls.append(ft.Text(f"{i[0]}-->{i[1]}"))
        self._view.update_page()


    def handle_path(self, e):
        self._view.txtOut3.controls.clear()
        try:
            num=int(self._view.txtN.value)
        except ValueError:
            self._view.txtOut3.controls.append(ft.Text(f"Errore nel testo inserito"))
            self._view.update_page()
            return
        best=self._model.find_path(num)
        self._view.txtOut3.controls.append(ft.Text(f"Peso cammino massimo: {best[1]}"))
        for edge in best[0]:
            self._view.txtOut3.controls.append(ft.Text(f"{edge[0].Retailer_name}-->{edge[1].Retailer_name}: {edge[2]}"))
        self._view.update_page()

