import sys
if sys.version_info <= (2, 7):
    reload(sys)
    sys.setdefaultencoding('utf-8')
import konlpy
from konlpy.tag import Kkma
from konlpy.utils import pprint

kkma = Kkma()
pprint(kkma.nouns(u'오늘 날씨는 정말 추운 것 같아요'))
