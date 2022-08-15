from text_rewrite import TextRewrite


sentences = ['credit cards provide a tool to help people manage their finances by borrowing money up to a certain credit limit that is then paid back in full or spread over mothly instalments', 'The amount that needs to be paid back will be determined by the interest rate as well as any special offers, which often include interest-free periods when you first take out the card', 'Save 10 percent of your salary each month.', 'Invest in the stock market']
for sentence in sentences:
    new_sentence = TextRewrite(sentence).work() 
    print(sentence + " -> " + new_sentence)
