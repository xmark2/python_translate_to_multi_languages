import json
from translate import Translator

languages = ['en','hi','bg','hr','cs','da','nl','et','fi','fr','de','el','hu','ga','it','lv','lt','mt','pl','ro','sk','sl','es','sv']

out_file = open("output_text_translated.json","w")

sentence_lan = []
# sentence_eng = "How are you?"
sentence_eng = input("Please type your text to translate for each languages: ")

for i in range(0,len(languages)):
	links = []
	language = languages[i]

	translator= Translator(to_lang=language)
	translation = translator.translate(sentence_eng)
	
	lang_dic = { 
		'lang_id':			language,
	    'name':            translation
	}

	sentence_lan.append(lang_dic)

my_dict = {
	'id' : 0,
	'sentence_eng' : sentence_eng,
	'translation':	sentence_lan
}


json.dump(my_dict,out_file, indent=4)

out_file.close()