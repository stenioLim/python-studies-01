class MyContextManger: 
    def __init__(self, file_path,mode_ ):
        self.file_path = file_path
        self.mode_ = mode_
        self._file = None

    def __enter__(self):
        self._file = open(self.file_path, self.mode_)
        return  self._file

    def __exit__(self, calss_exception, exception_, traceback_):
        self._file.close()


    


with MyContextManger('execise.txt', 'w') as _file:
    _file.write('line 1 \n')
    _file.write('line 2 \n')
    _file.write('line 3 \n')
    _file.write('line 4 \n')
    print('with', _file)