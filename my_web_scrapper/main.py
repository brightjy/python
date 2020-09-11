from thebell import get_articles as get_thebell_articles
from faxnet import get_articles as get_faxnet_articles
from save import save_to_file

thebell_articles = get_thebell_articles()
faxnet_articles = get_faxnet_articles()
articles = thebell_articles + faxnet_articles

save_to_file(articles)