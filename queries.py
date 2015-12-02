from entity_api import entity_extract
from untitled1 import Article, db, Keyword

# article = Article.query.filter_by(id=92).first()
# print article.category
# article.category = 'Musics'
# db.session.commit()

#data = Article.query.all()
#for article in data:
#    print article.category

#entity_extract(1, "The East India Company in the 1700s conjures pictures of British colonisation. What originally started as trade and business eventually led to 200 years of British Raj for our country.\nAt its peak, the company accounted for about half the global trade specialising in commodities like cotton, indigo, tea and opium, and offering employment to a third of the British workforce.\nAfter the 1857 mutiny in India, all its powers were transferred to the British Crown, and eventually, by 1874, the company was dissolved.\nForwarding into over a century later, in 2005, Mumbai-born entrepreneur, Sanjiv Mehta, with a \u201csense of redemption\u201d, bought the company from its 30 odd owners, and turned it into a luxury food brand.\nThe company now specialises in selling gourmet coffees, chocolates, rare teas, and other luxury-food items through its e-commerce website.\nThe first store was launched in the Mayfair neighborhood in London. Today, the company has escalated commercially and now runs stores across the UK, the Middle East, Europe and Asia, in addition to a successful e-commerce website.\nOn inaugurating the company, Mehta received congratulatory e-mails from thousands of Indians.\n\u201cIt is a dream come true to build a business like this and to acquire a brand like this to own the company,\u201d he said.\u201d\n\nParticipate in this discussion")
# key = Keyword.query.filter_by(id=2).first()
# print key.key_name
for i in range(500, 1290):
    article = Article.query.filter_by(id=i).first()
    if article is None:
        continue
    entity_extract(article.id, article.full_story, 1)
    print "done"
print"all done"