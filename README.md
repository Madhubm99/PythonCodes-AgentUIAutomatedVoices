1. The files here are a content of a  VS code python project. Please add these contents  as a project in your "vs code" or "pycharm".
2. There are recorded voices present in the folder "conversation" which trigger the convo.
3. Download the application "CABLE OUTPUT".
4. Run the code "device_index" present in the folder to determine the device name and its index.
5. In the console you can see the Cable input integrated with the devices present in the system. observe this "CABLE Input (VB-Audio Virtual C (ID: #)", where # is the device number.
6. open "my_mic_write" python file in vs code/pycharm.
7. Add the necessary libraries like "py audio", "wave", "OS" and "logging".
8. Add the necessary  "deviceId" with the device number in the code according to the device index number. Which makes the device run the conversation of the agent through the mic of the system, where as the speaker will be played directly.
9. open the main.yaml file and add a line with the "acquisitions" :  
handle_events_sleep_secs: 1.0
    debug_asyncio: False
    use_live_not_file: True
    caller_enabled: True
    agent_enabled: True
    input_device_name: "CABLE Output" // this line would be added in the .yaml file.
10. Run the "my_mic_write" python  file in vs code or through cmd to trigger the conversation when you already are logged in to "Agent UI" which starts a Conversation.
