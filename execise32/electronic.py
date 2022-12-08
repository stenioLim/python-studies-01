from log import LogPrintMixin, LogFileMixin

class Electronic:
    def __init__(self, name):
        self._name = name
        self._on = False

    def on(self):
        if not self._on:
            self._on = True
    
    def off(self):
        if self._on:
            self._on = False

class SmartPhone(Electronic, LogFileMixin):

    def on(self):
        super().on()

        if self._on:
            msg = f'{self._name} its on'
            self.log_sucess(msg)

    def off(self):
        super().off()
        
        if not self._on:
            msg = f'{self._name} its off'
            self.log_sucess(msg)
