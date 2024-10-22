#program gamify.py
#developer Abanoub Bashara
#UtorID: basharaa
#Due date: 9/10/2023



def initialize():

    global cur_hedons, cur_health
    global cur_time, last_star_time, last_star_time2
    global last_activity, last_activity_duration
    global cur_star_activity, cur_star
    global bored_with_stars
    global last_finished
    global effective_minutes_left_health
    global effective_minutes_left_hedons
    global x

    x = None
    cur_hedons = 0
    cur_health = 0
    cur_time = 0
    last_star_time = None
    last_star_time2 = None
    cur_star_activity = None
    cur_star = None
    bored_with_stars = False
    last_activity = None
    last_activity_duration = 0
    last_finished = -1000


initialize()
def get_cur_health():
    return cur_health

def get_cur_hedons():
    return cur_hedons



def is_tired():
    if cur_time - last_finished <= 120:
        return True
    else:
        return False

def star_can_be_taken(activity):
    if cur_star == True and cur_star_activity == activity and cur_time == last_star_time and bored_with_stars == False:
        return True
    else:
        return False



def offer_star(activity):
    global cur_star, cur_star_activity
    global cur_time, last_star_time, last_star_time2
    global bored_with_stars

    cur_star = True
    cur_star_activity = activity


    if last_star_time2 == None:
        bored_with_stars = False
    else:
        time_between_stars = cur_time - last_star_time2
        if time_between_stars <= 120:
            bored_with_stars = True
        else:
            bored_with_stars = False




    last_star_time2, last_star_time = last_star_time, cur_time



def perform_activity(activity, duration):
    global cur_hedons, cur_health
    global cur_time, last_star_time, last_star_time2
    global last_activity, last_activity_duration
    global cur_star_activity, cur_star
    global bored_with_stars
    global last_finished
    global effective_minutes_left_health
    global effective_minutes_left_hedons
    global x



    if activity == "running":

        #Update health pts
        if last_finished == cur_time and last_activity ==  activity: #stopped and started running rt away
            get_effective_minutes_left_health(activity)
            if x > 0:
                if duration <= x: #duration is less than effective time
                    cur_health = cur_health + (duration * 3)
                else:
                    cur_health = cur_health + (x * 3) + (duration - x) * 1
            else:
                 cur_health = cur_health + (duration * 1)

        else:
            if duration <= 180:
                cur_health = cur_health + (3 * duration)
            else:
                cur_health = cur_health + 540 + (duration - 180)

        #Update hedons
        if is_tired() is True: #If user is tired
            if star_can_be_taken("running") == False: #If star not used
                cur_hedons = cur_hedons + (-2 * duration)
            else: #if star is used
                if duration <= 10: #if running for less than 10 min
                    cur_hedons = cur_hedons + (-2 * duration) + (3 * duration)
                else: #if running for more than 10 min
                      cur_hedons  = cur_hedons + (-2 * duration) + 30

        else: #if user is not tired
            if star_can_be_taken("running") == False: #If star not used
                if duration <= 10:
                   cur_hedons = cur_hedons + (2 * duration)
                else:
                    cur_hedons = cur_hedons + 20 + (-2 * (duration-10))



            else: #if star is used
                if duration <= 10:
                   cur_hedons = cur_hedons + (2 * duration) + (3 * duration)
                else:
                    cur_hedons = cur_hedons + 30 + 20 + (-2 * (duration-10))



    #TEXTBOOKS
    if activity == "textbooks":

        #update health pts
        cur_health = cur_health + (2 * duration)


        #Update hedons
        if is_tired() is True: #If user is tired
            if star_can_be_taken("textbooks") == False: #If star not used
                cur_hedons = cur_hedons + (-2 * duration)
            else: #if star is used
                if duration <= 10: #if textbooks for less than 10 min
                    cur_hedons = cur_hedons + (-2 * duration) + (3 * duration)
                else: #if running for more than 10 min
                      cur_hedons  = cur_hedons + (-2 * duration) + 30



        else: #if user is not tired


            if star_can_be_taken("textbooks") == False: #If star not used
                if duration < 20:
                   cur_hedons = cur_hedons + (1 * duration)
                else:
                    cur_hedons = cur_hedons + 20 + ((duration - 20) * -1)


            else: #if star is used
                if duration < 20: #if duration is less than 20 min
                    if duration <= 10:
                        cur_hedons = cur_hedons + (1 * duration) + (3 * duration)
                    else:
                        cur_hedons = cur_hedons + ((duration - 30) * -1) + 30


                else: #if duration is more than 20 min
                    if duration <= 10:
                        cur_hedons = cur_hedons + 20 + ((duration - 20) * -1) + (3 * duration)
                    else:
                        cur_hedons = cur_hedons + 20 + ((duration - 20) * -1) + 30



    if activity == "resting":
        x = 180
    else:
        last_finished = cur_time + duration #updates time of last activity


    cur_time = cur_time + duration
    last_activity_duration = duration
    last_activity = activity



def get_effective_minutes_left_health(activity):
    global x
    if last_activity == activity and activity == "running":
        if x == None:
            x = 180 - last_activity_duration
        else:
            x =  x - last_activity_duration


##########


def most_fun_activity_minute():

   #CALCULATE POSSIBLE HEDONS FOR RUNNING

    if is_tired() is True: #If user is tired
        if star_can_be_taken("running") == False: #If star not used
            run_for_min_hedons = -2

        else: #if star is used

            run_for_min_hedons = -2 + 3


    else: #if user is not tired
        if star_can_be_taken("running") == False: #If star not used
            run_for_min_hedons =  2

        else: #if star is used
            run_for_min_hedons = 2 + 3



 #CALCULATE POSSIBLE HEDONS FOR TEXTBOOKS

    if is_tired() is True: #If user is tired
        if star_can_be_taken("textbooks") == False: #If star not used
            text_for_min_hedons =  -2
        else: #if star is used

            text_for_min_hedons = -2 + 3


    else: #if user is not tired
        if star_can_be_taken("textbooks") == False: #If star not used
            text_for_min_hedons = 1

        else: #if star is used

            text_for_min_hedons = 1 + 3

 #CALCULATE POSSIBLE HEDONS FOR RESTING
    rest_hedons = 0



    L = [run_for_min_hedons, text_for_min_hedons, rest_hedons]

    if max(L) == run_for_min_hedons:
        return "running"
    elif max(L) == text_for_min_hedons:
        return "textbooks"
    else:
        return "resting"



if __name__ == '__main__':

    perform_activity("running", 30)
    print(get_cur_hedons())            # -20 = 10 * 2 + 20 * (-2)             # Test 1
    print(get_cur_health())            # 90 = 30 * 3                          # Test 2
    print(most_fun_activity_minute())  # resting                              # Test 3
    perform_activity("resting", 30)
    offer_star("running") #star time = 60
    print(most_fun_activity_minute())  # running                              # Test 4
    perform_activity("textbooks", 30)
    print(get_cur_health())            # 150 = 90 + 30*2                       # Test 5
    print(get_cur_hedons())            # -80 = -20 + 30 * (-2)                # Test 6
    offer_star("running") #star time = 90
    perform_activity("running", 20)
    print(get_cur_health())            # 210 = 150 + 20 * 3                   # Test 7
    print(get_cur_hedons())            # -90 = -80 + 10 * (3-2) + 10 * (-2)   # Test 8
    perform_activity("running", 170)
    print(get_cur_health())            # 700 = 210 + 160 * 3 + 10 * 1         # Test 9
    print(get_cur_hedons())            # -430 = -90 + 170 * (-2)              # Test 10




















