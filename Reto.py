import flet as ft
def main(page: ft.Page):
    page.title = "Reto: Decisiones Interactivas"
	page.window_width = 420
	page.window_width = 720

	estado = {"actual": "inicio"} # cambia con tus tus propios estados

	titulo = ft.Text("Decisiones Interactivas", size=20, weight="bol")
	texto  = ft.Text("", size=18)
	imagen = ft.Image(src="", width=280, height=180, fit=ft.ImageFit.CONTAIn,visible=False)
	btn_si   = ft.ElevatedButton("Sí")
	btn_no	 = ft.ElevatedButton("No")
	btn_reset= ft.TextButton("Reiniciar, icon=ft.Icons.REFRESH") # Corregido
	botones	 = ft.Row([btn_si, btn_no], alignment=ft.MainAxalignment.CENTER, spacing=20)

	def mostrar_inicio():
		estado["actual"] = "inicio"
		page.bgcolor = None
		texto.value = "¿Ayudas al robot a reciclar hoy?"
		imagen.visible = False
		btn_si.visible = True
		btn_no.visible = True
		page.update()

	def a_pregunta2_si():
		estado["actual"] = "final_bueno"
		texto.value  = ¡Exelente
