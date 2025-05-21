import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora"
    page.bgcolor = "#080808"
    page.window.width = 350
    page.window.height = 420
    page.window_resizable = False # Opcional: impede o redimensionamento
    page.update()

    todos_valores = " "

    resultado_texto = ft.Text(value="0", size=28, color="white", text_align="right")

    def botao_click(e):
        nonlocal todos_valores
        todos_valores += str(e.control.text)
        resultado_texto.value = todos_valores
        page.update()

    def limpar_tela(e):
        nonlocal todos_valores
        todos_valores = " "
        resultado_texto.value = "0"
        page.update()

    def apagar_ultimo_caractere(e):
        nonlocal todos_valores
        if len(todos_valores) > 1:
            todos_valores = todos_valores[:-1]
        else:
            todos_valores = " "
        resultado_texto.value = todos_valores
        page.update()

    def calcular(e):
        nonlocal todos_valores
        try:
            resultado_texto.value = str(eval(todos_valores))
            todos_valores = resultado_texto.value
        except:
            resultado_texto.value = "Error"
            todos_valores = " "
        page.update()

    # Estilo do botão de limpar
    ft.ElevatedButton(
        text="C",
        on_click=limpar_tela,
        bgcolor="#FF3C00",
        color="white",
        height=60,
        expand=1,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=5),
            padding=0
        )
    )

    tela = ft.Container(
        content = resultado_texto,
        bgcolor="#37474F",
        padding=10,
        border_radius=10,
        height=70,
        alignment=ft.alignment.center_right
    )

    # Estilos dos botões
    estilo_numeros = {
        "bgcolor": "#1D5068",
        "color": "white",
        "height": 60,
        "expand": 1,
    }
    estilo_operadores = {
        "bgcolor": "#FCD600",
        "color": "white",
        "height": 60,
        "expand": 1,
    }
    estilo_limpar = {
        "bgcolor": "#FF3C00",
        "color": "white",
        "height": 60,
        "expand": 1,
    }
    estilo_equal = {
        "bgcolor": "#08A50E",
        "color": "white",
        "height": 60,
        "expand": 1,
    }

    grelha_teclado = [
        [
            ("C", estilo_limpar, limpar_tela),
            ("%", estilo_operadores, botao_click),
            ("/", estilo_operadores, botao_click),
            ("*", estilo_operadores, botao_click)
        ],

        [
            ("7", estilo_numeros, botao_click),
            ("8", estilo_numeros, botao_click),
            ("9", estilo_numeros, botao_click),
            ("-", estilo_operadores, botao_click)
        ],

        [
            ("4", estilo_numeros, botao_click),
            ("5", estilo_numeros, botao_click),
            ("6", estilo_numeros, botao_click),
            ("+", estilo_operadores, botao_click)
        ],

        [
            ("1", estilo_numeros, botao_click),
            ("2", estilo_numeros, botao_click),
            ("3", estilo_numeros, botao_click),
            ("=", estilo_equal, calcular)
        ],

        [
            ("0", {**estilo_numeros, "expand":2}, botao_click),
            (".", estilo_operadores, botao_click),
            ("DEL",estilo_operadores, apagar_ultimo_caractere)
        ]
    ]

    botoes = []
    for linha in grelha_teclado:
        linha_control = []
        for texto, estilo, handler in linha:
            btn = ft.ElevatedButton(
                text=texto,
                on_click=handler,
                **estilo,
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=5),
                    padding=0
                    )
                )
            linha_control.append(btn)
        botoes.append(ft.Row(linha_control, spacing=5))

    page.add(
        ft.Column(
            [
                tela,
                ft.Column(botoes, spacing=5)
            ]
        )
    )

ft.app(target=main)
