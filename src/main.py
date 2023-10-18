import random
import time
import pygame, sys

from pygame.locals import *

#generates an array with numbers going from 0 to the height of the window
def generateArray(n):
    arr = []
    for _ in range(n):
        arr.append(random.randint(0,(SIZE[1]//100)*100))
    return arr

#draws the array on to the screen
def drawArray(arr, i= 0, j = 0, sortMethod = "", count = 0):
    length = len(arr)
    screen.fill("black")
    for n in range(len(arr)):
        pygame.draw.rect(screen, "white", (n*SIZE[0]//length, SIZE[1]-arr[n], SIZE[0]//length, SIZE[1]))
    pygame.draw.rect(screen, "green", (i*SIZE[0]//length, SIZE[1]-arr[i], SIZE[0]//length, SIZE[1]))
    pygame.draw.rect(screen, "red", (j*SIZE[0]//length, SIZE[1]-arr[j], SIZE[0]//length, SIZE[1]))
    pygame.display.update()
    pygame.display.set_caption(f"{sortMethod}-sort ({len(arr)} elements): {count}")
            


def drawInsertion(arr):
    count = 0
    drawArray(arr,0,0)
    for i in range(1,len(arr)):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            count+= 1
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
            drawArray(arr,i=i,j=j, sortMethod="Bubble", count= count)
            for event in pygame.event.get():
                if event.type == QUIT:
                     return
               


def drawBubble(arr):
    count = 0
    drawArray(arr,len(arr)-1,(len(arr)-1))
    for i in range(len(arr)-1,0,-1):
        for j in range(len(arr)-1,0,-1):
            if (arr[j] < arr[j-1]):
                arr[j], arr[j-1] = arr[j-1], arr[j]
            count += 1
            drawArray(arr,i=i,j=j, sortMethod="Bubble", count= count)
            for event in pygame.event.get():
                if event.type == QUIT:
                     return

def drawSelection(arr):
    count = 0
    drawArray(arr,len(arr)-1,(len(arr)-1))
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            drawArray(arr,i=i,j=j, sortMethod="Selection", count= count)
            for event in pygame.event.get():
                if event.type == QUIT:
                     return
            if (arr[j] < arr[i]):
                arr[i], arr[j] = arr[j], arr[i]
            count += 1


def drawQuick(arr, low, high, count = ""):
    if count == "":
        count = 0
    if len(arr) == 1:
        return
    if low < high:
        i = low
        j = high - 1
        drawArray(arr, i, j, "Quick", count = count)
        pivot = arr[high]

        while i <= j:
            drawArray(arr, i, j, "Quick", count = count)
            for event in pygame.event.get():
                if event.type == QUIT:
                     return
            if arr[i] < pivot:
                i += 1
            
            else:
                if (arr[j] < pivot):
                    arr[i], arr[j] = arr[j], arr[i]
                j-= 1
            count += 1
        arr[i], arr[high] = arr[high], arr[i]

        drawQuick(arr, low, i - 1)
        drawQuick(arr, i + 1, high)


def drawBogo(arr):
    count = 0
    drawArray(arr)
    while  sorted(arr) != arr:
        random.shuffle(arr)
        pygame.display.set_caption(f"Bogo-sort ({len(arr)} elements): {count}")
        count += 1
        drawArray(arr, sortMethod="Bogo", count= count)
        for event in pygame.event.get():
                if event.type == QUIT:
                     return
                
def heapify(arr, N, i):
    parent = i
    left_child = 2*i + 1
    right_child = 2*i + 2

    if (left_child < N and arr[parent] < arr[left_child]):
        parent = left_child
    if (right_child < N and arr[parent] < arr[right_child]):
        parent = right_child

    if parent != i:
        arr[i], arr[parent] = arr[parent], arr[i]
        heapify(arr, N, parent)

def drawHeap(arr):
    count = 0
    N = len(arr)
    drawArray(arr, 0,0, sortMethod="Heap", count=count)
    for i in range(N//2 - 1, -1, -1):
        for event in pygame.event.get():
                if event.type == QUIT:
                     return
        heapify(arr, N, i)
        drawArray(arr, 0,0, sortMethod="Heap", count=count)
        count += 1

    
    # One by one extract elements
    for i in range(N-1, 0, -1):
        for event in pygame.event.get():
                if event.type == QUIT:
                     return
        arr[i], arr[0] = arr[0], arr[i] 
        heapify(arr, i, 0)
        drawArray(arr, 0,0, sortMethod="Heap", count=count)
        count += 1


def drawStalin(arr):
     count = 0
     for i in range(1,len(arr)):
        for event in pygame.event.get():
                if event.type == QUIT:
                     return
        if (arr[i-1] != arr[i]):
               arr[i] = arr[i-1]
        count += 1
        drawArray(arr,i=i, sortMethod= "Stalin", count = count)
        
pygame.init()
SIZE = (1000,600)

screen = pygame.display.set_mode(SIZE)

font = pygame.font.SysFont("Comic Sans", 65)

sorts = [["Bubble", "Selection", "Insertion"], ["Stalin", "Quick", "Heap"]]
done = False

while not done:
    for event in pygame.event.get():
                if event.type == QUIT:
                    done = True
                if event.type == MOUSEMOTION:
                     for i in range(2):
                        for j in range(3):
                            if  150 + i* 400 <= event.pos[0] <= 450 + i*400 and 100+j*140 <= event.pos[1] <= 200 + j*140:
                                pygame.draw.rect(screen, "grey", (150+i*400, 100+j*140, 300, 100))
                                text = font.render(sorts[i][j], True, "black")
                                screen.blit(text, (160+i*400, 100+j*140))
                                pygame.display.update()
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                     for i in range(2):
                        for j in range(3):
                            if  150 + i* 400 <= event.pos[0] <= 450 + i*400 and 100+j*140 <= event.pos[1] <= 200 + j*140:
                                if (i == 0 and j == 0):
                                     arr = generateArray(600)
                                     drawBubble(arr)
                                if (i == 0 and j == 1):
                                     arr = generateArray(600)
                                     drawSelection(arr)
                                if (i == 0 and j == 2):
                                     arr = generateArray(600)
                                     drawInsertion(arr)
                                if (i == 1 and j == 0):
                                     arr = generateArray(600)
                                     drawStalin(arr)
                                if (i == 1 and j == 1):
                                     arr = generateArray(600)
                                     drawQuick(arr,0,599)
                                if (i == 1 and j == 2):
                                     arr = generateArray(600)
                                     drawHeap(arr)

    screen.fill("white")
    for i in range(2):
         for j in range(3):
              pygame.draw.rect(screen, "darkgrey", (150+i*400, 100+j*140, 300, 100))
              text = font.render(sorts[i][j], True, "black")
              screen.blit(text, (160+i*400, 100+j*140))
    pygame.display.update()

pygame.quit()
sys.exit()