

# Staging Interaction

In the original stage production of Peter Pan, Tinker Bell was represented by a darting light created by a small handheld mirror off-stage, reflecting a little circle of light from a powerful lamp. Tinkerbell communicates her presence through this light to the other characters. See more info [here](https://en.wikipedia.org/wiki/Tinker_Bell). 

There is no actor that plays Tinkerbell--her existence in the play comes from the interactions that the other characters have with her.

For lab this week, we draw on this and other inspirations from theatre to stage interactions with a device where the main mode of display/output for the interactive device you are designing is lighting. You will plot the interaction with a storyboard, and use your computer and a smartphone to experiment with what the interactions will look and feel like. 

_Make sure you read all the instructions and understand the whole of the laboratory activity before starting!_



## Prep

### To start the semester, you will need:
1. Set up your own Github "Lab Hub" repository to keep all you work in record by [following these instructions](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2021Fall/readings/Submitting%20Labs.md).
2. Set up the README.md for your Hub repository (for instance, so that it has your name and points to your own Lab 1) and [learn how to](https://guides.github.com/features/mastering-markdown/) organize and post links to your submissions on your README.md so we can find them easily.
3. (extra: Learn about what exactly Git is from [here](https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F).)

### For this lab, you will need:
1. Paper
2. Markers/ Pens
3. Scissors
4. Smart Phone -- The main required feature is that the phone needs to have a browser and display a webpage.
5. Computer -- We will use your computer to host a webpage which also features controls.
6. Found objects and materials -- You will have to costume your phone so that it looks like some other devices. These materials can include doll clothes, a paper lantern, a bottle, human clothes, a pillow case, etc. Be creative!

### Deliverables for this lab are: 
1. Storyboard
1. Sketches/photos of costumed device
1. Any reflections you have on the process
1. Video sketch of the prototyped interaction
1. Submit the items above in the lab1 folder of your class [Github page], either as links or uploaded files. Each group member should post their own copy of the work to their own Lab Hub, even if some of the work is the same from each person in the group.

### The Report
This README.md page in your own repository should be edited to include the work you have done (the deliverables mentioned above). Following the format below, you can delete everything but the headers and the sections between the **stars**. Write the answers to the questions under the starred sentences. Include any material that explains what you did in this lab hub folder, and link it in your README.md for the lab.

## Lab Overview
For this assignment, you are going to:

A) [Plan](#part-a-plan) 

B) [Act out the interaction](#part-b-act-out-the-interaction) 

C) [Prototype the device](#part-c-prototype-the-device)

D) [Wizard the device](#part-d-wizard-the-device) 

E) [Costume the device](#part-e-costume-the-device)

F) [Record the interaction](#part-f-record)

Labs are due on Mondays. Make sure this page is linked to on your main class hub page.

## Part A. Plan 

To stage the interaction with your interactive device, think about:

_Setting:_ Where is this interaction happening? (e.g., a jungle, the kitchen) When is it happening?

_Players:_ Who is involved in the interaction? Who else is there? If you reflect on the design of current day interactive devices like the Amazon Alexa, it’s clear they didn’t take into account people who had roommates, or the presence of children. Think through all the people who are in the setting.

_Activity:_ What is happening between the actors?

_Goals:_ What are the goals of each player? (e.g., jumping to a tree, opening the fridge). 

The interactive device can be anything *except* a computer, a tablet computer or a smart phone, but the main way it interacts needs to be using light.

\*\***Describe your setting, players, activity and goals here.**\*\*

This interaction would take place wherever you are mining cryptocurrencies. This could be your office, your basement, or perhaps a dedicated mining warehouse. Depending on where you would like the notification light to be, this could include that location as well. There is really only one player for this interactive device, the person mining cryptocurrency. The activity is the individual is mining cryptocurrencies to a shared pool. This essentially means the miner works in tandem with many other miners to mine the crytpocurrency, and then the rewards are split among all the miners. To do so, each miner solves hashing problems to produce "shares", which are then submitted to the pool. If the shares are valid, it is successful and the miner is rewarded and if they are invalid, the miner failed the hashing problem (or some other issue arose) and the miner is not rewarded. The goal of the miner is to collect as many valid shares as possible, as this is how they get rewarded. 

Sketch a storyboard of the interactions you are planning. It does not need to be perfect, but must get across the behavior of the interactive device and the other characters in the scene. 

\*\***Include a picture of your storyboard here**\*\*

<img width="949" alt="Storyboard" src="https://user-images.githubusercontent.com/52221419/132272433-5fa8b593-1b83-4db8-a270-f94c38413fe7.png">


Present your idea to the other people in your breakout room. You can just get feedback from one another or you can work together on the other parts of the lab.

\*\***Summarize feedback you got here.**\*\*

Our initial plan was to simply have two flashing lights: one for valid shares, and one for invalid shares. However, some of the feedback we got was to take an average of the amount of valid and invalid shares, and leave on a solid color (red vs. green) based on the proportion of valid to invalid shares. This is because a flash for each share that was valid or invalid does not tell you much about the general state of the machine, just whether that one singular share passed. However, if it starts to change to mostly valid or invalid, we will be able to notice with the average. 

## Part B. Act out the Interaction

Try physically acting out the interaction you planned. For now, you can just pretend the device is doing the things you’ve scripted for it. 

\*\***Are there things that seemed better on paper than acted out?**\*\*

We found that the placement of the light was imporant. We initially placed it on the desk near our computer, but found that the many lights on the desk (monitor, flashing lights from the desktop window, and the RGB keyboard) caused distraction from the light, making it less noticeable. 

\*\***Are there new ideas that occur to you or your collaborators that come up from the acting?**\*\*

It was more effective to put the device in some location that had less light-based distraction, such as a coffee table or shelf somewhere away from many flashing lights. 

## Part C. Prototype the device

You will be using your smartphone as a stand-in for the device you are prototyping. You will use the browser of your smart phone to act as a “light” and use a remote control interface to remotely change the light on that device. 

Code for the "Tinkerbelle" tool, and instructions for setting up the server and your phone are [here](https://github.com/FAR-Lab/tinkerbelle).

We invented this tool for this lab! 

If you run into technical issues with this tool, you can also use a light switch, dimmer, etc. that you can can manually or remotely control.

\*\***Give us feedback on Tinkerbelle.**\*\*

It was not working on my teammates laptop, but I was able to it to work on mine. For some reason they could not get the web server to run, although we did the same actions. It worked flawlessly on my machine. I was not able to get the web page to go fullscreen on my iPhone, however. The user interface was very simple and effective! 

## Part D. Wizard the device
Take a little time to set up the wizarding set-up that allows for someone to remotely control the device while someone acts with it. Hint: You can use Zoom to record videos, and you can pin someone’s video feed if that is the scene which you want to record. 

\*\***Include your first attempts at recording the set-up video here.**\*\*

The demo for our first use of tinkerbelle can be shown below. We then applied a costume to the prototype as lined out in Part E. Moreover, we wrote a special script to mimic a cryptocurrency miner, which is shown in the follow-up work. This helped us achieve a sense of realism for the prototpye video. 

https://youtu.be/eSSHQjrBd6M

\*\***Show the follow-up work here.**\*\*

We used the following python definitions to create a fake cryptocurrency mining script, so it appeared as if we were mining cryptocurrency but we were actually not. By calling the functions `valid()`, `invalid()`, and `normal()`, we can print out a faux line that would indicate the status of the miner. 
```
import time

class bcolors:
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

MESSAGE_WAIT = 2

def valid():
    print(f"{bcolors.OKGREEN}Eth: GPU1: ETH share found! \nEth: Share actual difficulty: 14.1 GH (!)\nEth: Share accepted in 7 ms{bcolors.ENDC}")
    time.sleep(MESSAGE_WAIT)

def invalid():
    print(f"{bcolors.FAIL}Eth: GPU1: ETH share invalid! \nEth: Share actual difficulty: 15.1 GH (!)\nEth: Share rejected in 5 ms{bcolors.ENDC}")
    time.sleep(MESSAGE_WAIT)

def normal():
    print("Eth: New job #7a6b44n from ssl://eth-us-east.flexpool.io:5555; diff: 4000 MH")
    time.sleep(MESSAGE_WAIT)
 ```

## Part E. Costume the device

Only now should you start worrying about what the device should look like. Develop a costume so that you can use your phone as this device.

Think about the setting of the device: is the environment a place where the device could overheat? Is water a danger? Does it need to have bright colors in an emergency setting?

\*\***Include sketches of what your device might look like here.**\*\*

**Costume Sketches**


<img width="1135" alt="Costume sketches" src="https://user-images.githubusercontent.com/52221419/132272323-65cee185-ef0a-41e6-b743-2810f00d24e0.png">

**Costume Prototype**


<img width="499" alt="Costume sketches" src="https://user-images.githubusercontent.com/52221419/132272363-ebed8d9a-e811-4941-a007-e0b574ed43cb.png">

\*\***What concerns or opportunitities are influencing the way you've designed the device to look?**\*\*

There is not too much concern for the device costume, considering it will simply be a light that displays whether or not your crypto mining machine is working or not. So the main thing was to provide a stable housing that would hide electrical components. It would sit somewhere safe so durability or element protection is not as important. 


## Part F. Record

\*\***Take a video of your prototyped interaction.**\*\*

https://youtu.be/jeE3tEhL88A

\*\***Please indicate anyone you collaborated with on this Lab.**\*\*
Be generous in acknowledging their contributions! And also recognizing any other influences (e.g. from YouTube, Github, Twitter) that informed your design. 

Kristjan Tomasson (kt476) and I worked on this lab together. We came up with and did all of our work equally. 

# Staging Interaction, Part 2 

This describes the second week's work for this lab activity.

## Prep (to be done before Lab on Wednesday)

You will be assigned three partners from another group. Go to their github pages, view their videos, and provide them with reactions, suggestions & feedback: explain to them what you saw happening in their video. Guess the scene and the goals of the character. Ask them about anything that wasn’t clear. 

\*\***Summarize feedback from your partners here.**\*\*

I got a few comments on canvas that proved to be helpful in changing my prototype. One of my reviewers offered the great idea to apply our technology to deep learning models, where the light can indicate if something goes awry during the long training process many deep learning models require. We did not directly implement this in our second prototype, but the technology could be easily applied to that field - we wanted to further our device before using it elsewhere.

One of my other reviewers gave a few good suggestions. First, he suggested that we can make the device portable. This is a great idea, because in that sense we can bring the CryptoChecker around wherever we are, instead of only being able to check the status in one location, where at that point we could simply look at the computer running the cryptocurrency miner. Since we used our mobile phone to create the light, this was actually already possible with our device, although the video appeared otherwise. He also suggested that we add audio to the device, in order to help further adding alerts to the crypto checker since it can be easy to ignore a light. 

My last reviewer did not add too much, but liked our storyboard and advised us to trim our video down. 

I also got some more feedback at my lab table in class, where we were told our video was not clear enough, and the light was not too visible. They also noted how the background was distracting. 

## Make it your own

Do last week’s assignment again, but this time: 
1) It doesn’t have to (just) use light, 
2) You can use any modality (e.g., vibration, sound) to prototype the behaviors! Again, be creative!
3) We will be grading with an emphasis on creativity. 

\*\***Document everything here. (Particularly, we would like to see the storyboard and video, although photos of the prototype are also great.)**\*\*

We fixed our storyboard for the second part of the lab, shown below. We actually did a Verplank diagram by accident, so we have a proper storybaord now. 

**Storyboard:**

<img width="804" alt="Fixed Storybard" src="https://user-images.githubusercontent.com/52221419/133135598-86beb93f-0c47-4a25-b313-404c28e19df9.png">

We made numerous changes to the video and the prototype. First, instead of fading from green to red based on an average of successful/failed shares, we had the miner simply display white if there was no errors. This was mainly because the user should not be paying attention to the light if everything is going to plan, so the green was too prominent of a color. We modified it to flash yellow when errors were starting to arise, but not aggressively. Once the errors multiplied and it was getting more severe, the CryptoChecker would flash red, as well as sound an alarm. This was much more noticeable than before and helped the user realize there was an issue more quickly so they can go to fix it. 

We also modified the video to make it more clear what was going on. We used a split screen tactic, with the script running on one side and the device on the right side. this made it more clear how the light was responding to the mining script. We also added text to explain the actions in the video more effectively. 

**Improved Prototype Video:**
https://www.youtube.com/watch?v=96IsJhStaT4
