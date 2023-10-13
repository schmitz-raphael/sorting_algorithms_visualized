import random
import time
import pygame, sys

from pygame.locals import *

#generates an array with numbers going from 0 to the height of the window
def generateArray(n):
    arr = []
    for _ in range(n):
        arr.append(random.randint(0,SIZE[1]))
    return arr

#draws the array on to the screen
def drawArray(arr, i= 0, j = 0, sortMethod = "", count = 0):
    screen.fill("white")
    for n in range(len(arr)):
        pygame.draw.rect(screen, "red", (n*SIZE[0]//length, SIZE[1]-arr[n], SIZE[0]//length, SIZE[1]))
    pygame.draw.rect(screen, "green", (i*SIZE[0]//length, SIZE[1]-arr[i], SIZE[0]//length, SIZE[1]))
    pygame.draw.rect(screen, "black", (j*SIZE[0]//length, SIZE[1]-arr[j], SIZE[0]//length, SIZE[1]))
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
    for i in range(len(arr)-1,0,-1):
        for j in range(len(arr)-1,0,-1):
            drawArray(arr,i=i,j=j, sortMethod="Selection", count= count)
            for event in pygame.event.get():
                if event.type == QUIT:
                     return
            if (arr[j] < arr[j-1]):
                arr[j], arr[j-1] = arr[j-1], arr[j]
            count += 1


def drawQuick(arr, low, high, count=0):
    if low < high:
        i = low
        j = high - 1

        pivot = arr[high]

        while i < j:
            if arr[i] < pivot:
                i += 1
            
            if (arr[j] < pivot):
                arr[i], arr[j] = arr[j], arr[i]
            
            else:
                j -= 1
            drawArray(arr, i, j, "Quick", count = count)
            count += 1

        arr[i], arr[high] = arr[high], arr[i]

        drawQuick(arr, low, i - 1, count=count)
        drawQuick(arr, i + 1, high, count=count)

def drawBogo(arr):
    count = 0
    drawArray(arr)
    while  sorted(arr) != arr:
        random.shuffle(arr)
        pygame.display.set_caption(f"Bogo-sort ({len(arr)} elements): {count}")
        count += 1
        if (drawArray(arr, sortMethod="Bogo", count= count)):
                return


length = int(input("How many numbers do you want to sort: "))
pygame.init()
SIZE = (1500,1000)

screen = pygame.display.set_mode(SIZE)


arr = generateArray(length)


drawBubble(arr)

done = False

while not done:
    for event in pygame.event.get():
                if event.type == QUIT:
                    done = True

pygame.quit()
sys.exit()