# Chess-World
It is a simple chess game which runs on flask server. It is equipped with one built-in chess engine named devzero (where 'dev' stands for developer and 'zero' stands as an ending which many chess engines have such as alphazero and leelazero)  developed by me and three other uci compatible chess engines named stockfish, cdrill and deuterium for learning purposes. It has an assistant which gives the user some introduction, instructions and credits. It also warns the user when it is check and also when it is a checkmate or stalemate. This game can be played on two different devices by port forwarding your local host port or by the ngrok tool available for windows, mac and linux. But as it is running on a flask server it doesn't have any restrictions means anyone can play anymove, at anytime.
# Installation
Run the following command in your terminal:
```
git clone https://github.com/AnshGaikwad/Chess-World.git
```
# Requirements
You can run the `setup.py` by which all the modules will be downloaded automatically by pip:
```
python setup.py
```
Or you can do it manually by executing the following commands:
```
pip install python-chess
```
```
pip install flask
```
```
pip install pyttsx3
```
```
pip install webbrowser
```
# Execution
Run the following code in your terminal:
```
python play.py
```
# Features
> 1. Voice Assistant
> 2. Follows all chess rules
> 3. Four Compatible Chess Engines
> 4. Can be played on two different devices
# Playing over the internet
You can use the tool [ngrok](https://ngrok.com/download) for playing it in two different places of the world. Just download it, cd into the following directory and type the following code:
```
ngrok http 5000
```
Now send the following link provided by ngrok to the user you wish to play with. It will basically redirect the user to your [localhost:5000](http://127.0.0.1:5000).
# Some Bugs
> 1. Some engines stop working if used rapidly
> 2. No conditions are applied for playing over the internet, i.e. anyone can play anymove at anytime.
# Group Members
> 1. [Arshad Patel](https://github.com/arshadpatel2001)
> 2. [Nisha Modani](https://github.com/nisha2204)
> 3. [Prashanth Bijamwar](https://github.com/Prashanth820)
> 4. [Sarvesh Patil](https://github.com/Patil-Sarvesh)
