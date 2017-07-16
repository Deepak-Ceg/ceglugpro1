import csv
cost=0.0
class Bill:
	price=0.0
	quantity=0.0
	name=' '
	def add(self):
		print('enter item name')
		name=input()
		print('enter item price')
		price=input()
		print('enter the quantity of item')
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
			if k==0:
				print('Do you want to add the item?')
				print('Enter 1 to add and 0 to exit')
				ch=0
				ch=input()
				ch=int(ch)
				if ch==1:
					print('enter price and quantity')
					price=input()
					quantity=input()
					with open('project1.csv','a') as f:
						fieldnames=['Name','Price','Quantity']
						writer=csv.DictWriter(f,fieldnames)
						#writer.writeheader()
						writer.writerow({'Name':name,'Price':price,'Quantity':quantity})
					
		
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
				re[0]['Price']=str(price)
			else:
				print('enter Quantity')
				quanta=input()
				quanta=float(quanta)
				if quanta>1000:
					print('stock overflow!!!please redefine')
					quanta=input()
				re[0]['Quantity']=str(quanta)
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
		global cost
		cost+=float(bind[0]['Price'])*float(bind[0]['Quantity'])
	def billing(self):
		i=1
		while i:
			print('1.add item to cart\n')
			print('0.exit\n')
			i=input()
			if i==str(0):
				break
			else:
				self.display()
				print('enter item\n')
				pro=input()
				print('enter amount\n')
				amt=input()
				updat=0.0
				bind=[]
				temp=[]
				re=[]
				with open('project1.csv','r') as f:
					reader=csv.DictReader(f)
					for row in reader:
						if pro==row['Name']:
							re.append(row)
							bind.append(row)
							
							if float(bind[0]['Quantity'])>=float(amt):								
								updat=bind[0]['Quantity']
								bind[0]['Quantity']=str(amt)
								
							else:
								print('entry is not valid\n')
								print('Do you want to reenter your choice')
								print('type Y to reenter')
								ch=input()
								if ch=='Y'or ch=='y':
									print('Enter amount')
									amt=input()
									updat=bind[0]['Quantity']
									bind[0]['Quantity']=str(amt)
								else:
									continue
									
						if pro!=row['Name']:
							temp.append(row);
					re[0]['Quantity']=updat
					re[0]['Quantity']=float(re[0]['Quantity'])-float(amt)
				with open('project1.csv','w') as f:
					fieldnames=['Name','Price','Quantity']
					writer=csv.DictWriter(f,fieldnames)
					writer.writeheader()
					for row in temp:
						writer.writerow(row)
					writer.writerow(re[0])
			bind[0]['Quantity']=str(amt)
			self.calc(bind)
		print('The cost is'+str(cost))
		print('Thank you for your purchase!!!please do come again!!!')

i=1
print('1 to consumer')
print('2 to owner')
ch=input()
ch=int(ch)
obj=Bill()
if ch == 1:
	print('1.Purchase')
	print('2.Search')
	print('3.Quit')
	co=input()
	co=int(co)
	if co == 1:
		obj.billing()
	elif co == 2:
		obj.search()
elif ch == 2:
	while i:
		print('1.Add Item')
		print('2.Delete')
		print('3.Update the stock section')
		print('4.Display stock')
		print('5.Search')
		print('enter the process number')
		co=input()
		co=int(co)
		if co == 1:
			obj.display()
			obj.add()
		elif co == 2:
			obj.display()
			print('enter name')
			name=input()
			obj.delete(name)
		elif co == 3:
			obj.display()
			print('Enter item_name')
			name=input()
			print('enter 1 to update price 2 for quantity')
			up=input()
			up=int(up)
			if up == 1:
				print('enter the price')
				price=input()
				price=float(price)
				obj.update(name,price)
			else:
				obj.update(name)
		elif co == 4:
			obj.display()
		elif co == 5:
			print('Enter name of product')
			cm=input()
			obj.search(cm)
		print('Enter 1 to continue or 0 to exit')
		i=input()
		i=int(i)
		if i == 0:
			break
print('Thank you for your visit')
