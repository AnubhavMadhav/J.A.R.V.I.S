import wikipedia
import wolframalpha
import wx
import pyttsx3

engine = pyttsx3.init()

#

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,
            pos=wx.DefaultPosition, size=wx.Size(550, 100),
            style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
             wx.CLOSE_BOX | wx.CLIP_CHILDREN,
            title="PyDa")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel,
        label="Hello I am J.A.R.V.I.S , the Python Digital Assistant made by Anubhav Madhav. How can I help you?")
        engine.say('Hello Anubhav')
        
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER,size=(400,30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()
        engine.runAndWait()
        
    def OnEnter(self, event):
        input = self.txt.GetValue()
        input = input.lower()
       # print("It worked!")
        try:
            app_id = "HH23Y3-5645968TGY"
            client = wolframalpha.Client(app_id)
            res = client.query(input)
            answer = next(res.results).text
            print(answer)
            engine.say('The answer is '+ answer)
            engine.runAndWait()
           
        except:
           # wikipedia.set_lang("es")
           # input = input.split(' ')
           # input = " ".join(input[2:])
            print(wikipedia.summary(input, sentences=2))



if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()
    
    