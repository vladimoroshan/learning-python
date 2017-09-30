# I'm not native English so don't harsh
	
from sys import exit
	
def tuition():
	print("We are made of the body, mind and spirit. Each part affect others")
	subject = input("What do you want to know about first? Choose one: \n").lower()

	if subject == 'body':		
		print('Good physical habits are:') 
    	print('- healthy eating (eat when you are hungry, until you are 80% full)') 
    	print('- Adequate rest (sleep when you are tired)') 
    	print('- Physical activity/Exercising')
    	print('- Confident body language (Body posture and poses affects how we think and feel)')
    	print('- Voice loud, clear, and deep.')

    elif subject == 'mind':
    	print("The only way to change your brain structure is through your work")
		print("What in your opinion the most important for our brain?")	
		print("Learning new thing, have fun when working or eating chocolate? \n")	
		print("You'd be right if said that's all it")		

	else: 
		print("You didn't choose body or mind. We'll glance at human spirit")
		print("Practical ways for example would remain calm under pressure. Stoicism goes here")
		print("Emotional health as important as personal hygiene")
		

def start():
	print('''We'll play a small life game. \n 
			I know it sounds crazy. At first think for a moment 
			about how long you can stay focused on one task?
			Are you lazy? Are you consistent with your goals? \n
		''')

	will_power = input("If you think that you have a will power type in 'YES': \n").lower()

	desire = input("Do you want to improve yourself? Answer 'YES' or 'NO' \n").lower()

	if will_power == 'yes' and desire == 'yes':		
		print("This is commendable! Let's start \n")
		tuition()

	elif will_power != 'yes' or desire != 'yes':
		print("You don't want to become better or you just lazy. That's pity. World needs YOU!!!")		
		exit(0)

	else:
		print("If you are not sure come back when you decide")
		start()

start()
