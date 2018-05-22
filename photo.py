import pynstagram
import  pynstagram.data

def upload(file,comment):
    with pynstagram.client(pynstagram.data.get('usr'), pynstagram.data.get('pass')) as client:
     client.upload(file, comment)
