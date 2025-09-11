import flet as ft
import time


def main(page: ft.page):
   page.title = "¿Me perdonas?"
   page.bgcolor=ft.colors.RED_ACCENT_100
   page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
   page.vertical_alignment = ft.MainAxisAlignment.CENTER



   label=ft.Text(
	    "¿Me perdonas?",
    	style=ft.TextStyle(size=40,weight="bold")
   )


   image = ft.Image(src="triste.png", width=200, height=200)

   button_yes=ft.ElevatedButton(text="Si",color=ft.Colors.GREEN,width=100,height=50)
   button_no=ft.ElevatedButton(text="No",color=ft.Colors.RED,width=100,height=50)
   button_maybe=ft.ElevatedButton(text="Quisas",color=ft.Colors.YELLOW,width=100,height=50)


   def no_click(e):
        button_yes.width+=20
        button_yes.hidth+=20
        page.update()


   def yes_click(e):
       image.src = "feliz.png"
       image.update()

   def maybe_click(e):
       image.src = "Quiza.png"
       image.update()

       time.sleep(2)
       reset_app():

   def reset_app():

       image.src = "triste.png"
       button_yes.width=100
       butoon_yes.hidth=50
       page.update()

   button_no.no_click = no_click
   button-yes.on_click = yes_click
   button_maybe.on_click = maybe_click

   page.add(
        ft.Comlumn(
            [
                label,
                image,
                ft.Row([
                    button_yes,
                    button_no,
                    Button_maybe
                ],
                        alignment=ft.MainAxisAlignment.CERNTER,
                 )
            ],
            alignment=ft.MainAxisAlignment.CERNTER,
            horizontal=ft.CrossAxisAlignment.CENTER,
            spancing=20,
        )
   )


ft.app(main)
