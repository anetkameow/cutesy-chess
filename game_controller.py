import wx
import pygame
import game_view
import game_model


class ChessPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)

        self.SetSize((480, 480))
        self.SetBackgroundColour(wx.Colour(255, 182, 193))  # Pastelowy różowy
        self.Bind(wx.EVT_PAINT, self.on_paint)
        self.Bind(wx.EVT_LEFT_DOWN, self.on_mouse_down)
        self.Bind(wx.EVT_LEFT_UP, self.on_mouse_up)

        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.Surface((480, 480))

        # Ładowanie dźwięków
        self.move_sound = pygame.mixer.Sound("sound.wav")  # Wstaw plik dźwiękowy

        self.Biale_figury = [('W', 1, 0, 0), ('S', 1, 1, 0), ('G', 1, 2, 0), ('K', 1, 3, 0), ('D', 1, 4, 0),
                             ('G', 1, 5, 0), ('S', 1, 6, 0), ('W', 1, 7, 0),
                             ('P', 1, 0, 1), ('P', 1, 1, 1), ('P', 1, 2, 1), ('P', 1, 3, 1), ('P', 1, 4, 1),
                             ('P', 1, 5, 1), ('P', 1, 6, 1), ('P', 1, 7, 1)]

        self.Czarne_figury = [('W', 1, 0, 7), ('S', 1, 1, 7), ('G', 1, 2, 7), ('K', 1, 3, 7), ('D', 1, 4, 7),
                              ('G', 1, 5, 7), ('S', 1, 6, 7), ('W', 1, 7, 7),
                              ('P', 1, 0, 6), ('P', 1, 1, 6), ('P', 1, 2, 6), ('P', 1, 3, 6), ('P', 1, 4, 6),
                              ('P', 1, 5, 6), ('P', 1, 6, 6), ('P', 1, 7, 6)]

        game_model.pozycje(self.Biale_figury, self.Czarne_figury)

        self.tura = 0
        self.moves = []
        self.refresh_board()

    def refresh_board(self):

        game_view.odswiezanie(self.screen, self.Biale_figury, self.Czarne_figury)
        self.Refresh(False)

    def on_paint(self, event):
        """Rysowanie pygame na wx.Panel"""
        dc = wx.PaintDC(self)
        bitmap = wx.Bitmap.FromBuffer(480, 480, pygame.image.tostring(self.screen, "RGB"))
        dc.DrawBitmap(bitmap, 0, 0)

    def on_mouse_down(self, event):
        """Obsługa kliknięcia myszką"""
        self.press_x, self.press_y = event.GetPosition()

    def on_mouse_up(self, event):
        release_x, release_y = event.GetPosition()
        import game_model
        press_x, press_y, release_x, release_y, vec_x, vec_y = game_model.przesuniecie(
            self.press_x, self.press_y, release_x, release_y
        )
        if game_model.ruch(self.Biale_figury, self.Czarne_figury, press_x, press_y, vec_x, vec_y, self.tura,
                           self.moves):
            self.tura += 1
            self.refresh_board()
            self.move_sound.play()  # Odtwarzanie dźwięku po ruchu
            if game_model.mat(self.Biale_figury, self.Czarne_figury, self.tura, self.moves):
                wx.MessageBox("Szach mat!", "Koniec gry", wx.OK | wx.ICON_INFORMATION)
                wx.GetApp().ExitMainLoop()


class CustomMessageDialog(wx.Dialog):
    def __init__(self, parent, title, message):
        super().__init__(parent, title=title, size=(300, 200))

        panel = wx.Panel(self)
        panel.SetBackgroundColour(wx.Colour(225, 0, 127))  # Ustaw kolor tła na różowy

        # Dodajemy sizer, aby ułatwić wyśrodkowanie tekstu
        sizer = wx.BoxSizer(wx.VERTICAL)

        # Tworzymy pole tekstowe z możliwością zawijania
        text = wx.TextCtrl(panel, value=message, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_CENTER)
        text.SetBackgroundColour(wx.Colour(225, 0, 127))  # Dopasowanie koloru tła do panelu
        text.SetForegroundColour(wx.WHITE)  # Kolor tekstu na biały
        text.SetFont(wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))

        # Dodajemy marginesy
        text.SetMargins(10, 10)  # Górny i dolny margines, oraz lewy i prawy margines

        # Dodajemy tekst do sizer i centralizujemy go
        sizer.Add(text, 1, wx.EXPAND | wx.ALL, 10)  # Dodajemy zewnętrzny margines

        # Dodajemy przycisk OK
        ok_button = wx.Button(panel, label="OK")
        ok_button.Bind(wx.EVT_BUTTON, self.on_close)

        sizer.Add(ok_button, 0, wx.ALIGN_CENTER | wx.ALL, 10)  # Przyciski także mają marginesy

        # Ustawiamy sizer
        panel.SetSizerAndFit(sizer)

        # Wyśrodkowanie okna
        self.Centre()
        self.ShowModal()

    def on_close(self, event):
        self.EndModal(wx.ID_OK)


class ChessApp(wx.App):
    def OnInit(self):
        self.frame = wx.Frame(None, title="🎀 Chess in wxPython 🎀", size=(495, 535),
                              style=wx.DEFAULT_FRAME_STYLE & ~wx.RESIZE_BORDER)
        self.frame.SetBackgroundColour(wx.Colour(255, 182, 193))

        self.panel = ChessPanel(self.frame)
        self.frame.Bind(wx.EVT_CLOSE, self.on_close)
        self.ZbudujMenu(self.frame)
        self.frame.Show()
        return True

    def ZbudujMenu(self, frame):
        menu_bar = wx.MenuBar()
        frame.SetMenuBar(menu_bar)

        menu = wx.Menu()
        menu_bar.Append(menu, '🎀 &Plik 🎀')

        # Append the menu items and bind events
        item_exit = menu.Append(wx.ID_EXIT, "🎀 Zakończ 🎀")
        item_about = menu.Append(wx.ID_ABOUT, "💖 O programie 💖")
        item_instrukcja = menu.Append(wx.NewIdRef(), "📖 Instrukcja 📖")

        # Bind events to these items using frame.Bind
        frame.Bind(wx.EVT_MENU, self.zakoncz, item_exit)
        frame.Bind(wx.EVT_MENU, self.about, item_about)
        frame.Bind(wx.EVT_MENU, self.instrukcja, item_instrukcja)

    def instrukcja(self, evt):
        # Wyświetlenie niestandardowego okna dialogowego
        dlg = CustomMessageDialog(self.frame,
                                  "instructione",
                                  "Im just a girl, idk how to play. I merely hope it will get me laid <3")

    def zakoncz(self, evt):
        wx.GetApp().ExitMainLoop()

    def about(self, evt):
        wx.MessageBox('I love my bf so so so muuuuuuuch', "O programie", wx.OK)

    def on_close(self, event):
        wx.GetApp().ExitMainLoop()
        event.Skip()


if __name__ == "__main__":
    app = ChessApp()
    app.MainLoop()
