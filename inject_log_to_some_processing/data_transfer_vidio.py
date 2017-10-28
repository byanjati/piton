from logging import log_after_do
from base import VidioBase

def __main__():
    impl = ImplBase()
    impl.run()

class ImplBase(VidioBase):
    def extract(self):
        print('[TASK] before extract')
        log_after_do('[TASK] extract_impl_base', super(ImplBase, self).extract())

__main__()
