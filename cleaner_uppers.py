def observationCleaner(observation):
	if observation in ("NA", "-9999", "-999", "-9999.00", "-999.00"):
		obs = "NULL"
	else:
		obs = observation
	return	obs

def nullStringer(observation, is_int=False, is_float=False):
	nullString = ""
# 	for some reason not *all* of the values are strings 
	try:
		if "%" in observation:
			observation = float(observation[:-1])/100
	except:
		pass
	# now cast if not null
	if observation == "NULL":
		nullString += ", NULL"
	else:
		if is_float:
			nullString += ", %f" %(float(observation))
		elif is_int:
			nullString += ", %i" %(int(observation))
	return nullString
