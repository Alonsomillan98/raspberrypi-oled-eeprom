'''
Examen practico II - Arquitectura de Computadoras

Carlos Mario Bielma Avendaño			A01730645
Sergio Alonso Saldaña Millán			A01731958
Jonatan Emanuel Salinas Avila           A01731815

30/04/2021
'''

from smbus import SMBus
import time
import board
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

# Define the Reset Pin
oled_reset = digitalio.DigitalInOut(board.D4)

# Change these
# to the right size for your display!
WIDTH = 128
HEIGHT = 32  # Change to 64 if needed
BORDER = 5

# Use for I2C.
i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C, reset=oled_reset)

# Clear display.
oled.fill(0)
oled.show()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
image = Image.new("1", (oled.width, oled.height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a white background
draw.rectangle((0, 0, oled.width, oled.height), outline=0, fill=0)

# Draw a smaller inner rectangle
draw.rectangle(
    (BORDER, BORDER, oled.width - BORDER - 1, oled.height - BORDER - 1),
    outline=0,
    fill=0,
)

# Load default font.
font = ImageFont.load_default()

eeprom_address = 0x50
regmsbyte = 0
reglsbyte = 0

i2cbus = SMBus(1)

if __name__ == '__main__':
	
	listaNumeros = list()
	
	print("Escribe 20 numeros:")
	
	for i in range(0,20):
		numTemp = int(input())
		#numTemp = i+1
		listaNumeros.append(numTemp)
		
	listaNumeros.insert(0,reglsbyte)
	#listaNumeros_bytearray = bytearray(listaNumeros)
	
	#print("Bytearray es: ")
	#print(listaNumeros_bytearray)
	
	#Escribo los primeros 20 datos:
	i2cbus.write_i2c_block_data(eeprom_address, regmsbyte, listaNumeros)
	
	time.sleep(1)
	i2cbus.write_byte_data(eeprom_address, regmsbyte, reglsbyte)
	data1 = i2cbus.read_byte(eeprom_address)
	data2 = i2cbus.read_byte(eeprom_address)
	data3 = i2cbus.read_byte(eeprom_address)
	data4 = i2cbus.read_byte(eeprom_address)
	data5 = i2cbus.read_byte(eeprom_address)
	data6 = i2cbus.read_byte(eeprom_address)
	data7 = i2cbus.read_byte(eeprom_address)
	data8 = i2cbus.read_byte(eeprom_address)
	data9 = i2cbus.read_byte(eeprom_address)
	data10 = i2cbus.read_byte(eeprom_address)
	data11 = i2cbus.read_byte(eeprom_address)
	data12 = i2cbus.read_byte(eeprom_address)
	data13 = i2cbus.read_byte(eeprom_address)
	data14 = i2cbus.read_byte(eeprom_address)
	data15 = i2cbus.read_byte(eeprom_address)
	data16 = i2cbus.read_byte(eeprom_address)
	data17 = i2cbus.read_byte(eeprom_address)
	data18 = i2cbus.read_byte(eeprom_address)
	data19 = i2cbus.read_byte(eeprom_address)
	data20 = i2cbus.read_byte(eeprom_address)
	print("data1:")
	print(data1)
	print("data2:")
	print(data2)
	print("data3:")
	print(data3)
	print("data4:")
	print(data4)
	print("data5:")
	print(data5)
	print("data6:")
	print(data6)
	print("data7:")
	print(data7)
	print("data8:")
	print(data8)
	print("data9:")
	print(data9)
	print("data10:")
	print(data10)
	print("data11:")
	print(data11)
	print("data12:")
	print(data12)
	print("data13:")
	print(data13)
	print("data14:")
	print(data14)
	print("data15:")
	print(data15)
	print("data16:")
	print(data16)
	print("data17:")
	print(data17)
	print("data18:")
	print(data18)
	print("data19:")
	print(data19)
	print("data20:")
	print(data20)
	
	def sumalista(listaNumeros):
		laSuma = 0
		for i in listaNumeros:
			laSuma = laSuma + i
		return laSuma
	
	sumpar = sumalista([data2,data4,data6,data8,data10,data12,data14,data16,data18,data20])
	
	resnon = data1 - data3 - data5 - data7 - data9 - data11 - data13 - data15 - data17 - data19
	mulprim = data2 * data3 * data5 * data7 * data11 * data13 * data17 * data19
	listaMulPrim = list()
	listaMulPrim = [int(i) for i in str(mulprim)]
	dirMul = 30
	pot1 = pow(data3,2)
	pot2 = pow(data6,2)
	pot3 = pow(data9,2)
	pot4 = pow(data12,2)
	pot5 = pow(data15,2)
	pot6 = pow(data18,2)
	sumpot = sumalista([pot1,pot2,pot3,pot4,pot5,pot6])
	
	listaPots = list()
	listaPots = [int(i) for i in str(sumpot)]
	
	dirPot = 40
	listaSumas = list()
	listaSumas.append(sumpar)
	listaRestas = list()
	listaRestas.append(resnon)
	dirMulElem = list()
	dirMulElem.append(dirMul)
	dirPotElem = list()
	dirPotElem.append(dirPot)
	listaSumas.insert(0,21)
	listaRestas.insert(0,22)
	dirMulElem.insert(0,23)
	dirPotElem.insert(0,24)
	i2cbus.write_i2c_block_data(eeprom_address, regmsbyte, listaSumas)
	time.sleep(1)
	i2cbus.write_i2c_block_data(eeprom_address, regmsbyte, listaRestas)
	time.sleep(1)
	i2cbus.write_i2c_block_data(eeprom_address, regmsbyte, dirMulElem)
	time.sleep(1)
	i2cbus.write_i2c_block_data(eeprom_address, regmsbyte, dirPotElem)
	time.sleep(1)
	i2cbus.write_byte_data(eeprom_address, regmsbyte, 21)
	data21 = i2cbus.read_byte(eeprom_address)
	sumParRespaldo = data21
	data22 = i2cbus.read_byte(eeprom_address)
	data23dir = i2cbus.read_byte(eeprom_address)
	data24dir = i2cbus.read_byte(eeprom_address)
	listaMulPrim.insert(0,data23dir)
	i2cbus.write_i2c_block_data(eeprom_address, regmsbyte, listaMulPrim)
	time.sleep(1)
	
	def twos_comp(val, bits):
		if (val & (1 << (bits - 1))) != 0: # if sign bit is set e.g., 8bit: 128-255
			val = val - (1 << bits)        # compute negative value
		return val  
	
	valorReal = twos_comp(data22,8)
	print("data21:")
	print(data21)
	# Draw Some Text
	text = "Suma pares:"
	text1 = str(data2) + ',' + str(data4) + ',' +str(data6) + ',' +str(data8) + ','+str(data10) + ','
	text2 =str(data12) + ','+str(data14) + ','+str(data16) + ','+str(data18) + ','+str(data20)
	(font_width, font_height) = font.getsize(text)
	draw.text(
		(oled.width // 2 - font_width // 2, oled.height // 4.5 - font_height // 2),
		text,
		font=font,
		fill=255,
	)
	draw.text(
		(oled.width // 2 - font_width // 2, oled.height // 2 - font_height // 2),
		text1,
		font=font,
		fill=255,
	)
	draw.text(
		(oled.width // 2 - font_width // 2, oled.height // 1.3 - font_height // 2),
		text2,
		font=font,
		fill=255,
	)
	# Display image
	oled.image(image)
	oled.show()
	time.sleep(3)
	# Draw a smaller inner rectangle
	draw.rectangle(
	  (BORDER, BORDER, oled.width - BORDER - -2, oled.height - BORDER - -2),
	  outline=0,
	  fill=0,
	)
	oled.image(image)
	oled.show()
	time.sleep(1)
	# Draw Some Text
	text3 = "Resultado:"
	text4 = str(data21)
	draw.text(
		(oled.width // 2 - font_width // 2, oled.height // 2 - font_height // 2),
		text3,
		font=font,
		fill=255,
	)
	draw.text(
		(oled.width // 2 - font_width // 2, oled.height // 1.3 - font_height // 2),
		text4,
		font=font,
		fill=255,
	)
	# Display image
	oled.image(image)
	oled.show()
	time.sleep(3)
	# Draw a smaller inner rectangle
	draw.rectangle(
	  (BORDER, BORDER, oled.width - BORDER - -2, oled.height - BORDER - -2),
	  outline=0,
	  fill=0,
	)
	oled.image(image)
	oled.show()
	time.sleep(1)
	print("data22:")
	print(valorReal)
	# Draw Some Text
	text5 = "Resta nones:"
	text6 = str(data1) + ',' + str(data3) + ',' +str(data5) + ',' +str(data7) + ','+str(data9) + ','
	text7 =str(data11) + ','+str(data13) + ','+str(data15) + ','+str(data17) + ','+str(data19)
	(font_width, font_height) = font.getsize(text)
	draw.text(
		(oled.width // 2 - font_width // 2, oled.height // 4 - font_height // 2),
		text5,
		font=font,
		fill=255,
	)
	draw.text(
		(oled.width // 2 - font_width // 2, oled.height // 2 - font_height // 2),
		text6,
		font=font,
		fill=255,
	)
	draw.text(
		(oled.width // 2 - font_width // 2, oled.height // 1.3 - font_height // 2),
		text7,
		font=font,
		fill=255,
	)
	# Display image
	oled.image(image)
	oled.show()
	time.sleep(3)
	# Draw a smaller inner rectangle
	draw.rectangle(
	  (BORDER, BORDER, oled.width - BORDER - -4, oled.height - BORDER - -4),
	  outline=0,
	  fill=0,
	)
	oled.image(image)
	oled.show()
	time.sleep(1)
	# Draw Some Text
	text8 = str(valorReal)
	draw.text(
		(oled.width // 2 - font_width // 2, oled.height // 2 - font_height // 2),
		text3,
		font=font,
		fill=255,
	)
	draw.text(
		(oled.width // 2 - font_width // 2, oled.height // 1.3 - font_height // 2),
		text8,
		font=font,
		fill=255,
	)
	# Display image
	oled.image(image)
	oled.show()
	time.sleep(3)
	# Draw a smaller inner rectangle
	draw.rectangle(
	  (BORDER, BORDER, oled.width - BORDER - -2, oled.height - BORDER - -2),
	  outline=0,
	  fill=0,
	)
	oled.image(image)
	oled.show()
	time.sleep(1)
	
	
	i2cbus.write_byte_data(eeprom_address, regmsbyte, data23dir)
	readMult = list()
	for i in range(0,len(str(mulprim))):
		numTemp = i2cbus.read_byte(eeprom_address)
		readMult.append(numTemp)
	strings = [str(integer) for integer in readMult]
	a_string = "".join(strings)
	data23 = int(a_string)
	print("data23:")
	print(data23)
	
	
	listaPots.insert(0,data24dir)
	i2cbus.write_i2c_block_data(eeprom_address, regmsbyte, listaPots)
	time.sleep(1)
	i2cbus.write_byte_data(eeprom_address, regmsbyte, data24dir)
	readPots = list()
	for i in range(0,len(str(sumpot))):
		numTemp2 = i2cbus.read_byte(eeprom_address)
		readPots.append(numTemp2)
	strings1 = [str(integer1) for integer1 in readPots]
	a_string1 = "".join(strings1)
	data24= int(a_string1)
	
	# Draw Some Text
	text9 = "Multiplicacion:"
	text10 = str(data2) + ',' + str(data3) + ',' +str(data5) + ',' +str(data7) 
	text11 =str(data11) + ','+str(data13) + ','+str(data17) + ','+str(data19)
	(font_width, font_height) = font.getsize(text)
	draw.text(
		(oled.width // 2 - font_width // 2, oled.height // 4 - font_height // 2),
		text9,
		font=font,
		fill=255,
	)
	draw.text(
		(oled.width // 2 - font_width // 2, oled.height // 2 - font_height // 2),
		text10,
		font=font,
		fill=255,
	)
	draw.text(
		(oled.width // 2 - font_width // 2, oled.height // 1.3 - font_height // 2),
		text11,
		font=font,
		fill=255,
	)
	# Display image
	oled.image(image)
	oled.show()
	time.sleep(3)
	# Draw a smaller inner rectangle
	draw.rectangle(
	  (BORDER, BORDER, oled.width - BORDER - -4, oled.height - BORDER - -4),
	  outline=0,
	  fill=0,
	)
	oled.image(image)
	oled.show()
	time.sleep(1)
	# Draw Some Text
	text12 = str(data23)
	draw.text(
		(oled.width // 2 - font_width // 2, oled.height // 2 - font_height // 2),
		text3,
		font=font,
		fill=255,
	)
	draw.text(
		(oled.width // 2 - font_width // 2, oled.height // 1.3 - font_height // 2),
		text12,
		font=font,
		fill=255,
	)
	# Display image
	oled.image(image)
	oled.show()
	time.sleep(3)
	# Draw a smaller inner rectangle
	draw.rectangle(
	  (BORDER, BORDER, oled.width - BORDER - -2, oled.height - BORDER - -2),
	  outline=0,
	  fill=0,
	)
	oled.image(image)
	oled.show()
	time.sleep(1)
	print("data24:")
	print(data24)
	
	# Draw Some Text
	text13 = "Potencias:"
	text14 = str(data3) + ',' + str(data6) + ',' +str(data9)
	text15 =str(data12) + ','+str(data15) + ','+str(data18)
	(font_width, font_height) = font.getsize(text)
	draw.text(
		(oled.width // 2 - font_width // 2, oled.height // 3.8 - font_height // 2),
		text13,
		font=font,
		fill=255,
	)
	draw.text(
		(oled.width // 2 - font_width // 2, oled.height // 2 - font_height // 2),
		text14,
		font=font,
		fill=255,
	)
	draw.text(
		(oled.width // 2 - font_width // 2, oled.height // 1.3 - font_height // 2),
		text15,
		font=font,
		fill=255,
	)
	# Display image
	oled.image(image)
	oled.show()
	time.sleep(3)
	# Draw a smaller inner rectangle
	draw.rectangle(
	  (BORDER, BORDER, oled.width - BORDER - -4, oled.height - BORDER - -4),
	  outline=0,
	  fill=0,
	)
	oled.image(image)
	oled.show()
	time.sleep(1)
	# Draw Some Text
	text16 = str(data24)
	draw.text(
		(oled.width // 2 - font_width // 2, oled.height // 2 - font_height // 2),
		text3,
		font=font,
		fill=255,
	)
	draw.text(
		(oled.width // 2 - font_width // 2, oled.height // 1.3 - font_height // 2),
		text16,
		font=font,
		fill=255,
	)
	# Display image
	oled.image(image)
	oled.show()
	time.sleep(3)
	# Draw a smaller inner rectangle
	draw.rectangle(
	  (BORDER, BORDER, oled.width - BORDER - -2, oled.height - BORDER - -2),
	  outline=0,
	  fill=0,
	)
	oled.image(image)
	oled.show()
	time.sleep(1)
	listaNumerosFinales = list()
	
	print("Escribe 4 numeros:")
	
	for i in range(0,4):
		numTemp = int(input())
		listaNumerosFinales.append(numTemp)
	
	print("Lista es:")
	print(listaNumerosFinales)
	listaNumerosFinales.insert(0,21)
	i2cbus.write_i2c_block_data(eeprom_address, regmsbyte, listaNumerosFinales)
	time.sleep(1)
	i2cbus.write_byte_data(eeprom_address, regmsbyte, 21)
	data21 = i2cbus.read_byte(eeprom_address)
	data22 = i2cbus.read_byte(eeprom_address)
	data23 = i2cbus.read_byte(eeprom_address)
	data24 = i2cbus.read_byte(eeprom_address)
	listaNumerosFinales = sumalista([data21,data22,data23,data24,sumParRespaldo])
	print("data21:")
	print(data21)
	print("data22:")
	print(data22)
	print("data23:")
	print(data23)
	print("data24:")
	print(data24)
	print("suma:")
	print(listaNumerosFinales)
	
	
	# Draw Some Text
	text17 = "Ultima suma:"
	text18 = str(data21) + ',' + str(data22) + ',' +str(data23)+ ','+str(data24)+ ','
	text19 =str(sumParRespaldo) 
	(font_width, font_height) = font.getsize(text)
	draw.text(
		(oled.width // 2 - font_width // 2, oled.height // 3.8 - font_height // 2),
		text17,
		font=font,
		fill=255,
	)
	draw.text(
		(oled.width // 2 - font_width // 2, oled.height // 2 - font_height // 2),
		text18,
		font=font,
		fill=255,
	)
	draw.text(
		(oled.width // 2 - font_width // 2, oled.height // 1.3 - font_height // 2),
		text19,
		font=font,
		fill=255,
	)
	# Display image
	oled.image(image)
	oled.show()
	time.sleep(3)
	# Draw a smaller inner rectangle
	draw.rectangle(
	  (BORDER, BORDER, oled.width - BORDER - -4, oled.height - BORDER - -4),
	  outline=0,
	  fill=0,
	)
	oled.image(image)
	oled.show()
	time.sleep(1)
	# Draw Some Text
	text20 = str(listaNumerosFinales)
	draw.text(
		(oled.width // 2 - font_width // 2, oled.height // 2 - font_height // 2),
		text3,
		font=font,
		fill=255,
	)
	draw.text(
		(oled.width // 2 - font_width // 2, oled.height // 1.3 - font_height // 2),
		text20,
		font=font,
		fill=255,
	)
	# Display image
	oled.image(image)
	oled.show()
	time.sleep(3)
	# Draw a smaller inner rectangle
	draw.rectangle(
	  (BORDER, BORDER, oled.width - BORDER - -2, oled.height - BORDER - -2),
	  outline=0,
	  fill=0,
	)
	oled.image(image)
	oled.show()
	time.sleep(1)