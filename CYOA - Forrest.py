def main():
	answer=input("Excellent! You are lost in a forest and you find yourself at a crossroad. Do you turn left or right? ")
	if answer.lower() == "left":
		answer=input("You find yourself face to face with a bear with a key around it's neck. Do you fight the bear or grab the key and run? (grab/fight) ")
		if answer.lower()=="grab":
			answer=input("Good choice, this beast is way too tough to take on by yourself. You grab the key and run. You now come to a river with an old bridge barely holding itself together. Do you go by the bridge or the stones that lead to the other side? (bridge/stones) ")
			if answer.lower()=="stones":
				answer=input("You take your first step across the stones. things are going fine until halfway though, you slip! You land in the water and current starts taking you downstream fast! You see ahead of you a thin branch over a rock in the river. Do you grab the branch and pull yourself out or let the current carry you downstream? (branch/current) ")
			if answer.lower()=="branch":
				print("You grab the branch and pull yourself up. Just as your body leaves the water the branch snaps. You fall back and crack your head on the rock below.Sorry", name, "better luck next time.")
				answer=input("Do you want to try again? (yes/no) ")
				if answer.lower()=="yes":
					main()
				elif answer.lower()=="no":
					print("Another time then.")
				else:
					quit()
			elif answer.lower()=="current":
				answer=input("The current starts to slow down and you're able to get to the river bank on the other side. You start walking back upstream until you're back at the bridge. In front of you is a dark cave. You can either go down the cave or travel around and hope there another way around, which do you choose? (cave/around) ")
				if answer.lower()=="cave":
					print("You enter the cave and stumble through until you trigger a floor trap. A boulder has started hurling toward you from the entrance. You run down the cave until you come to the end where a stone door with a keyhole blocks your way. You use the key you found from the bear and the door opens. The boulder slams behind you but you are safe in the unlocked room. You see a way out of the cave and it opens up to a path back to your village! You made it out the Forrest!")
					quit()
				elif answer.lower()=="around":
					answer=input("You make your way around a face of a cliff, clinging to the wall. You come across a breaking in the wall. Do you continue around or do you enter the break in the wall? (enter/around) ")
					if answer.lower()=="enter":
						print("You enter the break in the wall. It's dark but you see a light at the end of the tunnel. You make it through and you see a path back to your village! You made it out the Forrest!")
						quit()
					elif answer.lower()=="around":
						print("You continue to make your way around the face of the cliff. The rocks become steeper. You slip and fall to your demise. Sorry", name, "better luck next time.")
						answer=input("Do you want to try again? (yes/no) ")
						if answer.lower()=="yes":
							main()
						elif answer.lower()=="no":
							print("Another time then.")
						else:
							quit()
					else:
						print("Didn't understand that, sorry")
						quit()
			elif answer.lower()=="bridge":
				answer=input("You run along the bridge, it creaks with every step. The bear is running close behind, but the bridge cannot hold its weight! You just make it to the other side just as it crumbles away. The bear lands in the river and is swept away with the current. In front of you is a dark cave. You can either go down the cave or travel around and hope there another way around, which do you choose? (cave/around) ")
				if answer.lower()=="cave":
					print("You enter the cave and stumble through until you trigger a floor trap. A boulder has started hurling toward you from the entrance. You run down the cave until you come to the end where a stone door with a keyhole blocks your way. You use the key you found from the bear and the door opens. The boulder slams behind you but you are safe in the unlocked room. You see a way out of the cave and it opens up to a path back to your village! You made it out the Forrest!")
					quit()
				elif answer.lower()=="around":
					answer=input("You make your way around a face of a cliff, clinging to the wall. You come across a breaking in the wall. Do you continue around or do you enter the break in the wall? (enter/around) ")
					if answer.lower()=="enter":
						print("You enter the cave. It's dark but you see a light at the end of the tunnel. You make it through and you see a path back to your village! You made it out the Forrest!")
						quit()
					elif answer.lower()=="around":
						print("You continue to make your way around the face of the cliff. The rocks become steeper. You slip and fall to your demise. Sorry", name, "better luck next time.")
						answer=input("Do you want to try again? (yes/no) ")
						if answer.lower()=="yes":
							main()
						elif answer.lower()=="no":
							print("Another time then.")
						else:
							quit()
					else:
						quit()
		elif answer.lower()=="fight":
			print("Sorry", name, "This bear was just too strong to take head on. You died this time, better luck next time.")
			answer=input("Do you want to try again? (yes/no) ")
			if answer.lower()=="yes":
				main()
			elif answer.lower()=="no":
				print("Another time then.")
			else:
				quit()
		else:
			print("Didn't understand that, sorry")
			quit()
	elif answer.lower()=="right":
		answer=input("You now come to a river with an old bridge barely holding together. Do you go by the bridge or the stones that lead to the other side? (bridge/stones) ")
		if answer.lower()=="bridge":
			answer=input("You run along the bridge, it creaks with every step, a plank cracks as you make the last step to the other side. You made it. In front of you is a dark cave. You can either go down the cave or travel around and hope there another way around, which do you choose? (cave/around) ")
			if answer.lower()=="cave":
				print("You enter the cave and stumble through until you trigger a floor trap. A boulder has started hurling toward you from the entrance. You run down the cave until you come to the end where a stone door with a keyhole blocks your way. You s ramble for the key but find nothing. The boulder crushes you where you stand. Sorry", name, "better luck next time.")
				answer=input("Do you want to try again? (yes/no) ")
				if answer.lower()=="yes":
					main()
				elif answer.lower()=="no":
					print("Another time then.")
				else:
					quit()
			elif answer.lower()=="around":
				answer=input("You make your way around a face of a cliff, clinging to the wall. You come across a breaking in the wall. Do you continue around or do you enter the break in the wall? (enter/around) ")
				if answer.lower()=="enter":
					print("You enter the break in the wall. It's dark but you see a light at the end of the tunnel. You make it through and you see a path back to your village! You made it out the Forrest!")
					quit()
				elif answer.lower()=="around":
					print("You continue to make your way around the face of the cliff. The rocks become steeper. You slip and fall to your demise. Sorry", name, "better luck next time.")
					answer=input("Do you want to try again? (yes/no) ")
					if answer.lower()=="yes":
						main()
					elif answer.lower()=="no":
						print("Another time then.")
					else:
						quit()
				else:
					print("Didn't understand that, sorry")
					quit()
			else:
				print("Didn't understand that, sorry")
				quit()
		elif answer.lower()=="stones":
			answer=input("You take your first step across the stones. things are going fine until halfway though, you slip! You land in the water and current starts taking you downstream fast! You see ahead of you a thin branch over a rock in the river. Do you grab the branch and pull yourself out or let the current carry you downstream? (branch/current) ")
			if answer.lower()=="branch":
				print("You grab the branch and pull yourself up. Just as your body leaves the water the branch snaps. You fall back and crack your head on the rock below.Sorry", name, "better luck next time.")
				answer=input("Do you want to try again? (yes/no) ")
				if answer.lower()=="yes":
					main()
				elif answer.lower()=="no":
					print("Another time then.")
				else:
					quit()
			elif answer.lower()=="current":
				answer=input("The current starts to slow down and you're able to get to the river bank on the other side. You start walking back upstream until you're back at the bridge. In front of you is a dark cave. You can either go down the cave or travel around and hope there another way around, which do you choose? (cave/around) ")
				if answer.lower()=="cave":
					print ("You enter the cave and stumble through until you trigger a floor trap. A boulder has started hurling toward you from the entrance. You run down the cave until you come to the end where a stone door with a keyhole blocks your way. You s ramble for the key but find nothing. The boulder crushes you where you stand. Sorry", name, "better luck next time.")
					answer=input("Do you want to try again? (yes/no) ")
					if answer.lower()=="yes":
						main()
					elif answer.lower()=="no":
						print("Another time then.")
					else:
						quit()
				elif answer.lower()=="around":
					answer=input("You make your way around a face of a cliff, clinging to the wall. You come across a breaking in the wall. Do you continue around or do you enter the break in the wall? (enter/around) ")
					if answer.lower()=="enter":
						print("You enter the break in the wall. It's dark but you see a light at the end of the tunnel. You make it through and you see a path back to your village! You made it out the Forrest!")
						quit()
					elif answer.lower()=="around":
						print("You continue to make your way around the face of the cliff. The rocks become steeper. You slip and fall to your demise. Sorry", name, "better luck next time.")
						answer=input("Do you want to try again? (yes/no) ")
						if answer.lower()=="yes":
							main()
						elif answer.lower()=="no":
							print("Another time then.")
						else:
							quit()
					else:
						print("Didn't understand that, sorry")
						quit()
				else:
					print("Didn't understand that, sorry")
					quit()
			else:
				print("Didn't understand that, sorry")
				quit()
			if answer.lower()=="branch":
				print("You grab the branch and pull yourself up. Just as your body leaves the water the branch snaps. You fall back and crack your head on the rock below.Sorry", name, "better luck next time.")
				answer=input("Do you want to try again? (yes/no) ")
				if answer.lower()=="yes":
					main()
				elif answer.lower()=="no":
					print("Another time then.")
				else:
					quit()
			elif answer.lower()=="current":
				answer=input("The current starts to slow down and you're able to get to the river bank on the other side. You start walking back upstream until you're back at the bridge. In front of you is a dark cave. You can either go down the cave or travel around and hope there another way around, which do you choose? (cave/around) ")
				if answer.lower()=="cave":
					print ("You enter the cave and stumble through until you trigger a floor trap. A boulder has started hurling toward you from the entrance. You run down the cave until you come to the end where a stone door with a keyhole blocks your way. You s ramble for the key but find nothing. The boulder crushes you where you stand. Sorry", name, "better luck next time.")
					answer=input("Do you want to try again? (yes/no) ")
					if answer.lower()=="yes":
						main()
					elif answer.lower()=="no":
						print("Another time then.")
					else:
						quit()
				elif answer.lower()=="around":
					print("You continue to make your way around the face of the cliff. The rocks become steeper. You slip and fall to your demise. Sorry", name, "better luck next time.")
					answer=input("Do you want to try again? (yes/no) ")
					if answer.lower()=="yes":
						main()
					elif answer.lower()=="no":
						print("Another time then.")
					else:
						quit()
				else:
					print("Didn't understand that, sorry")
					quit()
			else:
				print("Didn't understand that, sorry")
				quit()
	else:
		print("Didn't understand that, sorry")
		quit()

name=input("what is your name? ")
print("Hello", name)
answer=input("interested in a little adventure? (yes/no) ")
if answer.lower()== "yes":
	main()
elif answer.lower()=="no":
	print("Another time then.")
	quit()
else:
	quit()