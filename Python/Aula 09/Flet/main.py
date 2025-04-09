import flet as ft

def main(page: ft.Page):

    def add_item(e):
        page.add(ft.Checkbox(label=item.value))
        item.value = ""
        page.update()


    item = ft.TextField(label="Digite uma tarefa:", border_color="#ffffff")
    tarefas = ft.Text(value="Lista de tarefas", size=30, weight=ft.FontWeight.BOLD)

    page.add(
        ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                item, 
                ft.ElevatedButton(text="Inserir", on_click=add_item)
            ]
        ),
        ft.Row([tarefas])
    )

ft.app(target=main)