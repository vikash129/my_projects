import pygame as p,random as r,os

p.mixer.init()
p.init()

#creating window
screen_width=720
screen_hight=930
win=p.display.set_mode((screen_width,screen_hight))

#title
p.display.set_caption('snake pygame')
p.display.update()


#creatingclock
clock=p.time.Clock()

exit_game=False
game_over=False
	
#creating colours
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
blue=(0,0,255)
green=(0,220,0)
yellow=(255,255,0)


#bg images
def bgimg(img):
	load=p.image.load(img)
	trans=p.transform.scale(load,
	(screen_width,screen_hight)).convert_alpha()
	win.blit(trans,(0,0))	
	
	

#display score
font=p.font.SysFont(None,60)

def text_screen(text,colour,x,y):
	screen_text=font.render(text,True,colour)
	win.blit(screen_text,(x,y))

		
	
#Increase lenth
def snk_plot(win,colour,snk_body,xsize,ysize):
			for x,y in snk_body:
				p.draw.rect(win,colour,[x,y,xsize,ysize])
	

def music(a):
	p.mixer.music.load(a)
	p.mixer.music.play()
	

	

def welcome():
	exit_game=False
	music('bhthard.mp3')
	while not exit_game:
		
		win.fill((239,234,226))
		bgimg('welbg.jpg')
			
		text_screen('Welcome To SnakeWorld',red,120,250)
		
		text_screen('Controls:',yellow,250,400)
		text_screen('w : Up  |  s : Down',green,160,450)
		text_screen('a : Left  |  d : Right',green,160,490)
		
		text_screen('Press Space To Play',blue,130,600)

		
		for event in p.event.get():
			if event.type==p.QUIT:
				quit()
			elif event.type==p.KEYDOWN:
				if event.key==p.K_SPACE:
					 gameloop()
					
		p.display.update()
		clock.tick(60)
		
	

def gameloop():
		music('emiway.mp3')
		
		#specific variables
		exit_game=False
		game_over=False
		s_x=45
		s_y=120
		s_xsize=25
		s_ysize=30
		ini_v=8
		v_x=0
		v_y=0
		score=0
		fps=60
		snk_len=1
		snk_body=[]
			
			
		#creating food var
		food_x=r.randint(20,screen_width-50)
		food_y=r.randint(50,screen_hight-50)
		food_size=20
		
		#to check existence of file
		if not(os.path.exists('highscore.txt')):
			with open('highscore.txt','w') as f:
				f.write('0')
				
		with open("highscore.txt",'r') as f:
			highscore=f.read()
		
		while not exit_game:
			if game_over:
						#music('dragons.mp3')
						with open('highscore.txt','w')  as f:
							f.write(str(highscore))
						win.fill(white)
						bgimg('gameover.jpg')
						text_screen("GAME OVER !",red,200,500)
						text_screen('ENTER TO START',blue,190,650)
						
						for event in p.event.get():
							if event.type==p.QUIT:
								exit_game=True
							if event.type==p.KEYDOWN:
								if event.key==p.K_RETURN:
									welcome()
			else:
					for event in p.event.get():
						if event.type==p.QUIT:
							exit_game=True
						
						#creating controls
						elif event.type==p.KEYDOWN:
							if event.key==p.K_d:
								v_x=ini_v
								v_y=0
								
							elif event.key==p.K_a:
								v_x=-ini_v
								v_y=0
							
							elif event.key==p.K_w:
								v_y=-ini_v
								v_x=0
							
							elif event.key==p.K_s:
								v_y=ini_v
								v_x=0
								
							elif event.key==p.K_SPACE:#cheat code
								score+=50
								
							elif event.key==p.K_ESCAPE:
								v_x=v_y=0#pause
							
													
						
					#creating velocity
					s_x+=v_x
					s_y+=v_y
					
					#creating score
					if abs(s_x-food_x)<15 and abs(s_y-food_y)<15:
						score+=10
						food_x=r.randint(20,screen_width-200)
						food_y=r.randint(20,screen_hight-200)
						snk_len+=10
						music('point.ogg')
						
						if score>int(highscore):
							highscore=score

					#update length
					head=[]
					head.append(s_x)
					head.append(s_y)
					snk_body.append(head)
					
					
					#reduce length
					if len(snk_body)>snk_len:
						del snk_body[0]
					
					#check collision	
					if head in snk_body[:-1] or (screen_width-10<s_x or s_x<0 )or(screen_hight-20<s_y or s_y<0):
						music('die.ogg')
						game_over=True
					
					#creating snake
					win.fill(white)
					bgimg('snakebg.jpg')
					text_screen("SCORE :"+str(score)+'      HIGHSCORE :'+str(highscore),red,15,50)
					snk_plot(win,green,snk_body,s_xsize,s_ysize)
					
					
					#creating food
					p.draw.rect(win,yellow,[food_x,food_y,food_size,food_size])
			p.display.update()
			clock.tick(fps)
			
		
		#for exit
		p.quit()
		quit()
welcome()