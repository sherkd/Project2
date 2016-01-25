import pygame
import time

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("song.wav")
pygame.mixer.music.play(-1)
class Button:
   def __init__(self, text):
      self.text = text
      self.is_hover = False
      self.default_color = (191,191,191)
      self.hover_color = (255,255,255)
      self.font_color = (0,0,0)
      self.obj = None

   def button(x,y,w,h,action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            if click[0] == 1 and action != None:
                if action == 'Tow Players':
                    pygame.quit()
                    quit()
            elif action == 'Quit':
                pygame.quit()
                quit()

   def label(self):
      '''button label font'''
      font = pygame.font.Font(None, 20)
      return font.render(self.text, 1, self.font_color)

   def color(self):
      '''change color when hovering'''
      if self.is_hover:
         return self.hover_color
      else:
         return self.default_color

   def draw(self, screen, mouse, rectcoord, labelcoord):
      '''create rect obj, draw, and change color based on input'''
      self.obj  = pygame.draw.rect(screen, self.color(), rectcoord)
      screen.blit(self.label(), labelcoord)

      #change color if mouse over button
      self.check_hover(mouse)

   def check_hover(self, mouse):
      '''adjust is_hover value based on mouse over button - to change hover color'''
      if self.obj.collidepoint(mouse):
         self.is_hover = True
      else:
         self.is_hover = False
def TwoPlayers():
    pygame.mixer.music.load("song.wav")
    pygame.mixer.music.play(-1)

if __name__ == '__main__':


   tp = Button('Two Players')
   fp = Button('Four Players')
   rl = Button('Rules')
   qt = Button('Quit')
   screen = pygame.display.set_mode((800,600))
   clock = pygame.time.Clock()

   run = True
   while run:
      screen.fill((230,230,230))
      mouse = pygame.mouse.get_pos()
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            run = False
         elif event.type == pygame.MOUSEBUTTONDOWN:
            if tp.obj.collidepoint(mouse):
               print('Two Players button clicked')
            elif fp.obj.collidepoint(mouse):
               print('Four Players button clicked')
            elif rl.obj.collidepoint(mouse):
               print('Rules button clicked')
            elif qt.obj.collidepoint(mouse):
               print('Quit button clicked')

      tp.draw(screen, mouse, (370,100,100,20), (382,103))
      fp.draw(screen, mouse, (370,130,100,20), (380,133))
      rl.draw(screen, mouse, (370,160,100,20), (400,163))
      qt.draw(screen, mouse, (370,450,100,20), (405,453))
      #btn.check_hover(mouse)

      pygame.display.update()
      clock.tick(60)

pygame.quit()
quit()
