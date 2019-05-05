import datetime
__tic_toc = datetime.datetime.now()

def tic():
    global __tic_toc
    __tic_toc = datetime.datetime.now()

def toc(show=True):
    if show:
        print(datetime.datetime.now() - __tic_toc)
    else:
        return(datetime.datetime.now() - __tic_toc)