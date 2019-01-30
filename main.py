from video_lib.models import video_path
from docs_lib.models import doc_path
from image_lib.models import img_path
from music_lib.models import music_path

import os

path = os.getcwd()
videos=path+video_path
docs=path+doc_path
images=path+img_path
music=path+music_path