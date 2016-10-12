paragraph = 'A suspicious item found in Manchester Uniteds Old Trafford stadium ahead of a key soccer game was actually a training device, police said on Sunday.The discovery of the "incredibly lifelike explosive device" Sunday prompted the evacuation of Uniteds game against AFC Bournemouth, which was then canceled. "Following todays controlled explosion, we have since found out that the item was a training device which had accidentally been left by a private company following a training exercise involving explosive search dogs," Assistant Chief Constable John OHare of the Greater Manchester Police said in a statement. "Whilst this item did not turn out to be a viable explosive, on appearance this device was as real as could be, and the decision to evacuate the stadium was the right thing to do, until we could be sure that people were not at risk." Explosive material accidentally left on school bus after training exercise The match was rescheduled for Tuesday at 8 p.m. local time (3 p.m. ET), the Premier League said. Manchester Uniteds Old Trafford stadium evacuated 5 photos: Security fears prompt abandonment "We would like to thank Manchester Uniteds staff, the police and other emergency services for all their efforts today as well as rearranging the match for this coming Tuesday," the Premier League said in a statement. "Both Manchester United and AFC Bournemouths management has been extremely helpful." Man Utd bus attacked before West Ham game Sniffer dogs United was due to to face off against Bournemouth in the final game of the English Premier League season on Sunday. The game could have qualified United for next seasons Champions League -- European soccers biggest competition -- if they had won and their local rivals Manchester City lost at Swansea. Shortly before the 3 p.m. kickoff, Manchester United staff alerted police to a suspicious item found in the toilets within the North West Quadrant, between the Sir Alex Ferguson stand and the Stretford End. Initially, a partial evacuation of the stadium was put in place while sniffer dogs searched the stands of the 75,000-capacity stadium. A sniffer dog patrols the Old Trafford stands. A sniffer dog patrols the Old Trafford stands. After the initial sweep a decision was made between police and Manchester United officials to abandon the game and a full controlled evacuation of the stadium was carried out. "We dont make these decisions lightly and we have done this today to ensure the safety of all those attending," OHare of Greater Manchester Police said. Bomb disposal experts carried out a controlled explosion of the device and determined it was not "viable." "Everyone remained calm, followed instructions, and worked with officers and stewards to ensure that a safe evacuation was quickly completed," OHare said. "Those present today were a credit to the football family and their actions should be recognized." Earlier in the day, fans praised United and emergency services for their handling of the situation.'

import time

# your code to measure the time goes here
def task():
    #vowels = set(['a', 'e', 'i', 'o', 'u']) #### set
    #vowels = ['a', 'e', 'i', 'o', 'u'] #### list
    vowels = 'aeiou'  #### string
    
    count = 0
    
    for chr in paragraph:
        if chr in vowels:
            count += 1
            
    print("there are %d vowels in the paragraph" %(count))

#processing start

total_time = 0

for i in range(10):
    start_time = time.time()
    task()
    #processing end
    end_time = time.time()
    #print processing time
    total_time += end_time - start_time
print total_time/10