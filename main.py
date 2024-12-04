from flet import *
def light (page:Page) :
    page.window.width=350
    page.window.height=700
    page.window.left=900
    page.title="Light"
    page.bgcolor="white"
    page.theme_mode =ThemeMode.LIGHT

    flsh=Flashlight()
    page.overlay.append(flsh)
    ph= PermissionHandler()
    page.overlay.append(ph)
    
    def open_app (e) :
        ph.open_app_settings()



    page.add(
        AppBar(
            title=Text("Flash light",text_align="center",width=350),
            color="white",
            bgcolor="#e3113e",
            actions=[
                IconButton(icon=icons.SETTINGS,on_click=open_app)
            ] 
        ),
        Row(
        [
            
            Text('\n\nFlash light  app',size=20,color="white",bgcolor="pink",text_align="center",width=320)
        ]
        ),
        Row([
            Image(src="app light/rr.png",width=300,height=200),
        ],alignment=MainAxisAlignment.CENTER),
        Row([
            ElevatedButton(
                "on",
                width=100,
                icon=icons.PLAY_ARROW,
                style=ButtonStyle(
                 bgcolor="#e3113e",
                 padding=20,
                 color="black",
                 shape=ContinuousRectangleBorder(radius=100) 
                ),
                on_click=lambda _:Flashlight.turn_on()
            ),
            ElevatedButton(
                "off",
                width=100,
                icon=icons.PLAY_DISABLED_SHARP,
                style=ButtonStyle(
                 bgcolor="#e3113e",
                 padding=20,
                 color="black",
                 shape=ContinuousRectangleBorder(radius=100) 
                ),
                on_click=lambda _:Flashlight.turn_off()
            ),
        
            
        ],alignment=MainAxisAlignment.CENTER),
        Row(
        [
            
            Text('\n\n\n\nFlash light yousef 2025',size=14,color="white",bgcolor="pink",text_align="center",width=320)
        ]
        ),
        

    )
    page.update()

app(light)
