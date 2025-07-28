import cv2

import sys
import os

# Funzione per trovare i file nell'eseguibile
def resource_path(relative_path):
    try:
        # PyInstaller crea una cartella temporanea e memorizza il percorso in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)






import pygame
import random
# Inizializza Pygame
pygame.init()

# Imposta dimensioni finestra
size = width, height = 1500, 900
schermo = pygame.display.set_mode(size)
pygame.display.set_caption("FALL OUT")

# Carica l'immagine di sfondo FUORI dal loop
sfondo_img = pygame.image.load(resource_path("racist_game/sfondo_character1.png"))
sfondo_img = pygame.transform.scale(sfondo_img, (1500, 900))
# testi 
# Mostra punti (opzionale)
          
font = pygame.font.Font(resource_path("racist_game/street_of_r.ttf"), 36)

tempo = pygame.time.Clock()
running = True
# carica immagini scheramte iniziale, finale
schermata_iniziale_img = pygame.image.load(resource_path("racist_game/schermata_iniziale.png")).convert_alpha()
# Usa l'icona di Diddy come icona del gioco
icon = pygame.transform.scale(schermata_iniziale_img, (32, 32))  # Ridimensiona a 32x32
pygame.display.set_icon(icon)

schermata_iniziale_img = pygame.transform.scale(schermata_iniziale_img, (1500, 900))
schermata_finale_img = pygame.image.load(resource_path("racist_game/schermata_finale.png")).convert_alpha()
schermata_finale_img = pygame.transform.scale(schermata_finale_img, (1500, 900))
# Carica immagini personaggi
diddy_img = pygame.image.load(resource_path("racist_game/Diddy.png")).convert_alpha()
bonnie_img = pygame.image.load(resource_path("racist_game/Bonnie_blue.png")).convert_alpha()
dux_img = pygame.image.load(resource_path("racist_game/dux.png")).convert_alpha()
tate_img = pygame.image.load(resource_path("racist_game/tate.png")).convert_alpha()

#coricie
cornice_img= pygame.image.load(resource_path("racist_game/glow_frame.png")).convert_alpha()
cornice_img= pygame.transform.scale(cornice_img, (340, 310))
posizione_cornice_diddy= (430,150)
posizione_cornice_bonnie=(730,150)
posizione_cornice_dux=(130,150)
posizione_cornice_tate=(1030,150)

# play button
play_button_pos= (1100, 580)
play_button_size= (400, 300)

play_button_img = pygame.image.load(resource_path("racist_game/play_button.png")).convert_alpha()
play_button_img = pygame.transform.scale(play_button_img, (play_button_size[0], play_button_size[1]))

play_button_rect = pygame.Rect(play_button_pos[0], play_button_pos[1], 400, 300)

light_img = pygame.image.load(resource_path("racist_game/light.png")).convert_alpha()
light_img = pygame.transform.scale(light_img, (play_button_size[0], play_button_size[1]))

# statistiche personaggi 
stats_img= pygame.image.load(resource_path("racist_game/stats.png")).convert_alpha()
stats_img= pygame.transform.scale(stats_img, (450, 450))

_5_stelle_img= pygame.image.load(resource_path("racist_game/5_stelle.png")).convert_alpha()
_5_stelle_img= pygame.transform.scale(_5_stelle_img, (80, 80))
distanza_stelle= 60

#stands
diddy_stand=pygame.image.load(resource_path("racist_game/diddy_stand.png")).convert_alpha()
diddy_stand= pygame.transform.scale(diddy_stand, (500, 500))

bonnie_stand=pygame.image.load(resource_path("racist_game/Bonnie_stand.png")).convert_alpha()
bonnie_stand= pygame.transform.scale(bonnie_stand, (600, 500))

dux_stand=pygame.image.load(resource_path("racist_game/dux_stand.png")).convert_alpha()
dux_stand= pygame.transform.scale(dux_stand, (500, 500))

tate_stand=pygame.image.load(resource_path("racist_game/tate_stand.png")).convert_alpha()
tate_stand= pygame.transform.scale(tate_stand,(500,500))

# nomi personaggi 
tate_name=pygame.image.load(resource_path("racist_game/tate_name.png")).convert_alpha()
bonnie_name=pygame.image.load(resource_path("racist_game/bonnie_name.png")).convert_alpha()
duce_name=pygame.image.load(resource_path("racist_game/dux_name.png")).convert_alpha()
diddy_name=pygame.image.load(resource_path("racist_game/diddy_name.png")).convert_alpha()

tate_name= pygame.transform.scale(tate_name, (280, 80))
bonnie_name= pygame.transform.scale(bonnie_name, (300, 100))
duce_name= pygame.transform.scale(duce_name, (280, 80))
diddy_name= pygame.transform.scale(diddy_name, (280, 80))

#grandezza icone personaggi
ICONA_LARGHEZZA = 250
ICONA_ALTEZZA = 250

# Ridimensiona le icone
diddy_img = pygame.transform.scale(diddy_img, (ICONA_LARGHEZZA, ICONA_ALTEZZA))
bonnie_img = pygame.transform.scale(bonnie_img, (ICONA_LARGHEZZA, ICONA_ALTEZZA))
dux_img = pygame.transform.scale(dux_img, (ICONA_LARGHEZZA, ICONA_ALTEZZA))
tate_img = pygame.transform.scale(tate_img, (ICONA_LARGHEZZA, ICONA_ALTEZZA))

# Posizioni delle icone (coordinate dall'immagine di riferimento)
diddy_pos = (460, 170)  # Seconda posizione
bonnie_pos = (780, 170)  # Terza posizione
dux_pos = (140, 170)  # Prima posizione
tate_pos = (1100, 170)  # Quarta posizione

# Crea rettangoli per il click detection
diddy_rect = pygame.Rect(diddy_pos[0], diddy_pos[1], ICONA_LARGHEZZA, ICONA_ALTEZZA)
bonnie_rect = pygame.Rect(bonnie_pos[0], bonnie_pos[1], ICONA_LARGHEZZA, ICONA_ALTEZZA)
dux_rect = pygame.Rect(dux_pos[0], dux_pos[1], ICONA_LARGHEZZA, ICONA_ALTEZZA)
tate_rect = pygame.Rect(tate_pos[0], tate_pos[1], ICONA_LARGHEZZA, ICONA_ALTEZZA)

# Variabile per tenere traccia del personaggio selezionato
scelto= False
istart= False
scelta= None
aspetta=0

# loop scelta personaggio
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            scelto= True
            mouse_x, mouse_y = event.pos
            if diddy_rect.collidepoint(mouse_x, mouse_y):
                scelta = "DIDDY"
            elif bonnie_rect.collidepoint(mouse_x, mouse_y):
                scelta = "BONNIE"
            elif dux_rect.collidepoint(mouse_x, mouse_y):
                scelta = "DUX"
            elif tate_rect.collidepoint(mouse_x, mouse_y):
                scelta = "TATE"
            
            elif play_button_rect.collidepoint(mouse_x, mouse_y):
               istart= True

    # Disegna lo sfondo
    schermo.blit(sfondo_img, (0, 0))

        
    # Se c'è una scelta, mostra cornice e stand
    if scelta == "DIDDY":
        schermo.blit(cornice_img, posizione_cornice_diddy)
        schermo.blit(diddy_stand, (50, 400))
        schermo.blit(diddy_name, (550, 450))
        # mostra statistiche
        statistiche= [3, 3, 2, 5, 3]

    elif scelta == "BONNIE":
        schermo.blit(cornice_img, posizione_cornice_bonnie)
        schermo.blit(bonnie_stand, (10, 400))
        schermo.blit(bonnie_name, (550, 450))
        # mostra statistiche
        statistiche= [2, 3, 4, 2, 5]
        
    elif scelta == "DUX":
        schermo.blit(cornice_img, posizione_cornice_dux)
        schermo.blit(dux_stand, (0, 400))
        schermo.blit(duce_name, (550, 450))
        # mostra statistiche
        statistiche= [5, 4, 2, 3, 2]
        
    elif scelta == "TATE":
        schermo.blit(cornice_img, posizione_cornice_tate)
        schermo.blit(tate_stand, (10, 400))
        schermo.blit(tate_name, (550, 450))
        # mostra statistiche
        statistiche= [4, 5, 2, 2, 3]
        
    #mostra statistiche
    if scelto:
        schermo.blit(stats_img, (480, 450))
        schermo.blit(play_button_img, (play_button_pos[0], play_button_pos[1]))
        schermo.blit(light_img, (play_button_pos[0], play_button_pos[1]))
        for i in range(statistiche[0]):
            schermo.blit(_5_stelle_img, (800 + i * distanza_stelle, 520))
        for i in range(statistiche[1]):
            schermo.blit(_5_stelle_img, (880 + i * distanza_stelle, 580))
        for i in range(statistiche[2]):
            schermo.blit(_5_stelle_img, (800 + i * distanza_stelle, 640))
        for i in range(statistiche[3]):
            schermo.blit(_5_stelle_img, (760 + i * distanza_stelle, 700))
        for i in range(statistiche[4]):
            schermo.blit(_5_stelle_img, (850 + i * distanza_stelle, 760))

    if istart:
        # ===== SETUP DEL GIOCO =====

        if scelta == "DIDDY":
            good_drop = resource_path("racist_game/diddy_good_drop1.png")
            bad_drop = resource_path("racist_game/diddy_bad_drop1.png")
            player_name = "diddy_player"
            points="BABY OIL"
        elif scelta == "BONNIE":
            good_drop = resource_path("racist_game/bonnie_good_drop1.png")
            bad_drop = resource_path("racist_game/bonnie_bad_drop1.png")
            player_name = "bonnie_player"
            points="BODY COUNT"
        elif scelta == "DUX":
            bad_drop = resource_path("racist_game/dux_bad_drop1.png")
            good_drop = resource_path("racist_game/dux_good_drop1.png")
            player_name = "dux_player"
            points="CAMERATI"
        elif scelta == "TATE":
            good_drop = resource_path("racist_game/tate_good_drop1.png")
            bad_drop = resource_path("racist_game/tate_bad_drop1.png")
            player_name = "tate_player"
            points="BITCHES"

        # Carica il player
        player_img = pygame.image.load(resource_path(f"racist_game/{player_name}.png")).convert_alpha()
        player_img = pygame.transform.scale(player_img, (150, 150))

        # Posizione iniziale del player
        player_x = width // 2 - 125  # Centrato
        player_y = 660
        player_rect = pygame.Rect(player_x, player_y, 50, 40)

        # Player velocity
        player_velocity = 8
        player_point = 0
        player_life = 3

        # vita immagini
        heart_img = pygame.image.load(resource_path("racist_game/heart.png")).convert_alpha()
        heart_img = pygame.transform.scale(heart_img, (110, 110))

        empty_heart_img = pygame.image.load(resource_path("racist_game/empty_heart.png")).convert_alpha()
        empty_heart_img = pygame.transform.scale(empty_heart_img, (110, 110))

        # carica immagini esplosione
        explosion_frames = [
            pygame.transform.scale(pygame.image.load(resource_path("racist_game/bubble_explo1.png")).convert_alpha(), (150, 150)),
            pygame.transform.scale(pygame.image.load(resource_path("racist_game/bubble_explo2.png")).convert_alpha(), (150, 150)),
            pygame.transform.scale(pygame.image.load(resource_path("racist_game/bubble_explo3.png")).convert_alpha(), (150, 150)),
            pygame.transform.scale(pygame.image.load(resource_path("racist_game/bubble_explo4.png")).convert_alpha(), (150, 150)),
            pygame.transform.scale(pygame.image.load(resource_path("racist_game/bubble_explo5.png")).convert_alpha(), (150, 150)),
            pygame.transform.scale(pygame.image.load(resource_path("racist_game/bubble_explo6.png")).convert_alpha(), (150, 150)),
            pygame.transform.scale(pygame.image.load(resource_path("racist_game/bubble_explo7.png")).convert_alpha(), (150, 150)),
            pygame.transform.scale(pygame.image.load(resource_path("racist_game/bubble_explo8.png")).convert_alpha(), (150, 150)),
            pygame.transform.scale(pygame.image.load(resource_path("racist_game/bubble_explo9.png")).convert_alpha(), (150, 150)),
            pygame.transform.scale(pygame.image.load(resource_path("racist_game/bubble_explo10.png")).convert_alpha(), (150, 150))
        ]
        explotion= False
        a= 0
        
        # Carica i drop
        size_drop = (100, 100)
        g_drop_img = pygame.image.load(good_drop).convert_alpha()
        g_drop_img = pygame.transform.scale(g_drop_img, size_drop)
        g_drop_probability = 40

        b_drop_img = pygame.image.load(bad_drop).convert_alpha()
        b_drop_img = pygame.transform.scale(b_drop_img, size_drop)
        b_drop_probability = 60

        l_drop_velocity= 2
        f_drop_velocity= 12
        # Lista per i drop
        drops = []

        class Drop:
            def __init__(self, x, y, speed, marker):
                self.x = x
                self.y = y
                self.speed = speed
                self.marker = marker
                self.rect = pygame.Rect(x, y, size_drop[0], size_drop[1])
            
            def update(self):
                self.y += self.speed
                self.rect.y = self.y
            
            def draw(self, screen):
                if self.marker == 'good':
                    screen.blit(g_drop_img, (self.x, self.y))
                elif self.marker == 'bad':
                    screen.blit(b_drop_img, (self.x, self.y))  
            
            def is_off_screen(self):
                return self.y > height

        def spawn_drop():
            x = random.randint(0, width - size_drop[0])
            y = 30 # Inizia sopra lo schermo
            speed = random.randint(l_drop_velocity, f_drop_velocity)  
            marker = random.choices(['good', 'bad'], weights=[g_drop_probability,b_drop_probability], k=1)[0]  # Aggiungi un marker per il drop
            new_drop = Drop(x, y, speed, marker)
            drops.append(new_drop)

        def update_drops():
            for drop in drops[:]:
                drop.update()
                if drop.y > 730:
                    drops.remove(drop)

        def draw_drops():
            for drop in drops:
                drop.draw(schermo)

        # Timer per spawn automatico
        SPAWN_DROP = pygame.USEREVENT + 1
        pygame.time.set_timer(SPAWN_DROP, 2000)

        VELOCITY_ENCREASE = pygame.USEREVENT 
        pygame.time.set_timer(VELOCITY_ENCREASE, 10000)  # Aument

        n_drop= 1

        # ===== LOOP DEL GIOCO =====
        # Carica il video
        cap = cv2.VideoCapture(resource_path('racist_game/drop_game_sfondo.mp4'))
        clock = pygame.time.Clock()
        running1 = True

        while running1:
            # Leggi frame del video
            ret, frame = cap.read()
            
            if not ret:
                # Riavvia il video quando finisce
                cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                continue
            
            # Converti da BGR a RGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            # Ruota il frame (3 rotazioni = 270 gradi)
            frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
            frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
            frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
            
            # Converti in superficie pygame
            frame_surface = pygame.surfarray.make_surface(frame)
            frame_surface = pygame.transform.scale(frame_surface, size)
            
            # Disegna il frame come sfondo
            schermo.blit(frame_surface, (0, 0))
            
            # Gestione eventi
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running1 = False
                    running = False
                elif event.type == SPAWN_DROP:
                    for _ in range(n_drop):  # Spawna due drop ogni secondo
                        spawn_drop()
                elif event.type == VELOCITY_ENCREASE:
                    player_velocity +=0.5
                    if n_drop < 10 :  # Limita il numero di drop a spawnare
                        n_drop += 1  # Aumenta il numero di drop da spawnare
                        f_drop_velocity += 1
                    else:
                        if g_drop_probability > 20:
                            g_drop_probability -= 10
                            b_drop_probability += 10
            
            if player_life <= 0:# controlla se il player ha perso tutte le vit
                aspetta+=1
                if aspetta >= 10:  # Aspetta 60 frame (1 secondo)
                    sali = 0
                    running1 = False
                    istart = False  # Torna alla schermata di selezione
                    running2 = True
                    back_button_rect = pygame.Rect(1100, 600, 300, 100)
                    quit_button_rect = pygame.Rect(100, 600, 300, 100)

                    # Variabili per l'animazione del testo "GAME OVER"
                    game_over_text = "GAME OVER"
                    game_over_chars_shown = 0
                    game_over_timer = 0
                    game_over_delay = 10  # frames tra ogni lettera

                    # Font più grande per GAME OVER
                    font_large = pygame.font.Font(resource_path("racist_game/street_of_r.ttf"), 65)

                    # Variabili per mostrare i pulsanti dopo che il punteggio è completo
                    show_buttons = False
                    
                    while running2:
                        # Animazione del punteggio
                        if sali < player_point:
                            sali += 0.1
                        if sali > player_point:
                            sali = player_point
                        else:
                            show_buttons = True  # Mostra i pulsanti quando il punteggio è completo
        
                        # Animazione del testo GAME OVER
                        game_over_timer += 1
                        if game_over_timer >= game_over_delay and game_over_chars_shown < len(game_over_text):
                            game_over_chars_shown += 1
                            game_over_timer = 0
        
                        # Testo del punteggio (nero, centrato spostato a sinistra)
                        text_punteggio = font.render(f"SCORE: {int(sali)}", True, (0, 0, 0))
        
                        # Testo GAME OVER (lettere che appaiono una alla volta)
                        game_over_display = game_over_text[:game_over_chars_shown]
                        text_game_over = font_large.render(game_over_display, True, (250, 0, 0))
        
                        # Testi per i pulsanti (solo se show_buttons è True)
                        if show_buttons:
                            text_quit = font.render("QUIT", True, (0, 0, 0))
                            text_play_again = font.render("BACK", True, (0, 0, 0))
        
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                running2 = False
                                running = False
                            elif event.type == pygame.MOUSEBUTTONDOWN and show_buttons:
                                mouse_x, mouse_y = event.pos
                                if back_button_rect.collidepoint(mouse_x, mouse_y):  # PLAY AGAIN
                                    running2 = False
                                elif quit_button_rect.collidepoint(mouse_x, mouse_y):  # QUIT
                                    running2 = False
                                    running = False
        
                        # Disegna tutto
                        schermo.blit(schermata_finale_img, (0, 0))
        
                        # GAME OVER centrato in alto
                        game_over_x = width // 2 - text_game_over.get_width() // 2+50
                        schermo.blit(text_game_over, (game_over_x,500))
        
                        # Score centrato spostato a sinistra
                        score_x = width // 2 - 150  # Spostato a sinistra
                        score_y = height // 2 - 50
                        schermo.blit(text_punteggio, (score_x, score_y))
        
                        # Pulsanti (solo se visibili)
                        if show_buttons:
                            # Pulsante QUIT
                            pygame.draw.rect(schermo, (200, 200, 200), quit_button_rect)
                            quit_text_x = quit_button_rect.x + quit_button_rect.width // 2 - text_quit.get_width() // 2
                            quit_text_y = quit_button_rect.y + quit_button_rect.height // 2 - text_quit.get_height() // 2
                            schermo.blit(text_quit, (quit_text_x, quit_text_y))
                            
                            # Pulsante PLAY AGAIN
                            pygame.draw.rect(schermo, (200, 200, 200), back_button_rect)
                            play_again_x = back_button_rect.x + back_button_rect.width // 2 - text_play_again.get_width() // 2 -30
                            play_again_y = back_button_rect.y + back_button_rect.height // 2 - text_play_again.get_height() // 2
                            schermo.blit(text_play_again, (play_again_x, play_again_y))
        
                        pygame.display.flip()
                        tempo.tick(60)

            #mostra le esplosioni            
            if explotion== True:
                if a==10:
                    explotion = False  
                    a= 0 
                else :
                    schermo.blit(explosion_frames[a], (player_x - 40, player_y))
                    a+=1

            # Controlla spostamenti player
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and player_x > 0:
                player_x -= player_velocity
            elif keys[pygame.K_RIGHT] and player_x < width-90:
                player_x += player_velocity

            # Aggiorna la posizione del player rectangle
            player_rect.x = player_x

            # Controlla se il player ha preso un drop
            for drop in drops[:]:
                if player_rect.colliderect(drop.rect):
                    drops.remove(drop)
                    if drop.marker == 'good':
                        player_point += 1
                    elif drop.marker == 'bad':
                        player_life -= 1
                        explotion= True

            # Aggiorna e disegna i drop
            update_drops()
            draw_drops()

            # Disegna il player
            schermo.blit(player_img, (player_x-40, player_y))

            text = font.render(f" {points}: {player_point}", True, (255, 255, 255))
            schermo.blit(text, (10, 30))

            # Mostra vite
            for i in range(player_life):
                schermo.blit(heart_img, (1200 - i * 100, 0))
            if player_life < 3:
                for i in range(3 - player_life):
                    schermo.blit(empty_heart_img, (1200 - (i + player_life) * 100, 0))

            pygame.display.flip()
            clock.tick(30)

        cap.release()

    

    pygame.display.flip()
    tempo.tick(60)

pygame.quit()