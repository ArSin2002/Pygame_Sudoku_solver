import pygame
import requests

WIDTH =550
background_color =(251,247,245)
original_grid_element_color = (52,31,151)
buffer=5

# url = "https://sudoku-generator1.p.rapidapi.com/sudoku/generate"

# querystring = {"seed":"1337"}

# headers = {
# 	"X-RapidAPI-Key": "3a5e882512msh94f27218e3a93fap15c51fjsnf1ac22a77aa9",
# 	"X-RapidAPI-Host": "sudoku-generator1.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers, params=querystring)
# grid=response.json()['puzzle']

grid=[  [3, 0, 6, 5, 0, 8, 4, 0, 0],          
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0], 
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]

grid_original =[[3, 0, 6, 5, 0, 8, 4, 0, 0],
                [5, 2, 0, 0, 0, 0, 0, 0, 0],
                [0, 8, 7, 0, 0, 0, 0, 3, 1],
                [0, 0, 3, 0, 1, 0, 0, 8, 0],
                [9, 0, 0, 8, 6, 3, 0, 0, 5],
                [0, 5, 0, 0, 9, 0, 6, 0, 0], 
                [1, 3, 0, 0, 0, 0, 2, 5, 0],
                [0, 0, 0, 0, 0, 0, 0, 7, 4],
                [0, 0, 5, 2, 0, 6, 3, 0, 0]]

def isempty(num):
    if num == 0:
        return True
    return False

def isvalid(position,num):
    for i in range(len(grid[0])):
        if grid[position[0]][i]==num:
            return False
    
    for i in range(len(grid)):
        if grid[i][position[1]]==num:
            return False
    
    x=position[0]//3*3
    y=position[1]//3*3

    for i in range(3):
        for j in range(3):
            if grid[x+i][y+j]==num:
                return False
    return True

solved=0
def sudoku_solver(win):
    myfont=pygame.font.SysFont('Comic Sans MS',35)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if isempty(grid[i][j]):
                for k in range(1,10):
                    if isvalid((i,j),k):
                        grid[i][j]=k
                        value=myfont.render(str(k),True,(0,0,0))
                        win.blit(value,(((j+1)*50+15 , (i+1)*50)))
                        pygame.display.update()
                        pygame.time.delay(0)

                        sudoku_solver(win)
                        global solved
                        if solved==1:
                            return
                        
                        grid[i][j]=0
                        pygame.draw.rect(win,background_color,((j+1)*50+buffer,(i+1)*50+buffer,50-2*buffer,50-2*buffer))
                        pygame.display.update()
                return
    solved=1

def insert(win,position):
    i=position[1]
    j=position[0]
    myfont=pygame.font.SysFont('Comic Sans MS',35)

    while True:
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                return 
            
            if event.type==pygame.KEYDOWN:
            
                if (grid_original[i-1][j-1]!=0):
                    return 
            
                if (event.key==48):
                    grid[i-1][j-1]=event.key-48
                    pygame.draw.rect(win,background_color,(position[0]*50+buffer ,position[1]*50+buffer,50-2*buffer,50-2*buffer))
                    pygame.display.update()
                    return
                if (0< event.key -48 <10):
                    pygame.draw.rect(win,background_color,(position[0]*50+buffer ,position[1]*50+buffer,50-2*buffer,50-2*buffer))
                    value=myfont.render(str(event.key-48) , True ,(0,0,0))
                    win.blit(value,(position[0]*50+15,position[1]*50))
                    grid[i-1][j-1]=event.key-48
                    pygame.display.update()
                    return
                return 
       
def main():
    pygame.init()
    win=pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption("Sudoku")
    win.fill(background_color)
    myfont=pygame.font.SysFont('Comic Sans MS',35)

    for i in range(0,10):
        if i%3==0:
            pygame.draw.line(win,(0,0,0),(50+50*i,50),(50*i+50,500),4)
            pygame.draw.line(win,(0,0,0),(50,50+50*i),(500,50+50*i),4)
        
        pygame.draw.line(win,(0,0,0),(50+50*i,50),(50*i+50,500),2)
        pygame.draw.line(win,(0,0,0),(50,50+50*i),(500,50+50*i),2)
    

    for i in range(0,len(grid)):
        for j in range(0,len(grid[0])):
            if (0<grid[i][j]<10):
                value=myfont.render(str(grid[i][j]),True,original_grid_element_color)
                win.blit(value,((j+1)*50+15 , (i+1)*50))

    pygame.display.update()
    solve=False
    while True:
        for event in pygame.event.get():
           
            if event.type==pygame.KEYDOWN:
                # print('a')
                if event.key==pygame.K_SPACE:
                    # solve=True
                    sudoku_solver(win)
            
            if event.type == pygame.MOUSEBUTTONUP and event.button==1:
                pos=pygame.mouse.get_pos()
                insert(win,(pos[0]//50,pos[1]//50))
            
        # if solve:
        #     sudoku_solver(win)


            
            if event.type == pygame.QUIT:
                pygame.quit()
                return

main()
