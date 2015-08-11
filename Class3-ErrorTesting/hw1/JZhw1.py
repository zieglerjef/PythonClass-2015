from random import uniform

class Portfolio(): #initialize portfolio with zero balance
	def __init__(self, cash=0.00):
		self.cash = cash #define cash
		self.portfolio = {"Stock": {}, "Mutual Fund": {}, "Bond": {}} #create dictionary with keys for different types of investments
		self.history = [] #create list of transaction history
		
	def addCash(self, cash): #add cash to portfolio
		self.cash += cash #add new cash amount to existing balance
		self.history.append("Cash deposit of $%.2f, $%.2f remaining." % (cash, self.cash)) #append history log with cash deposit
	
	def withdrawCash(self, cash): #withdraw cash from portfolio
		try:
			if self.cash < cash: #if withdrawal exceeds existing balance return exception
				raise Exception
			else:
				self.cash -= cash #remove cash amount from existing balance
				self.history.append("Cash: withdrawal of $%.2f, $%.2f remaining." % (cash, self.cash)) #append history log with cash withdrawal
		except:
			return "Cannot complete, insufficient funds."
		
	def buyAsset(self, share, asset): #add different assets to portfolio with general function
		try:
			if self.cash < (asset.price * share): #if purchase exceeds existing balance return exception
				raise Exception
			elif asset in self.portfolio[asset.typeName()]: #if asset has already been added to 
				self.portfolio[asset.typeName()][asset] += share
			else:
				self.portfolio[asset.typeName()][asset] = share
		except:
			return "Cannot complete, insufficient funds."			
		self.cash -= asset.price * share
		self.history.append("%s: Purchased %.2f shares of %s, $%.2f remaining." % (asset.typeName(), share, asset.name, self.cash))
	
	def buyMutualFund(self, share, asset): #create specific function to buy mutual funds using buyAsset function
		self.buyAsset(share, asset)
	
	def buyStock(self, share, asset): #create specific function to buy stocks using buyAsset function
		self.buyAsset(int(share), asset) #remember that stocks are bought as whole units
		
	def buyBond(self, share, asset): #create specific function to buy bonds using buyAsset function
		self.buyAsset(share, asset)
	
	def sellAsset(self, share, asset): #sell different assets from portfolio with general function
		self.portfolio[asset.typeName()][asset] -= share #since asset must be owned to sell, don't need if statement		
		self.cash += (asset.sellPrice() * share) #add value of sold assets to balance
		self.history.append("%s: Sold %.2f shares of %s, $%.2f remaining." % (asset.typeName(), share, asset.name, self.cash))
	
	def sellMutualFund(self, share, asset): #create specific function to sell mutual funds using sellAsset function
		self.sellAsset(share, asset)
	
	def sellStock(self, share, asset): #create specific function to sell stocks using sellAsset function
		self.sellAsset(int(share), asset) #remember that stocks are sold as whole units
		
	def sellBond(self, share, asset): #create specific function to sell bonds using sellAsset function
		self.sellAsset(share, asset)
	
	def history(self): #return transaction history
		return '\n'.join(self.history)
		
	def __str__(self): #print output of portfolio contents
		printPortfolio = "Cash: $%.2f \n" %self.cash #set initial printPortfolio to display cash
		for x in self.portfolio:
			printPortfolio += "%s: " %x #add other asset types to printPortfolio
			for y in self.portfolio[x]:
				printPortfolio += "$" + str(self.portfolio[x][y]) + str(y.price) + "\n"
		return printPortfolio

class assetType(): #create class attributes of assets (price and name)
	def __init__(self, price, name):
		self.price = price
		self.name = name

class Stock(assetType): #Stock subclass
	def __init__(self, price, name): #initialize stock subclass with input buy price, set sell price, and specify asset name
		assetType.__init__(self, price, name)
	def typeName(self):
		return "Stock"
	def sellPrice(self):
		return uniform(self.price * 0.5, self.price * 1.5)

class MutualFund(assetType):
	def __init__(self, name):
		assetType.__init__(self, 1.0, name)
	def typeName(self):
		return "Mutual Fund"	
	def sellPrice(self):
		return uniform(self.price * 0.9, self.price * 1.2)

class Bond(assetType):
	def __init__(self, price, name):
		assetType.__init__(self, price, name)
	def typeName(self):
		return "Bond"
	def	sellPrice(self):
		return uniform(0.7 * self.price, 1.3 * self.price)

portfolio = Portfolio()
portfolio.addCash(300.50)
s = Stock(20, "HFH")
portfolio.buyStock(5, s) #alternative: portfolio.buyAsset(5, s)
mf1 = MutualFund("BRT")
mf2 = MutualFund("GHT")
portfolio.buyMutualFund(10.3, mf1)  #alternative: portfolio.buyAsset(10.3, mf1)
portfolio.buyMutualFund(2, mf2)
print(portfolio)
portfolio.sellMutualFund(3, mf1) #alternative: portfolio.sellAsset(3, mf1)
portfolio.sellStock(1, s)
portfolio.withdrawCash(50)
portfolio.history