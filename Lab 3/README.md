# Chatterboxes
[![Watch the video](https://user-images.githubusercontent.com/1128669/135009222-111fe522-e6ba-46ad-b6dc-d1633d21129c.png)](https://www.youtube.com/embed/Q8FWzLMobx0?start=19)

In this lab, we want you to design interaction with a speech-enabled device--something that listens and talks to you. This device can do anything *but* control lights (since we already did that in Lab 1).  First, we want you first to storyboard what you imagine the conversational interaction to be like. Then, you will use wizarding techniques to elicit examples of what people might say, ask, or respond.  We then want you to use the examples collected from at least two other people to inform the redesign of the device.

We will focus on **audio** as the main modality for interaction to start; these general techniques can be extended to **video**, **haptics** or other interactive mechanisms in the second part of the Lab.

## Prep for Part 1: Get the Latest Content and Pick up Additional Parts 

### Pick up Additional Parts

As mentioned during the class, we ordered additional mini microphone for Lab 3. Also, a new part that has finally arrived is encoder! Please remember to pick them up from the TA.

### Get the Latest Content

As always, pull updates from the class Interactive-Lab-Hub to both your Pi and your own GitHub repo. As we discussed in the class, there are 2 ways you can do so:

**\[recommended\]**Option 1: On the Pi, `cd` to your `Interactive-Lab-Hub`, pull the updates from upstream (class lab-hub) and push the updates back to your own GitHub repo. You will need the *personal access token* for this.

```
pi@ixe00:~$ cd Interactive-Lab-Hub
pi@ixe00:~/Interactive-Lab-Hub $ git pull upstream Fall2021
pi@ixe00:~/Interactive-Lab-Hub $ git add .
pi@ixe00:~/Interactive-Lab-Hub $ git commit -m "get lab3 updates"
pi@ixe00:~/Interactive-Lab-Hub $ git push
```

Option 2: On your your own GitHub repo, [create pull request](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2021Fall/readings/Submitting%20Labs.md) to get updates from the class Interactive-Lab-Hub. After you have latest updates online, go on your Pi, `cd` to your `Interactive-Lab-Hub` and use `git pull` to get updates from your own GitHub repo.

## Part 1.
### Text to Speech 

In this part of lab, we are going to start peeking into the world of audio on your Pi! 

We will be using a USB microphone, and the speaker on your webcamera. (Originally we intended to use the microphone on the web camera, but it does not seem to work on Linux.) In the home directory of your Pi, there is a folder called `text2speech` containing several shell scripts. `cd` to the folder and list out all the files by `ls`:

```
pi@ixe00:~/text2speech $ ls
Download        festival_demo.sh  GoogleTTS_demo.sh  pico2text_demo.sh
espeak_demo.sh  flite_demo.sh     lookdave.wav
```

You can run these shell files by typing `./filename`, for example, typing `./espeak_demo.sh` and see what happens. Take some time to look at each script and see how it works. You can see a script by typing `cat filename`. For instance:

```
pi@ixe00:~/text2speech $ cat festival_demo.sh 
#from: https://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)#Festival_Text_to_Speech

echo "Just what do you think you're doing, Dave?" | festival --tts
```

Now, you might wonder what exactly is a `.sh` file? Typically, a `.sh` file is a shell script which you can execute in a terminal. The example files we offer here are for you to figure out the ways to play with audio on your Pi!

You can also play audio files directly with `aplay filename`. Try typing `aplay lookdave.wav`.

\*\***Write your own shell file to use your favorite of these TTS engines to have your Pi greet you by name.**\*\*
(This shell file should be saved to your own repo for this lab.)

Bonus: If this topic is very exciting to you, you can try out this new TTS system we recently learned about: https://github.com/rhasspy/larynx

### Speech to Text

Now examine the `speech2text` folder. We are using a speech recognition engine, [Vosk](https://alphacephei.com/vosk/), which is made by researchers at Carnegie Mellon University. Vosk is amazing because it is an offline speech recognition engine; that is, all the processing for the speech recognition is happening onboard the Raspberry Pi. 

In particular, look at `test_words.py` and make sure you understand how the vocab is defined. Then try `./vosk_demo_mic.sh`

One thing you might need to pay attention to is the audio input setting of Pi. Since you are plugging the USB cable of your webcam to your Pi at the same time to act as speaker, the default input might be set to the webcam microphone, which will not be working for recording.

\*\***Write your own shell file that verbally asks for a numerical based input (such as a phone number, zipcode, number of pets, etc) and records the answer the respondent provides.**\*\*

Bonus Activity:

If you are really excited about Speech to Text, you can try out [Mozilla DeepSpeech](https://github.com/mozilla/DeepSpeech) and [voice2json](http://voice2json.org/install.html)
There is an included [dspeech](./dspeech) demo  on the Pi. If you're interested in trying it out, we suggest you create a seperarate virutal environment for it . Create a new Python virtual environment by typing the following commands.

```
pi@ixe00:~ $ virtualenv dspeechexercise
pi@ixe00:~ $ source dspeechexercise/bin/activate
(dspeechexercise) pi@ixe00:~ $ 
```

### Serving Pages

In Lab 1, we served a webpage with flask. In this lab, you may find it useful to serve a webpage for the controller on a remote device. Here is a simple example of a webserver.

```
pi@ixe00:~/Interactive-Lab-Hub/Lab 3 $ python server.py
 * Serving Flask app "server" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 162-573-883
```
From a remote browser on the same network, check to make sure your webserver is working by going to `http://<YourPiIPAddress>:5000`. You should be able to see "Hello World" on the webpage.

### Storyboard

Storyboard and/or use a Verplank diagram to design a speech-enabled device. (Stuck? Make a device that talks for dogs. If that is too stupid, find an application that is better than that.) 

\*\***Post your storyboard and diagram here.**\*\*

**Storyboard:**

<img width="1026" alt="lab3a storyboard" src="https://user-images.githubusercontent.com/52221419/135953340-dd897e11-e76a-4032-99a1-0642d269607a.png">

**Verplank Diagram:**

<img width="1324" alt="lab 3a verplank" src="https://user-images.githubusercontent.com/52221419/135953362-2af79db8-a7ea-4819-a305-17a62c0439d6.png">


Write out what you imagine the dialogue to be. Use cards, post-its, or whatever method helps you develop alternatives or group responses. 

\*\***Please describe and document your process.**\*\*

As the device is fairly simple and merely takes a message, the dialogue was not very extensive. I thought about this with a quick sketch on a piece of scrap paper. The doorbell simply asks to leave a message after the door remains unopened, records the message, and then wishes them farewell. 

### Acting out the dialogue

Find a partner, and *without sharing the script with your partner* try out the dialogue you've designed, where you (as the device designer) act as the device you are designing.  Please record this interaction (for example, using Zoom's record feature).

\*\***Describe if the dialogue seemed different than what you imagined when it was acted out, and how.**\*\*

I partnered with Kristjan Ari Tomasson. Here is a link to the dialogue: 

https://youtu.be/DRni86YhyUM

When reviewing the video, I realized there were a few issues with my script. For example, it is a better to simply state to leave a message after the tone rather than ask. Not only does this make the device simpler, it also promises to notify the homeowner about any unknown arrivals at the property. If the guest were to not leave a message then the homeowner would still see that a message was recorded in the logs. I modified my storyboard to match this update. Another change that I thought to incorporate would be to understand the length of the message, as the the guest could speak for too long and it may get cut off. Otherwise, the dialogue was fairly straightforward and did not have any issues. 

### Wizarding with the Pi (optional)
In the [demo directory](./demo), you will find an example Wizard of Oz project. In that project, you can see how audio and sensor data is streamed from the Pi to a wizard controller that runs in the browser.  You may use this demo code as a template. By running the `app.py` script, you can see how audio and sensor data (Adafruit MPU-6050 6-DoF Accel and Gyro Sensor) is streamed from the Pi to a wizard controller that runs in the browser `http://<YouPiIPAddress>:5000`. You can control what the system says from the controller as well!

\*\***Describe if the dialogue seemed different than what you imagined, or when acted out, when it was wizarded, and how.**\*\*

# Lab 3 Part 2

For Part 2, you will redesign the interaction with the speech-enabled device using the data collected, as well as feedback from part 1.

## Prep for Part 2

1. What are concrete things that could use improvement in the design of your device? For example: wording, timing, anticipation of misunderstandings...

Like I noted above, the wording of the device will certainly need improvement - simply stating that we are taking recording and when the recording will begin rather then asking if they would like to leave a message. This will also help to ensure the homeowner knows whether or not someone rang the doorbell and was not let in, regardless of if the guest got into the house or not. One concern I was worried about was the audio level of the device - if this were to be put in practice, the audio might get easily washed out by the sounds of the environment. 

2. What are other modes of interaction _beyond speech_ that you might also use to clarify how to interact?

As mentioned above, I will need to incorporate a tactile button that represents the doorbell, and I will also need to find something to represent the door. I think I will use a button here as well, as it simply needs to click when the door opens. 

I was also thinking about using the camera in order to take a photo of whoever is at the door, to give the homeowner an even better idea of who came to the house. 

Additionally, using the proximity sensor to detect when someone is at the door could also help to further the device, and say hello/welcome to anyone at the door. This could be used alternatively to the doorbell to initiate the interaction, but that would indicate that it would be something the homeowner would have to set whenever they left the house. I figured it would be better used as a welcoming device, so that the homeowner does not have to set it whenever they leave the house and can always leave it running. Additionally, It would be a nice feature so that even while the homeowner is home there is something to greet any guests right upon arrival. 

3. Make a new storyboard, diagram and/or script based on these reflections.

**Updated Storyboard**

<img width="1000" alt="lab 3b storyboard" src="https://user-images.githubusercontent.com/52221419/136468799-ac3aced2-1609-4816-a405-26b477fb8f0a.png">

**Updated Verplank Diagram**

<img width="1268" alt="lab 3b verplank" src="https://user-images.githubusercontent.com/52221419/136468820-fb45a895-8fbc-4484-8810-400e5e2e1a1a.png">

**Updated Script**

<img width="724" alt="lab 3b script" src="https://user-images.githubusercontent.com/52221419/136468837-94d2c307-dc4b-4825-9010-3d0c5e43a12f.png">

## Prototype your system

The system should:
* use the Raspberry Pi 
* use one or more sensors
* require participants to speak to it. 

*Document how the system works*

The system works fairly simply. 
1. It begins by detecing someone approaching the device using the proximity sensor, at which point it greets the person and invites them to press the doorbell (the boottom button).
2. Once someone presses the doorbell, the system begins a countdown which could end prematurely if the door is opened (the top button), where the script will simply stop and restart at step one of this process. 
3. Otherwise, if the countdown reaches 0, then the device prompts the guest that nobody is home and that it will begin recording a message and taking a photo after a beep. 
4. Then the system beeps, and begins recording, at which point the guest speaks their message. 
5. Once the recording is done, the system takes a photo.
6. The photo and recording are then saved into respective photos and recordings folders on the system, marked with an index number for usability by the homeowner. 
7. Once the data is saved, the system informs the guest of this and wishes them a good day.
8. The system then resets and begins scannign for proximity of the next guest, or in other words, restarts at step 1 of this process. 

*Include videos or screencaptures of both the system and the controller.*

**Shown below is a picture of the front of my prototype.**

<img width="565" alt="lab3b prototype front" src="https://user-images.githubusercontent.com/52221419/137197408-87a80ee0-e034-4259-957e-d6d001e6c206.png">

There are a few items marked up on the image. 
- The green box surrounds the button that imitates the door being opened. If the door was opened, this button would represent the action taken by it. 
- The red box surrounds the button that represents the doorbell. 
- The blue box surrounds the proximity sensor of the device.
- The pink box surrunds the camera that will be used to take a photo of the person at the door after the message is taken. On the outside of this camera is the speakers. 

**Shown here is the interior of the prototype.**

<img width="607" alt="lab 3b prototype interior" src="https://user-images.githubusercontent.com/52221419/137197552-cce97568-3ac0-4c22-b92e-31ee336f26a1.png">

## Test the system
Try to get at least two people to interact with your system. (Ideally, you would inform them that there is a wizard _after_ the interaction, but we recognize that can be hard.)

Instead of a _10 second_ wait time after the doorbell had been pressed, I pushed it down to **3 seconds** for testing purposes so they could see results faster. 

Here are two videos from my two tests.
- My first video's star was Will Tappen, another Cornell Tech student:  https://youtu.be/GjtVt2WZaBA 
- My second video's star was Kristjan Ari Thomasson, another Cornell Tech student who is also currently taking IDD: https://youtu.be/2K_Z4_HUMdU

The photos & audio recordings from these testes can be found in the photos and recordings directory of this repository, respectively. 

Answer the following:

### What worked well about the system and what didn't?
\*\**your answer here*\*\*

**What worked well**
- The flow from my various scripts was much smoother than I expected. It was quite easy to go from bash scripts to python and back, as well as using multiple different text2speech commands, voice recordings, photos, and sleep/wait timers. I imagined there would have been more finnicky issues with it, but it worked well. (I even learned a good amount of bash scripting!)
- Although managing accessing the recordings/photos was somewhat annoying, the actual storage of them worked well, and even allowed for many different guests to be logged via index markers for each entry. 

**What did _not_ work well**
- The process of taking a photo was longer than my testers expected. Will, my first tester, almost left and got confused asking "Did it take the photo yet?" This could have been problematic if they thought it was instant, like many modern cameras. 
- The homeowner would be required to ssh into the raspberry pi and pull the photos and recordings directly from the pi onto an sd card/flash drive/online repository to view them. This could be improved by immediately pushing the data to a web server of sorts, where the homeowner can log into and view everything that was collected. Alternatively, there could be a display on the back of the door that allows the homeowner to view a file system and directly select photos/recordings from there. 
- The voice recording length was a fixed amount of time, and for Will (the first tester), I found he was almost cut off by the end of the recording. If he left a longer message, it would have been disregarded after a certain point. For Kristjan (the second tester), his recording was shorter than the length and he had to wait a little for the end of the recording to hit. 

### What worked well about the controller and what didn't?
\*\**your answer here*\*\*

**What worked well**
- It was fairly intuitive, and especially with the written guide on the device case, people understood what they needed to do to interact with the buttons. As mentioned in the next section, the proximity detector was not one of the controlling sensors that was not as intuitive. 
- The placement of the camera made it easy for the testers to know where to look for the photo, as it was obvious that it was a camera. 

**What did _not_ work well**
- First, the proximity sensor was not as sensitive as it should have been. In the video, you saw that the testers had to get very close to the proximity sensors to detect it. In fact, I had to actually tell Will (the first tester) to wave at the green light (where the proximity sensor was) in order to get him to detect it. This became something of an issue mainly because the software required the proximity sensor to be detected in order to begin detecting the doorbell and recording/taking a photo if nobody opened the door. 
- Second, although I mentioned above the controller was fairly intuitive, that was because it somewhat relied on a written guide on the device that could have been potentially misunderstood/misread. A more obvious design would be ideal here, that could remove the need for the written guide. In fact, it held up my first tester (Will) who read the whole guide thinking he needed to press the doorbell or something to activate the interaction. 

I was also unable to directly test the door open function on real people. This is partly due to two things: 
- I would have had to enter the area and press the button myself, introducing issues with allowing the tester to figure things out on their own. 
- It was difficult to literally have a door open to activate this button, so as mentioned above, I merely used the button on the raspberry pi to imitate this. There would have been much higher costs & engineering processing associated with literally connecting the door opening to the button activation.
- That being said, most of the device was aimed at handling the case when nobody opened the door. If someone opened the door, the device was not useful beyond greeting someone upon arrival, which was already shown in the current testing environment. Since it merely would end the script process, the door open function was very simple, and I felt _more_ comfortable leaving that out of the testing, although this is certainly not ideal. 

### What lessons can you take away from the WoZ interactions for designing a more autonomous version of the system?

\*\**your answer here*\*\*
- As mentioned above, it would be important to include an easier method for the homeowner to access photos oon the device, rather than having to manually log into the raspberry pi and move them to another platform on their own. This could have been done with perhaps a web server as described before, or a display on the back of the door with its own interface. 
- A more sensitive setting for the proximity sensor, or even a more precise proximity sensor altogether would have further helped. Rather than taking some waving and investigating (which could lead to someone not usuing the device at all) it would be much more fluid and autonomous. 
- Perhaps some way of asking the user for how long they would like the message to avoid cutting them off/waiting too long after a short message would make it a more fluid experience. Moreover, it would be great to find a way to automatically detect when there is enough silence to requite ending the reording. This could also be done with a button to end the recording prematurely, similar to how voicemails work (ending the call). 
- Perhaps instead of actually using the door to indicate if someone opened it, it could be handled by the homeowner with a button on the back of the door or perhaps a remote web server where they can end the script prematurely. This could be extended to maybe unlock the door and allow them in remotely, but this would also be complicated to set up and certainly concerning regarding privacy. 
- Utilize an upgraded camera or find faster camera management software that would improve the speed with which the photo was taken. 
- Rather than depending on the proximity detector to start the interaction, it would be a good idea to also allow the usage of simply pressing the doorbell to start the interaction. This way if the proximity detector fails, it will still record the guest / take a photo if they press the doorbell. 

### How could you use your system to create a dataset of interaction? What other sensing modalities would make sense to capture?

\*\**your answer here*\*\*

I already take a photo and a recording of the user throughout the recording, but there are a number of things I could do to further collect data for a dataset of interaction.
- Adding a speech2text component to store the data not just as an audio recording for the homeowner (like a classic voicemail) but as textual data as well would both conveniently allow the homeowner to read what was in the recording rather than have to play it, but also use NLP models to see what the messages are describing and perhaps what kinds of messages they get at certain times. 
- Logging the proximity data to observe how far the guests normally are when they arrive at a house could also be useful information that could potentially further help to describe trends. As mentioned above, this would most likely require a more precise proximity sensor. 
- Identifying noise in the audio / sounds not directly meant to be included in the recording could further introduct features that could indicate something important in the data, help create future products. 

In terms of other sensing modalities I could capture, there are certainly a few:
- Collecting information about the temperature outside could prove useful, in order to see how the temperature might affect the usage of automatic doorbells / how people arrive at a house. 
- Similar to the above idea, this device could also measure humidity to similar see how it might affect automatic doorbells / arrivals at a house. 

