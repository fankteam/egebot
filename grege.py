import asyncio
from pyrogram import Client, filters

# CHATS_IDS = [-1001743231906, -1001607287290, 'thefankor']
# CHATS_POSTING = [-1001377305762, -1001738819886]

# CHATS_IDS = [-1001461074662, -1001791457933, -1001545101844, -1001634878948, -1001641016891, 'thefankor']
CHATS_IDS = [-1001896434328, -1001689807778, -1001816773231, -1001634878948, -1001641016891, 'thefankor']
CHATS_POSTING = [-1001708635194, -1001567969026, -1001567256850, -1001205695463, -1001677436586]


api_id = 17034324
api_hash = '2d0088f1522eaadc977d4064b578e5d5'


api_id, api_hash = 9752917, '95b28ee23127ddf79f2e461ce89bddff'


app = Client('acc4', api_id=api_id, api_hash=api_hash)


@app.on_message(filters = ~filters.edited)
async def main(client, message):
	# print(message)
	try:
		ch_id = message['sender_chat']['id']
		if ch_id in CHATS_IDS:
			idc = CHATS_IDS.index(ch_id)
			# print(message)
			# await app.send_message(CHATS_POSTING[idc], message.text)
			# await app.send_message(CHATS_POSTING[1], "qql5")
			# await message.forward(CHATS_POSTING[idc])
			# print(message)
			if message['text']:
				text = message['text']
			elif message['caption']:
				text = message['caption']
			else:
				text = None
			if message['media']:
				media = True
				if message['media'] == 'photo':
					media_type = 'photo'
				elif message['media'] == 'video':
					media_type = 'video'
				elif message['media'] == 'animation':
					media_type = 'animation'
				elif message['media'] == 'document':
					media_type = 'document'
				elif message['media'] == 'web_page':
					media_type = 'web_page'
				else:
					media_type = None
			else:
				media = False
			if not media and text:
				await app.send_message(CHATS_POSTING[idc], text)
			elif media and media_type:
				if text and media_type == 'web_page':
					await app.send_message(CHATS_POSTING[idc], text)
				else:
					if media_type == 'photo':
						await app.send_photo(CHATS_POSTING[idc], photo=message[media_type]['file_id'], caption=text)
					elif media_type == 'video':
						await app.send_video(CHATS_POSTING[idc], video=message[media_type]['file_id'], caption=text)
					elif media_type == 'document':
						await app.send_document(CHATS_POSTING[idc], document=message[media_type]['file_id'], caption=text)
					elif media_type == 'animation':
						await app.send_animation(CHATS_POSTING[idc], animation=message[media_type]['file_id'], caption=text)
				# elif text:
				# 	await app.send_message(CHATS_POSTING[idc], 'text '+text+'. Media: '+media_type+' , file_id = '+message[media_type]['file_id'])
				# else:
				# 	await app.send_message(CHATS_POSTING[idc], 'text NONE '+'. Media: '+media_type+' , file_id = '+message[media_type]['file_id'])
	except Exception as e:
		print(e)
		await app.send_message('thefankor', "EXCEPTION " + str(e))


@app.on_message(filters = filters.edited)
async def mainedition(client, message):
	try:
		ch_id = message['sender_chat']['id']
		if ch_id in CHATS_IDS:
			idc = CHATS_IDS.index(ch_id)
			await app.send_message('thefankor', "Message edited in " + str(idc))
	except Exception as e:
		print(e)
		await app.send_message('thefankor', "EXCEPTION " + str(e))



# @app.on_message(filters = ~filters.edited)
# async def main(client, message):
# 	# print(message)
# 	try:
# 		ch_id = message['sender_chat']['id']
# 		if ch_id in CHATS_IDS:
# 			idc = CHATS_IDS.index(ch_id)

# 			await message.forward(CHATS_POSTING[idc])

# 	except Exception as e:
# 		print(e)

app.run()













# async def main():
# 	await app.start()
# 	await app.send_message('thefankor', "qq")




# app.run(main())




