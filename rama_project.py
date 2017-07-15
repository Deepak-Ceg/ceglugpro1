import csv
#rebuild few items properly
class Bill:
	price=0.0
	quantity=0.0
	name=' '
	def add(self):
		name=input()
		price=input()
		quantity=input()
		with open('project1.csv','a') as f:
			fieldnames=['Name','Price','Quantity']
			writer=csv.DictWriter(f,fieldnames)
			#writer.writeheader()
			writer.writerow({'Name':name,'Price':price,'Quantity':quantity})
	def delete(self,name):
		with open('project1.csv','r') as f:
			temp=[]
			reader=csv.DictReader(f)
			for row in reader:
				if name!=row['Name']:
					temp.append(row);
		with open('project1.csv','w') as f:
			fieldnames=['Name','Price','Quantity']
			writer=csv.DictWriter(f,fieldnames)
			writer.writeheader()
			for row in temp:
				writer.writerow(row)
	def search(self,name):
		k=0
		with open('project1.csv','r') as f:
			reader=csv.DictReader(f)
			for row in reader:
				if name==row['Name']:	
					k=1
					print(row['Name'],row['Price'],row['Quantity'])
		
	def update(self,name,price=None):
		with open('project1.csv','r') as f:
			temp=[]
			re=[]
			reader=csv.DictReader(f)
			for row in reader:
				if name!=row['Name']:
					temp.append(row);
				else:
					re.append(row)
			if price:
				re[0]['Price']=price
			else:
				quanta=input()
				re[0]['Quantity']=quanta
		with open('project1.csv','w') as f:
			fieldnames=['Name','Price','Quantity']
			writer=csv.DictWriter(f,fieldnames)
			writer.writeheader()
			for row in temp:
				writer.writerow(row)
			writer.writerow(re[0])
	def display(self):
		with open('project1.csv','r') as f:
			reader=csv.DictReader(f)
			print('Name,Price,Quantity')
			for row in reader:
					print(row['Name'],row['Price'],row['Quantity'])
	def calc(self,bind):
		cost=0.0
		for row in bind:
			cost+=float(row['Price'])*float(row['Quantity'])
		print('the amount is'+str(cost))
	#problem with calc and data transfer
	def billing(self):
		bi=Bill()
		i=1
		while i:
			print('1.add item to cart\n')
			print('0.exit\n')
			i=input()
			if i==0:
				break
			else:
				bi.display()
				print('enter item\n')
				pro=' '
				pro=input()
				print('enter amount\n')
				amt=0.0
				amt=input()
				updat=0.0
				k=0
				bind=[]
				temp=[]
				re=[]
				with open('project1.csv','r') as f:
					reader=csv.DictReader(f)
					for row in reader:
						if pro==row['Name']:	
							k=1
							re.append(row)
							bind.append(row)
							if bind[0]['Quantity']>=amt:							
								updat=bind[0]['Quantity']
								bind[0]['Quantity']=amt
							else:
								print('entry is not valid\n')
						if pro!=row['Name']:
							temp.append(row);
					re[0]['Quantity']=str(float(re[0]['Quantity'])-updat)
				with open('project1.csv','w') as f:
					fieldnames=['Name','Price','Quantity']
					writer=csv.DictWriter(f,fieldnames)
					writer.writeheader()
					for row in temp:
						writer.writerow(row)
					writer.writerow(re[0])
			test=Bill()
			test.calc(bind)



obj=Bill()
				
"""obj.add() 	
obj.delete(name)
name=input()
price=input()
obj.update(name,price)"""
obj.billing()
