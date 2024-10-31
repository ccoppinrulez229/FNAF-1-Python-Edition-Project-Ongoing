import math
import random
class Animatronic:
    def __init__(self,ai,name):
        self.ai=ai
        self.name=name
        self.max_wait_timer=0 #will be randomized later when night starts based on the type of animatronic
        self.position=0 #will be initialized based on where animatronic is on the map (for example, freddy chica and bonnie will start at the same position, while foxy is at a different position since he's in pirate's cove)
        self.wait_to_move_timer=0
        self.map_icon=""
        self.max_door_wait_timer = 0
        self.wait_at_door_timer = self.max_door_wait_timer

    def set_max_door_wait_timer(self):
        self.max_door_wait_timer = 23 % self.ai if self.ai != 0 else 0
        self.wait_at_door_timer=self.max_door_wait_timer

    def randomize_max_wait_timer(self): #when night starts, the wait timer for specific animatronic object will be set to a random number. throughout the night, this timer will count down after each user input, eventually reaching 0, giving them the chance to move.
        if self.name=="Freddy":
            self.max_wait_timer=random.randint(3,6)
        elif self.name=="Bonnie":
            self.max_wait_timer=random.randint(3,5)
        elif self.name=="Chica":
            self.max_wait_timer=random.randint(4,8)
        elif self.name=="Foxy":
            self.max_wait_timer=random.randint(5,10)

        self.wait_to_move_timer = self.max_wait_timer


    def reduce_current_countdown(self): #countdown to change animatronic position.
        if self.ai!=0 and self.wait_at_door_timer==self.max_door_wait_timer:
            if self.wait_to_move_timer!=0:
                self.wait_to_move_timer-=1

    def reduce_current_door_countdown(self): #countdown decreases for each animatronic as long as they are in front of the doors
        if self.ai!=0:
            if (self.name == "Freddy" and self.position == 5) or (self.name == "Bonnie" and self.position == 6) or (self.name == "Chica" and self.position == 6):
                if self.wait_at_door_timer!=-1:
                    self.wait_at_door_timer-=1

    def check_to_kill_player(self): #if an animatronic has been at the door and their wait timer has run out, return which animatronic it was. Used in conjuction with the doors to check whether or not to jumpscare the player
        if self.ai!=0:
            if (self.name=="Freddy" and self.position==5 and self.wait_at_door_timer==-1):
                return "Freddy"
            elif (self.name == "Bonnie" and self.position == 6 and self.wait_at_door_timer==-1):
                return "Bonnie"
            elif (self.name == "Chica" and self.position == 6 and self.wait_at_door_timer==-1):
                return "Chica"

    def change_position_fred_chic_bon(self): #has a chance to change current position for freddy, chica and bonnie when their timers wait to move timers reach 0, as long as they havent reached their final positions (which is in front of the doors)
        if self.ai!=0:
            if (self.name=="Freddy" and self.position!=5) or (self.name=="Bonnie" and self.position!=6) or (self.name=="Chica" and self.position!=6):
                if self.wait_to_move_timer==0:
                    chance_to_move=random.randint(self.ai,25)
                    if chance_to_move>=20:
                        self.position+=1
                    self.wait_to_move_timer = self.max_wait_timer

    def change_position_foxy(self): #foxy works a bit differently, thus will have a different function
        if self.ai!=0:
            if self.name=="Foxy":
                pass
    def set_map_icon(self): #
        if self.name == "Freddy":
            self.map_icon="🐻"
        elif self.name == "Bonnie":
            self.map_icon="🐰"
        elif self.name == "Chica":
            self.map_icon="🐔"
        elif self.name == "Foxy":
            self.map_icon="🦊"

def print_office(left_door_closed,right_door_closed):
    if left_door_closed==0 and right_door_closed==0:
        print('''
            \n                    ┃╲               ⊚⊚               ╱┃
                    ┃  ╲           ⊚    ⊚           ╱  ┃
                    ┃    ╲           ⊚⊚           ╱    ┃
                    ┃     ┃                       ┃     ┃
                    ┃     ┃   ▧▧        ⧉ ⧉     ┃     ┃
                 🟥 ┃     ┃   ▧▧       ⧉ ⧉      ┃     ┃ 🟥
                 ⬜ ┃     ┃                  ㋡   ┃     ┃ ⬜
                    ┃     ┃┋☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶┋┃     ┃
                    ┃     ┃┋☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶┋┃     ┃
                    ┃     ┃┋                     ┋┃     ┃
                    ┃     ┃┇                     ┋┃     ┃''')
    elif left_door_closed==1 and right_door_closed==0:
        print('''
            \n                    ┃╲               ⊚⊚               ╱┃
                    ┃✕✕╲           ⊚    ⊚           ╱  ┃
                    ┃✕✕✕✕╲           ⊚⊚           ╱    ┃
                    ┃✕✕✕✕✕┃                       ┃     ┃
                    ┃✕✕✕✕✕┃   ▧▧        ⧉ ⧉     ┃     ┃
                 🟥 ┃✕✕✕✕✕┃   ▧▧       ⧉ ⧉      ┃     ┃ 🟥
                 ⬜ ┃✕✕✕✕✕┃                  ㋡   ┃     ┃ ⬜
                    ┃✕✕✕✕✕┃┋☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶┋┃     ┃
                    ┃✕✕✕✕✕┃┋☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶┋┃     ┃
                    ┃✕✕✕✕✕┃┋                     ┋┃     ┃
                    ┃✕✕✕✕✕┃┇                     ┋┃     ┃''')
    elif left_door_closed == 0 and right_door_closed == 1:
        print('''
            \n                    ┃╲               ⊚⊚               ╱┃
                    ┃  ╲           ⊚    ⊚           ╱✕✕┃
                    ┃    ╲           ⊚⊚           ╱✕✕✕✕┃
                    ┃     ┃                       ┃✕✕✕✕✕┃
                    ┃     ┃   ▧▧        ⧉ ⧉     ┃✕✕✕✕✕┃
                 🟥 ┃     ┃   ▧▧       ⧉ ⧉      ┃✕✕✕✕✕┃ 🟥
                 ⬜ ┃     ┃                  ㋡   ┃✕✕✕✕✕┃ ⬜
                    ┃     ┃┋☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶┋┃✕✕✕✕✕┃
                    ┃     ┃┋☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶┋┃✕✕✕✕✕┃
                    ┃     ┃┋                     ┋┃✕✕✕✕✕┃
                    ┃     ┃┇                     ┋┃✕✕✕✕✕┃''')
    elif left_door_closed==1 and right_door_closed==1:
        print('''
            \n                    ┃╲               ⊚⊚               ╱┃
                    ┃✕✕╲           ⊚    ⊚           ╱✕✕┃
                    ┃✕✕✕✕╲           ⊚⊚           ╱✕✕✕✕┃
                    ┃✕✕✕✕✕┃                       ┃✕✕✕✕✕┃
                    ┃✕✕✕✕✕┃   ▧▧        ⧉ ⧉     ┃✕✕✕✕✕┃
                 🟥 ┃✕✕✕✕✕┃   ▧▧       ⧉ ⧉      ┃✕✕✕✕✕┃ 🟥
                 ⬜ ┃✕✕✕✕✕┃                  ㋡   ┃✕✕✕✕✕┃ ⬜
                    ┃✕✕✕✕✕┃┋☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶┋┃✕✕✕✕✕┃
                    ┃✕✕✕✕✕┃┋☶☶☶☶☶☶☶☶☶☶☶☶☶☶☶┋┃✕✕✕✕✕┃
                    ┃✕✕✕✕✕┃┋                     ┋┃✕✕✕✕✕┃
                    ┃✕✕✕✕✕┃┇                     ┋┃✕✕✕✕✕┃''')

def check_time_progress(time_progress,time): #checks to see whether or not to change the hour. hours change every 20 inputs by user
    if time_progress%20==0 and time_progress!=0:
        time +=1
    return time
def check_camera(current_cam,cam_map,animatronic_list,time_progress): #checks which animatronics are in a camera
    chars_in_room=""
    cam_map = '''
                                     ━━━━━━━━━━━━
                                    ┃     1A     ┃      
                    ━━━━   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                    ┃  ┃━━┃   1B                            ┃  ━━━
                    ┃  ┃━━┃                                 ┃━━┃7┃ 
                    ┃5 ┃  ┃                                 ┃━━┃ ┃
                    ━━━━  ┃                                 ┃  ┃ ┃
                      ━━━━┃                                 ┃  ┃ ┃━━┃
                     ┃1C  ┃                                 ┃  ┃ ┃━━┃
                      ━━━━┃                                 ┃  ┃ ┃
                           ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   ━━━   
                                   ┃ ┃            ┃ ┃    ┃ ┃
                                 ━━━━━━          ━━━━━━  ━━━━━━━━━
                         ━━━━━━  ┃    ┃          ┃    ┃  ┃     6 ┃
                         ┃    ┃━━┃    ┃          ┃    ┃  ┃       ┃
                         ┃3   ┃━━┃2A  ┃          ┃  4A┃  ━━━━━━━━━
                         ━━━━━━  ┃    ┃  ━━━━━━  ┃    ┃
                                 ┃    ┃━━┃    ┃━━┃    ┃
                                 ┃2B  ┃━━┃ ▀▀ ┃━━┃  4B┃
                                 ━━━━━━  ━━━━━━  ━━━━━━''' #cam map is reset each time to potentially scan for animatronics in a specific cam
    if current_cam=="":
        return cam_map

    for animatronic in animatronic_list:
        if (current_cam=="1A" and animatronic.position==0) and (animatronic.name=="Freddy" or animatronic.name=="Bonnie" or animatronic.name=="Chica"):
            chars_in_room+=f"{animatronic.map_icon}"

        if (current_cam=="1B" and animatronic.position==1) and (animatronic.name=="Bonnie" or animatronic.name=="Chica"):
            chars_in_room+=f"{animatronic.map_icon}"

        if (current_cam=="5" and animatronic.position==2) and animatronic.name=="Bonnie":
            chars_in_room+=f"{animatronic.map_icon}"

        if (current_cam == "2A" and animatronic.position == 3) and animatronic.name == "Bonnie":
            chars_in_room += f"{animatronic.map_icon}"

        if (current_cam == "3" and animatronic.position == 4) and animatronic.name == "Bonnie":
            chars_in_room += f"{animatronic.map_icon}"

        if (current_cam == "2B" and animatronic.position == 5) and animatronic.name == "Bonnie":
            chars_in_room += f"{animatronic.map_icon}"

        if (current_cam=="7" and animatronic.position==2) and animatronic.name=="Chica":
            chars_in_room+=f"{animatronic.map_icon}"

        if (current_cam=="6" and animatronic.position==3) and animatronic.name=="Chica":
            chars_in_room+=f"{animatronic.map_icon}"

        if (current_cam=="4A" and animatronic.position==4) and animatronic.name=="Chica":
            chars_in_room+=f"{animatronic.map_icon}"

        if (current_cam=="4B" and animatronic.position==5) and animatronic.name=="Chica":
            chars_in_room+=f"{animatronic.map_icon}"

        #STILL NEED TO DO FOXY AND FREDDY

    new_map=cam_map.replace(current_cam,chars_in_room) #replaces camera string with animatronic icons
    #print(chars_in_room)
    return new_map

def jumpscare(animatronic):
    if animatronic=="Freddy":
        print("Freddy got you! Game over.")
    elif animatronic=="Bonnie":
        print("Bonnie got you! Game over.")
    elif animatronic=="Chica":
        print("Chica got you! Game over.")
    elif animatronic=="Foxy":
        print("Foxy got you! Game over.")
def cameras(animatronic_list, power,cam,time,usage,left_door_closed,right_door_closed,tips_visible,cam_map,current_cam,time_progress):

    while cam==1:
        jumpscared = 0
        for animatronic in animatronic_list: #each time this loops, animatronic countdown decreases by 1, eventually leading to a chance for them to move
            animatronic.reduce_current_countdown()
            animatronic.reduce_current_door_countdown()
            animatronic.change_position_fred_chic_bon()
            animatronic.change_position_foxy()

            if animatronic.check_to_kill_player()=="Bonnie" and left_door_closed==0:
                jumpscare("Bonnie") #bonnie jumpscare
                jumpscared=1
            elif animatronic.check_to_kill_player()=="Chica" and right_door_closed==0:
                jumpscare("Chica")
                jumpscared=1

        if jumpscared==1:
            break

        time_progress += 1 #each time this loops, time progress increases by 1
        time = check_time_progress(time_progress, time)
        print(f"Time progress: {time_progress}")

        print(("\n                                                    12" if time == 0 else "\n                                                    " +str(time)) + " AM\n                                             Custom Night")
        print(cam_map)
        print(f"Power left: {power}%\nUsage:{usage}")
        if tips_visible==1:
            print("\nOptions:\n1.)Close camera\n2.)Check cameras\n3.)Stall")
        option=int(input("\nChoose an option: "))
        if option==2:
            current_cam=str(input("Which camera would you like to check? Be sure to specify just the number, so for instance to look at CAM 4A, just type '4A': "))
            cam_map=check_camera(current_cam,cam_map,animatronic_list,time_progress)

        elif option==1:
            cam=0
            office(animatronic_list,time,power,cam,usage,left_door_closed,right_door_closed,tips_visible,cam_map,current_cam,time_progress)

        elif option==3:
            cam_map = check_camera(current_cam, cam_map, animatronic_list, time_progress)

        for animatronic in animatronic_list:
            print(f"{animatronic.name} current cooldown: {animatronic.wait_to_move_timer}")
            print(f"{animatronic.name} current position: {animatronic.position}\n")
            print(f"{animatronic.name} wait at door timer: {animatronic.wait_at_door_timer}\n")

def office(animatronic_list,time,power,cam,usage,left_door_closed,right_door_closed,tips_visible,cam_map,current_cam,time_progress): #main office gameplay...in text form!
    while cam==0:
        jumpscared = 0
        nothing = 0
        for animatronic in animatronic_list:  #each time this loops, animatronic countdown decreases by 1, eventually leading to a chance for them to move
            animatronic.reduce_current_countdown()
            animatronic.reduce_current_door_countdown()
            animatronic.change_position_fred_chic_bon()
            animatronic.change_position_foxy()
            print(f"{animatronic.name} current cooldown: {animatronic.wait_to_move_timer}")
            print(f"{animatronic.name} current position: {animatronic.position}\n")
            print(f"{animatronic.name} wait at door timer: {animatronic.wait_at_door_timer}\n")

            if animatronic.check_to_kill_player()=="Bonnie" and left_door_closed==0:
                jumpscare("Bonnie") #bonnie jumpscare
                jumpscared=1
            elif animatronic.check_to_kill_player()=="Chica" and right_door_closed==0:
                jumpscare("Chica")
                jumpscared=1

        if jumpscared==1:
            break


        time_progress += 1 #each time this loops, time progress increases by 1
        time = check_time_progress(time_progress, time)
        print(f"Time progress: {time_progress}")

        print(("\n                                                    12" if time == 0 else "\n                                                    " + str(time)) + " AM\n                                             Custom Night")
        print_office(left_door_closed,right_door_closed)
        print(f"Power left: {power}%\nUsage:{usage}")
        if tips_visible==1:
            print("\nOptions:\n1.)Check cameras\n2.)Open/Close left door\n3.)Check left door light\n4.)Open/Close right door\n5.)Check right door light\n6.)Stall\n7.)Hide tips")
        option=int(input("\nChoose an option: "))
        if option==1:
            cam=1
            cam_map = check_camera(current_cam, cam_map, animatronic_list, time_progress)
            cameras(animatronic_list,power,cam,time,usage,left_door_closed,right_door_closed,tips_visible,cam_map,current_cam,time_progress)
        if option==2:
            if left_door_closed==0:
                left_door_closed=1
            else:
                left_door_closed=0
        if option==3:
            if left_door_closed==0:
                for animatronic in animatronic_list:
                    if animatronic.name=="Bonnie" and animatronic.position==6:
                        print("\nYou checked the door and see a giant rabbit animatronic staring back at you with a blank expression.")

                    else:
                        nothing=1
            else:
                print("\nYou checked the door but came to the realization you can't see through a metal barrier.")
        if option==4:
            if right_door_closed==0:
                right_door_closed=1
            else:
                right_door_closed=0
        if option==5:
            if right_door_closed==0:
                for animatronic in animatronic_list:
                    if animatronic.name == "Chica" and animatronic.position == 6:
                        print("\nYou checked the door and see a giant chicken animatronic staring back at you with a blank expression.")
                    else:
                        nothing = 1
            else:
                print("\nYou checked the door but came to the realization you can't see through a metal barrier.")
        if option==6:
            pass
        if option==7:
            tips_visible=0

        if nothing == 1:
            print("\nYou checked the door. Nothing is there.")



def custom_night_menu():
    time = 0
    time_progress = -1 #continually increases through the night are more user actions are made. each hour changes by intervals of 20 (subject to change).
    power = 100
    cam = 0
    usage=0
    current_cam=""
    freddy=Animatronic(0,"Freddy")
    bonnie=Animatronic(0,"Bonnie")
    chica=Animatronic(0,"Chica")
    foxy=Animatronic(0,"Foxy")
    animatronic_list=[freddy,bonnie,chica,foxy]
    cam_map='''
                                     ━━━━━━━━━━━━
                                    ┃     1A     ┃      
                    ━━━━   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                    ┃  ┃━━┃   1B                            ┃  ━━━
                    ┃  ┃━━┃                                 ┃━━┃7┃ 
                    ┃5 ┃  ┃                                 ┃━━┃ ┃
                    ━━━━  ┃                                 ┃  ┃ ┃
                      ━━━━┃                                 ┃  ┃ ┃━━┃
                     ┃1C  ┃                                 ┃  ┃ ┃━━┃
                      ━━━━┃                                 ┃  ┃ ┃
                           ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   ━━━   
                                   ┃ ┃            ┃ ┃    ┃ ┃
                                 ━━━━━━          ━━━━━━  ━━━━━━━━━
                         ━━━━━━  ┃    ┃          ┃    ┃  ┃     6 ┃
                         ┃    ┃━━┃    ┃          ┃    ┃  ┃       ┃
                         ┃3   ┃━━┃2A  ┃          ┃  4A┃  ━━━━━━━━━
                         ━━━━━━  ┃    ┃  ━━━━━━  ┃    ┃
                                 ┃    ┃━━┃    ┃━━┃    ┃
                                 ┃2B  ┃━━┃ ▀▀ ┃━━┃  4B┃
                                 ━━━━━━  ━━━━━━  ━━━━━━'''
    print("Welcome to FNAF 1: Python Edition!\n----------------------------------")
    while True:
        print(f"\n             Custom Night:\nFreddy: {freddy.ai}  Bonnie: {bonnie.ai}  Chica: {chica.ai}  Foxy: {foxy.ai}")
        print("\n1.) Change Animatronic AI\n2.) Start Night\n3.) Exit Game")
        option=int(input("\nChoose an option: "))
        while option>3 or option<1:
            option=int(input("Invalid option. Try again!: "))
        if option==1: #change animatronic AI
            print("\nHow would you like to change animatronic AI?\n1.)Set all characters AI\n2.)Set specific character AI")
            option=int(input("\nChoose an option: "))
            while option > 2 or option < 1:
                option = int(input("Invalid option. Try again!: "))
            ai=int(input("\nInput an AI number from 0-20: "))
            if option==1:
                for animatronic in animatronic_list:
                    animatronic.ai = ai
            elif option==2:
                char=input("Type the name of the character starting with an uppercase to change their AI: ")
                for animatronic in animatronic_list:
                    if animatronic.name == char:
                        animatronic.ai = ai
        elif option==2: #start night
            for animatronic in animatronic_list: #for loop goes through each animatronic instance in the list
                animatronic.randomize_max_wait_timer() #specific animatronic wait timer is randomized
                animatronic.set_map_icon() #map icons are set for specific animatronic
                animatronic.set_max_door_wait_timer() #sets door wait timer based on animatronic
            office(animatronic_list,time,power,cam,usage,0,0,1,cam_map,"",time_progress)
        elif option==3:
            break


if __name__=="__main__":
    custom_night_menu()