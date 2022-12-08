from pathlib import Path


LOG_FILE = Path(__file__).parent / 'log.txt'

class Log: 
    def _log(self, msg):
        raise NotImplementedError('Implemente o metodo log')

    
    def log_erro(self, msg):
        self._log(f'Error: {msg}')
    def log_sucess(self, msg):
        self._log(f'sucess: {msg}')

class LogFileMixin(Log):
    def _log(self, msg):
        msg_format = f'{msg} ({self.__class__.__name__})'
        print('saveing')
        with open(LOG_FILE, 'a') as file:
            file.write(msg_format)
            file.write('\n')
        

class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ,{self.__class__.__name__}')


if __name__ == '__main__':
    l = LogPrintMixin()
    l.log_erro('QUALQUER COISA')
    l.log_sucess('Que massa')
    lf = LogFileMixin()
    lf.log_erro('QUALQUER COISA')
    lf.log_sucess('Que massa')
    print(LOG_FILE)
