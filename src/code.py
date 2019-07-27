from gamebuino_meta import begin, waitForUpdate, display, buttons

# **********************************************************************
# Constants

MODE_DISPLAY_CARD   = 0
MODE_MIX_CARD       = 1
MODE_DISPLAY_NB_MIX = 2

# **********************************************************************
# Initialization/reset function

def initialize():
	display.clear()
	display.println("Initialize")
	for c in range(4):
		for n in range(13):
			card = str(n) + ',' + str(c)
			cards.append(card)

def resetIndexPage():
	game['indexPage'] = 0

# **********************************************************************
# Command management

def manageCommand4DisplayCards():
	indexOfPage = game['indexPage']
	if buttons.pressed(buttons.RIGHT):
		if indexOfPage == 1:
			indexOfPage = 0
		else:
			indexOfPage += 1
	elif buttons.pressed(buttons.LEFT):
		if indexOfPage == 0:
			indexOfPage = 1
		else:
			indexOfPage -= 1

	game['indexPage'] = indexOfPage

def manageCommand4Mode():
	try:
		if game['mode'] == MODE_DISPLAY_CARD and buttons.pressed(buttons.A):
			game['mode'] = MODE_MIX_CARD
		elif game['mode'] != MODE_MIX_CARD and buttons.pressed(buttons.MENU):
			game['mode'] = MODE_DISPLAY_NB_MIX if game['mode'] == MODE_DISPLAY_CARD else MODE_DISPLAY_CARD
	except:
		display.print('Error cmd 4 mode')

# **********************************************************************
# Display management

def showCards(n):
	try:
		for r in range(10):
			for c in range(4):
				if n < 52:
					display.print(cards[n])
					display.print(' ')
					n += 1
			display.print('\n')
	except:
		display.print('exception')

def paint():
	if game['indexPage'] == 0:
		showCards(0)
	else:
		showCards(40)

# **********************************************************************
# Mix function

def mixCards():
	subSet1 = []
	subSet2 = []
	subSet3 = []
	subSet4 = []
	# Mix cards
	for i in range(52):
		s = i % 4
		if s == 0:
			subSet1.append(cards[i])
		elif s == 1:
			subSet2.append(cards[i])
		elif s == 2:
			subSet3.append(cards[i])
		else:
			subSet4.append(cards[i])
	# Re-order cards
	n = 0
	for s in range(4):
		subSet = subSet1
		if s == 0:
			subSet = subSet3
		elif s == 1:
			subSet = subSet2
		elif s == 2:
			subSet = subSet4
		for c in range(13):
			cards[n] = subSet[c]
			n += 1
	game['nbMix'] += 1

# **********************************************************************
# Main function

def tick():
	manageCommand4Mode()
	try:
		if game['mode'] == MODE_DISPLAY_CARD:
			manageCommand4DisplayCards()
			display.clear()
			paint()
		elif game['mode'] == MODE_DISPLAY_NB_MIX:
			display.clear()
			display.print('Nb mix: ')
			display.print(str(game['nbMix']))
		else:
			display.clear()
			display.print('Mix cards...')
			mixCards()
			resetIndexPage()
			game['mode'] = MODE_DISPLAY_CARD
	except:
		display.print('tick error ')
		display.print(str(game['mode']))

# **********************************************************************
# Variables of program

cards = []

game = {
	'indexPage': 0,
	'mode': MODE_DISPLAY_CARD,
	'nbMix': 0
}

# **********************************************************************
# Initialization of program

begin()
initialize()

# **********************************************************************
# Main loop

while True:
	waitForUpdate()
	tick()
