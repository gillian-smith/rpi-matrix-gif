# Animated GIFs on Adafruit RGB LED Matrix with Raspberry Pi

This README describes the process of using a **Raspberry Pi** microcontroller along with my `displayGIF.py` script to display an **animated gif** on an **Adafruit RGB LED Matrix**. 

For example, I used my matrix to display a spooky ghost gif for Halloween. :jack_o_lantern:

---
<a href="https://twitter.com/heatheramahan/status/789191493088980992"><img align="left" height="150" src="https://i.giphy.com/media/rZL5cIy8irYM2JCL75/giphy-downsized-large.gif"></a>

<p>
<a href="https://twitter.com/heatheramahan"><img src="https://pbs.twimg.com/profile_images/840044211680366593/p1P6s56l_400x400.jpg" height="48" width="48"></a>
<a href="https://twitter.com/heatheramahan">@heatheramahan</a> via Twitter
<a href="https://twitter.com/heatheramahan/status/789191493088980992">October 20, 2016</a>
</p>

<p>
Happy Halloween! 👻 Spooky little collab by <a href="https://twitter.com/jettisonjoe">@jettisonjoe</a> (pixel art) & <a href="https://twitter.com/heatheramahan">me</a> (pi hacking).
</p>

<p>
<a href="https://twitter.com/adafruit">@adafruit</a>
<a href="https://twitter.com/hashtag/RaspberryPi">#RaspberryPi</a>
</p>

---

## HARDWARE

| [32x32 RGB LED Matrix Panel](https://www.adafruit.com/products/2026) | Raspberry Pi[^rpi] | [Adafruit RGB Matrix HAT + RTC for Raspberry Pi - Mini Kit](https://www.adafruit.com/product/2345) |
| :---: | :---: | :---: |
| <a href="https://www.adafruit.com/products/2026"><img height="150" src="https://cdn-shop.adafruit.com/970x728/2026-05.jpg"></a> | <a href="https://www.adafruit.com/product/3055"><img height="150" src="https://cdn-shop.adafruit.com/970x728/3055-08.jpg"></a> | <a href="https://www.adafruit.com/product/2345"><img height="150" src="https://cdn-shop.adafruit.com/970x728/2345-08.jpg"></a> |
| Displays graphics on a grid of 1024 dazzling RGB LEDs! | The brains of the operation.  Raspberry Pi Model Zero/A+/B+/Pi 2/3/ or Pi 4 are all compatible. | Plugs into your Raspberry Pi and allows you to control the RBG LED Matrix panel. (Soldering required!) |


[^rpi]:
    Originally I used a [Raspberry Pi Model B+](https://www.adafruit.com/products/1914) (and Raspbian OS) for this project back in 2016. In 2022, I revisited the project using a [Raspberry Pi 3 - Model B](https://www.adafruit.com/product/3055) (and Raspberry Pi OS). 

| [MicroSD Memory Card](https://www.adafruit.com/products/2692) | (Optional) [Mini USB WiFi Module](https://www.adafruit.com/product/2810)[^wifi]| [5V 4A power supply](https://www.adafruit.com/product/1466) | [Female DC Power adapter - 2.1mm jack to screw terminal block](https://www.adafruit.com/products/368)|
| :---: | :---: | :---: | :---: |
| <a href="https://www.adafruit.com/products/2692"><img height="150" src="https://cdn-shop.adafruit.com/970x728/2692-01.jpg"></a>| <a href="https://www.adafruit.com/product/2810"><img height="150" src="https://cdn-shop.adafruit.com/970x728/2810-10.jpg"></a> | <a href="https://www.adafruit.com/product/1466"><img height="150" src="https://cdn-shop.adafruit.com/970x728/1466-02.jpg"></a> | <a href="https://www.adafruit.com/products/368"><img height="150" src="https://cdn-shop.adafruit.com/970x728/368-03.jpg"></a> |
| Storage for Raspberry Pi OS and your projects. | Connects your Raspberry Pi to the internet via wifi. | Powers the RGB Matrix HAT. | Connects the HAT to the power supply. |
  
[^wifi]:
    If you are using a Raspberry Pi that includes built-in wifi (ex: Raspberry Pi 3), you do need to purchase a wifi module. Alternatively, you can use an Ethernet cable for a wired network connection. Originally, I used the [Miniature WiFi (802.11b/g/n) Module](https://www.adafruit.com/product/814) but this product is now discontinued. The product linked in the table is a recommended alternative. 

| [USB MicroSD Card Reader/Writer](https://www.adafruit.com/product/939) | [USB A to Micro-B cable](https://www.adafruit.com/product/592)[^usb] | USB mouse, HDMI display & cable | Soldering Supplies |
| :---: | :---: | :---: | :---: |
| <a href="https://www.adafruit.com/product/939"><img height="150" src="https://cdn-shop.adafruit.com/970x728/939-06.jpg"></a> | <a href="https://www.adafruit.com/product/592"><img height="150" src="https://cdn-shop.adafruit.com/970x728/592-01.jpg"></a> | ![](https://staging-assets.raspberrypi.com/static/hero__container-bg-89d1baabda817d708f2a5fb82ece2c6c.svg)| <a href="https://learn.adafruit.com/adafruit-guide-excellent-soldering"><img height="150" src="https://cdn-learn.adafruit.com/guides/cropped_images/000/000/102/medium640/Solder_Badge.png"></a> |
| Required for installing Rasberry Pi OS. | Powers the Raspberry Pi using your regular computer’s USB port or a USB wall charger. | You’ll need these items to interface with your Raspberry Pi the first time you log in. Later, you can set up SSH to access your Raspberry Pi remotely. | Soldering iron, solder, and wirecutters are required to assemble the [Adafruit RGB Matrix HAT + RTC](https://www.adafruit.com/product/2345). |

[^usb]:
    Alternatively, you can use a [USB C to Micro B Cable](https://www.adafruit.com/product/3878), depending on your preference / available USB ports.

---

## SOFTWARE

| [Raspberry PI OS](https://www.raspberrypi.com/software/) | [Aseprite](https://www.aseprite.org/) | [Nano](https://www.nano-editor.org/) |
| :---: | :---: | :---: |
| <a href="https://www.raspberrypi.com/software/"><img height="150" src="https://upload.wikimedia.org/wikipedia/commons/d/d1/Raspberry_Pi_OS_Logo.png"></a> | <a href="https://www.aseprite.org"><img height="150" src="https://www.aseprite.org/assets/images/header-logo.png"></a> | <a href="https://www.nano-editor.org/"><img height="150" src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Gnu-nano.svg/1200px-Gnu-nano.svg.png"></a> |
| The official OS for Raspberry Pi microcontrollers. | Animated sprite editor & pixel art tool. (Or some other program for creating 32x32 animated gif.) | Command line text editor that comes pre-installed on Raspberry Pi OS. (Or some other code editor, such as [Sublime Text](https://www.sublimetext.com/) or [VS Code](https://code.visualstudio.com/).) |

---

## INSTRUCTIONS

### Step 1: Prepare your Raspberry Pi

<ol>
  <li>
    Install <a href="https://www.raspberrypi.com/software/">Raspberry Pi OS</a>.
		<ol>
			<li>Insert your <a href="https://www.adafruit.com/products/2692">MicroSD Memory Card</a> into your <a href="https://www.adafruit.com/product/939">USB MicroSD Card Reader/Writer</a> and attach it to your regular computer.</li>
			<li>Recommended: Use the official <a href="https://www.raspberrypi.com/documentation/computers/getting-started.html#using-raspberry-pi-imager">Raspberry Pi Imager</a> to install Raspberry Pi OS Lite.</li>
		</ol>
    <a href="https://www.raspberrypi.com/software/">
			<img src="https://assets.raspberrypi.com/static/md-bfd602be71b2c1099b91877aed3b41f0.png" height="250">
		</a>
  </li>
	<li>
    Connect accessories and power up.
		<ol>
			<li>Insert the prepared MicroSD card into your Raspberry Pi.</li>
			<li>Connect <strong>your keyboard</strong> and <strong>HDMI display</strong> to your Raspberry Pi.</li>
			<li>If needed, attach your <a href="https://www.adafruit.com/product/2810">Mini USB WiFi Module</a>. Or, if you're using a wired connection, attach your ethernet cable.</li>
			<li>Apply power using your <a href="https://www.adafruit.com/product/592">USB A to Micro-B cable</a> and a USB power source.
 </li>
		</ol>
<!-- 		<img src="https://staging-assets.raspberrypi.com/static/hero__container-bg-89d1baabda817d708f2a5fb82ece2c6c.svg" height="250"> -->
  </li>
	<li>
    Log in to your Raspberry Pi.
		<p>The default credentials are <strong>pi</strong> (user name) and <strong>raspberry</strong> (password).</p>
	</li>
	<li><a href="https://www.raspberrypi.com/documentation/computers/configuration.html#wireless-networking-command-line">Connect your Raspberry Pi to Wifi.</a>
		<p>(Ignore this step if you're using a wired network connection.)</p>
		<p>The crucial steps are summarized below. Please reference the <a href="https://www.raspberrypi.com/documentation/computers/configuration.html#wireless-networking-command-line">documentation</a> for more details and troubleshooting.</p>
		<ol>
			<li>Configure the <strong>wireless country</strong> in the <strong>Localization</strong> options using the <code>raspi-config</code> command line tool.</li>
			<li>Edit the <code>wpa-supplicant.conf</code> file to include your wireless network ID and password.</li>
			<li>Reconfigure the interface with <code>wpa_cli -i wlan0 reconfigure</code>.</li>
		</ol>
  </li>
  <li>
    (Optional) <a href="https://www.raspberrypi.org/documentation/remote-access/ssh/">Set Up SSH for Remote Connection</a>.
		<p>With an SSH connection, you can log in to your Raspberry Pi remotely (from your regular computer). You’ll no longer need the HDMI display and USB keyboard to access your Raspberry Pi.</p>
		<p>The crucial steps are summarized below. Please reference the <a href="https://www.raspberrypi.org/documentation/remote-access/ssh/">documentation</a> for more details and troubleshooting.</p>
		<p>On your Raspberry Pi:</p>
		<ol>
			<li>Enable SSH using the <code>raspi-config</code> command line tool.</li>
			<li>Run the <code>hostname -I</code> command and note your Raspberry Pi's IP address.</li>
		</ol>
		<p>On your regular computer:</p>
		<ol>
			<li><a href="https://www.raspberrypi.com/documentation/computers/remote-access.html#secure-shell-from-linux-or-mac-os">Connect to your Raspberry Pi via SSH</a> using the command <code>ssh pi@&lt;IP&gt;</code> in the terminal.</li>
			<p>Replace <code>&lt;IP&gt;</code> with your Raspberry Pi's IP address.</p>
		</ol>
		
  </li>
  <li>
    (Optional) Set Up Remote Code Editing with your preferred code editor, for example <a href="https://github.com/poemusica/rpi-matrix-gif/blob/master/UsingRsub.md">Sublime Text</a>.
		<p>Alternatively, you can ignore this step and use <a href="https://www.nano-editor.org/">Nano</a> to write and edit code via the command line.</p>
  </li>
</ol>    

### Step 2: Assemble the HAT

Follow Adafruit's [great tutorial](https://learn.adafruit.com/adafruit-rgb-matrix-plus-real-time-clock-hat-for-raspberry-pi/assembly)
on how to solder the components of the RGB Matrix HAT.

If you’re new to soldering, see also Adafruit’s [Guide to Excellent Soldering](https://learn.adafruit.com/adafruit-guide-excellent-soldering).

Don’t be intimidated! This project was my first time soldering. I was able to do it and you can do it too.
  
 ---
<a href="https://twitter.com/heatheramahan/status/782779412462743552"><img align="left" height="150" src="https://pbs.twimg.com/media/Ctz9ssYUkAAT1fu.jpg"></a>

<p>
<a href="https://twitter.com/heatheramahan"><img src="https://pbs.twimg.com/profile_images/840044211680366593/p1P6s56l_400x400.jpg" height="48" width="48"></a>
<a href="https://twitter.com/heatheramahan">@heatheramahan</a> via Twitter
<a href="https://twitter.com/heatheramahan/status/782779412462743552">October 3, 2016</a>
</p>

<p>
Solder? I hardly know her!
<a href="https://twitter.com/hashtag/myfirst">#myfirst</a>
<a href="https://twitter.com/hashtag/soldering">#soldering</a>
</p>
<p>
<a href="https://twitter.com/adafruit">@adafruit</a>
<a href="https://twitter.com/hashtag/RaspberryPi">#RaspberryPi</a>
</p>

---

### Step 3: Activate the Matrix

Follow Adafruit’s [instructions](https://learn.adafruit.com/adafruit-rgb-matrix-plus-real-time-clock-hat-for-raspberry-pi/driving-matrices)
for connecting the hardware, installing PIL (Python Image Library), and downloading/running their demo code.
    
When you have the Adafruit demos working, you’re ready to start displaying your own animations!

### Step 4: Display Animation


  1. On your regular computer, make a 32x32 pixel art animation using [Aseprite](https://www.aseprite.org/) (or some other software) and export it as a gif.
    

  2. Copy your animated gif onto your Raspberry Pi.
     
		On your regular computer, open a new terminal and type:
		```
		scp <source> pi@<pi_ip>:<destination>
		```
		replacing the following parts of the command as described:
		- `<source>` is the path to the file you want to copy
		- `<pi_ip>` is your Raspberry Pi’s IP address
		- `<destination>` the path to this project directory on your Raspberry Pi
    

  3. Run the `displayGIF.py` script to display your animation.
  	
		On the Raspberry Pi or in your SSH terminal, type:
		```
		python displayGIF.py
		```
		By default, the script displays the included sample gif created by [@jettisonjoe](https://github.com/jettisonjoe).
		![Ghost](https://github.com/poemusica/rpi-matrix-gif/blob/master/myGIF.gif)
    
		To display your own gif, replace `myGIF` in the code with the name of your gif.
    
		If you want to stop the script, use the `Ctrl`+`c` key combination.
    

### (Optional) Step 5: Run on boot

If you want the `displayGIF.py` script to run automatically whenever you start up the Raspberry Pi,
follow [these instructions](https://www.raspberrypi.org/documentation/linux/usage/rc-local.md)
to edit the `rc.local` file on your Raspberry Pi.
