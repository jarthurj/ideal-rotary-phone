from django import forms

COLOR_CHOICES = (
	('U','Blue'),
	('B','Black'),
	('W','White'),
	('R','Red'),
	('G','Green'))
EXACT = (
	('exact','Exactly these colors'),
	('contains','Contains these colors'),
	('at_most','At most these colors'),
	('default','-'))
RARITY = (
	('mythic','Mythic'),
	('rare','Rare'),
	('uncommon','Uncommon'),
	('common','Common'))
MPT = (
	("none","-"),
	('mana', 'Converted Mana Cost'),
	('power', 'Power'),
	('toughness', 'Toughness'),)
MPTCONS = (
	("none","-"),
	("equal","equal to"),
	("gt","greater than"),
	("lt","less than"),
	("lte","less than or equal to"),
	("gte","greater than or equal to"),
	("nte","not equal to"),)
LRB = (
	("none","-"),
	("banned","Banned"),
	("restricted","Restricted"),
	("legal","Legal"),)
GAME_TYPES=(
	("none","-"),
	('standard',"Standard"),
	('historic',"Historic"),
	('pioneer',"Pioneer"),
	('premodern',"Premodern"),
	('paupercommander',"Paupercommander"),
	('duel',"Duel"),
	('oldschool',"Oldschool"),
	('modern',"Modern"),
	('brawl',"Brawl"),
	('pauper',"Pauper"),
	('predh',"Predh"),
	('future',"Future"),
	('vintage',"Vintage"),
	('legacy',"Legacy"),
	('oathbreaker',"Oathbreaker"),
	('historicbrawl',"Historicbrawl"),
	('penny',"Penny"),
	('alchemy',"Alchemy"),
	('commander',"Commander"),
	('gladiator',"Gladiator"),
	('explorer',"Explorer"),)

	
class CardSearch(forms.Form):
	card_name = forms.CharField(max_length=50, 
				required=False,
				widget=forms.TextInput(attrs={'class':'form-control mb-3'
					,'placeholder':'Any words in the name ex."Fire"'}),
				label="Card Name:")

	any_text = forms.CharField(max_length=50,
				required=False,
				label="Text:",
				widget=forms.TextInput({'class':'form-control mb-3'
					,'placeholder':'Any text on the card ex."Draw a card"'}))

	colors = forms.MultipleChoiceField(
				widget=forms.CheckboxSelectMultiple(),
				choices=COLOR_CHOICES,required=False,
				label="Colors:")


	exactly_or_not = forms.MultipleChoiceField(
				widget=forms.SelectMultiple(),
				choices=EXACT,
				required=False,
				initial=EXACT[3],
				label="")

	colors_identity = forms.MultipleChoiceField(
				widget=forms.CheckboxSelectMultiple(attrs={}),
				choices=COLOR_CHOICES,required=False,
				label="Color Identity:")

	rarity = forms.MultipleChoiceField(
				widget=forms.CheckboxSelectMultiple,
				choices=RARITY,required=False,
				label="Rarity:")

	#mpt = mana power toughness
	mpt = forms.MultipleChoiceField(
				widget=forms.Select(attrs={'class':'form-select'}),
				choices=MPT,required=False,
				label="Stats:")

	mpt_condition = forms.MultipleChoiceField(
				widget=forms.Select(attrs={'class':'form-select'}),
				choices=MPTCONS,required=False,
				label="")

	mpt_parameter = forms.CharField(max_length=10, required=False, 
		label="",
		widget=forms.TextInput(attrs={'class':'form-control mb-3'
					,'placeholder':'ex. 6'}))

	lrb = forms.MultipleChoiceField(
				widget=forms.Select(attrs={'class':'form-select'}),
				choices=LRB,required=False,
				label="Formats:")

	game_types = forms.MultipleChoiceField(
				widget=forms.Select(attrs={'class':'form-select'}),
				choices=GAME_TYPES,required=False,
				label="")

	type_line = forms.CharField(max_length=50,required=False,
		label="Type Line:",
		widget=forms.TextInput(attrs={'class':'form-control mb-3'
					,'placeholder':'ex."Creature"'}))
	