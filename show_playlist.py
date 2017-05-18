#!/usr/bin/env python


# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import os
import pygame
import time
import sys
import glob

from stat import S_ISREG, ST_CTIME, ST_MODE


queue='./output'
archive='./played'

screen = None;

os.putenv('SDL_VIDEODRIVER', 'fbcon')
try:
   pygame.display.init()
except pygame.error:
   raise Exception('Could not open fbcon')

width = pygame.display.Info().current_w
height = pygame.display.Info().current_h

#width = 640
#height = 480

screen = pygame.display.set_mode((width, height))
pygame.font.init()
pygame.mouse.set_visible(False)

bg = pygame.image.load('wood.jpg')
bg = pygame.transform.scale(bg, (width, height))
screen.blit(bg, bg.get_rect())

# dimensions of the boxes containing people punched in/out
box_width = width * 0.50
box_height = height * 0.85


box_playlist_x = width * 0.41875
box_playlist_x = width * 0.46
box_playlist_y = height * 0.09


# create the "surface" for playlist songs, set transparent
box_playlist = pygame.Surface((box_width, box_height))
box_playlist.set_alpha(180)


# Display header and add a black background
font = pygame.font.Font(None, 60)

header_playlist = font.render('Play List', True, (255, 255, 255))
font_size = header_playlist.get_height()

pygame.draw.rect(screen, (0, 0, 0), (box_playlist_x, height * 0.04, box_width, font_size))

screen.blit(header_playlist, (box_playlist_x, height * 0.04))


# Font size for playlist
font = pygame.font.Font(None, 40)

playlist = []
files = filter(os.path.isfile, glob.glob(queue + "/*.jpg"))

file_date_tuple_list = []
for x in files:
    d = os.path.getmtime(x)
    file_date_tuple = (x,d)
    file_date_tuple_list.append(file_date_tuple)

if file_date_tuple_list:
    file_date_tuple_list.sort(key=lambda x: x[1])

    video_id = str(file_date_tuple_list[0][0])
    video_id = video_id[:-4]
    video_id = video_id.lstrip(queue + '/')

    for filename in file_date_tuple_list:
        playlist.append(filename[0])
else:
    files = filter(os.path.isfile,glob.glob(archive+"/*.jpg"))
    file_date_tuple_list = []

    for x in files:
    	d = os.path.getmtime(x)
    	file_date_tuple = (x,d)
    	file_date_tuple_list.append(file_date_tuple)
    
    if file_date_tuple_list:
    	file_date_tuple_list.sort(key=lambda x: x[1])
    	transfer = file_date_tuple_list[:3]
    
    	for a in transfer:
    		fname = a[0].lstrip(played+"/")
    		fname = fname[:-4]
    		playlist.append(fname)
    		print(fname)		
    		os.rename(archive+"/"+fname+".jpg",queue+"/"+fname+".jpg")
    		os.rename(archive+"/"+fname,queue+"/"+fname)	   
    
    video_id = transfer[0].lstrip(played+"/");
    video_id=video_id[:-4]
    playlist.append("Add more songs")	

text_surface = font.render(playlist[0], True, (255, 255, 255))
font_size = text_surface.get_height()

y = 0
i = 0
for song in playlist:
    if i % 2 == 0:
        text_surface = font.render(song, True, (255, 255, 255))
    else:
        text_surface = font.render(song, True, (0, 0, 0))
        pygame.draw.rect(box_playlist, (255, 255, 255), (0, y, box_width, font_size))

    box_playlist.blit(text_surface, (width * 0.00625, y))
    y += text_surface.get_size()[1]
    i += 1

screen.blit(box_playlist, (box_playlist_x, box_playlist_y))

# show QR code and next song info
info = pygame.Surface((width * 0.40, box_height + header_playlist.get_height()))
info.set_alpha(180)

qr = pygame.image.load('url.png')
qr = pygame.transform.scale(qr, (200, 200))
font = pygame.font.Font(None, 150)
text_surface = font.render('NEXT', True, (255, 255, 255))
info.blit(text_surface, (0, 0))
# for opaqueness
screen.blit(qr, (info.get_width() - qr.get_width() + 10, info.get_height() - qr.get_height() + height * 0.04, qr.get_width(), qr.get_height()))
info.blit(qr, (info.get_width() - qr.get_width(), info.get_height() - qr.get_height(), qr.get_width(), qr.get_height()))

# Next song title
font = pygame.font.Font(None, 40)
next_song = playlist[0]
if len(next_song) >= 30:
    next_song = next_song[:30] + '...'

text_surface = font.render(next_song, True, (255, 255, 255))
info.blit(text_surface, (0, 0))

thumb = pygame.image.load(queue + '/' + video_id + '.jpg')
thumb = pygame.transform.scale(thumb, (200, 200))

# add to screen surface so that transparency of "info" surface has identical background
# attempting to make image non-transparent
# offset by the screen.blit(info, (10... near the bottom of script
screen.blit(thumb, (info.get_width() - thumb.get_width() + 10, height * 0.04, thumb.get_width(), thumb.get_height()))

font = pygame.font.Font(None, 150)
text_surface = font.render('SCAN', True, (255, 255, 255))
info.blit(text_surface, (0, info.get_height() - text_surface.get_height()))

info.blit(thumb, (info.get_width() - thumb.get_width(), 0, thumb.get_width(), thumb.get_height()))

font = pygame.font.Font(None, 40)
text_surface = font.render('To add new songs', True, (255, 255, 255))
info.blit(text_surface, (0, info.get_height() - thumb.get_height()))

youtube = pygame.image.load('YouTube-logo-light.png')
youtube = pygame.transform.scale(youtube, (642, 400))

screen.blit(youtube, (10, 200, 0, 0))

screen.blit(info, (10, height * 0.04))
#                  ^ these x,y need to be in vars cause they are referenced in other places

#update the display
pygame.display.update()
time.sleep(10)




