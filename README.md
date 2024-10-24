<a id="readme-top"></a>

<h1 align='center'>Speed Typing Test :stopwatch:</h1> 

<div align='center'>

<img src='/images/WPM_Speed_Test.png' alt='Picture of the words per minute Python speed typing test, measuring the users typing speed and giving feedback on mistakes.'>

<p align='center'>Welcome to the Speed Typing Test! This project allows users to measure their typing speed in Words Per Minute (WPM) and gives real-time feedback on mistakes and overall performance.<br/>

<a href='https://github.com/AmberForrester/WPM-Typing-Test'><strong>Source Code »</strong></a>
<br />
<br />
<a href='https://github.com/AmberForrester/WPM-Typing-Test/issues/new?assignees=&labels=bug&projects=&template=bug-report-%F0%9F%90%9E.md&title='>Report Bug</a>
.
<a href='https://github.com/AmberForrester/WPM-Typing-Test/issues/new?assignees=&labels=enhancement&projects=&template=feature-request-%F0%9F%9A%80.md&title='>Request Feature</a>
</p>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#features">Features</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#steps-to-install">Steps to Install</a></li>
    <li><a href="#how-to-run-the-application">How to Run the Application</a></li>
    <li><a href="#how-the-test-works">How the Test Works</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>
<br />



## Features
- **Real-time WPM Calculation:** Measures typing speed as you type.
- **Error Tracking:** Highlights mistakes in red and displays the number of errors.
- **Responsive Feedback:** Shows live updates of your WPM and error count.
<br />
<br />
A good understanding of Python and Pygame would be beneficial to helping you create this project. However, it is always good practice to refer to the Documentation available when developing ***any*** project. 

_Please refer to the [Python Documentation](https://docs.python.org/3/) for your reference._

_The standard shell of Python, or REPL (Read-Eval-Print Loop) allows you to run Python code interactively as you work on a project or are in the process of learning this programming language. You may find it useful to vist the [Getting the Most Out of the Python Standard REPL website](https://realpython.com/python-repl/) to further your understanding and produce better results._

<p align="right">(<a href="#readme-top">top of page</a>)</p>



## Installation

### Prerequisites
- **Python** >= 3: Make sure Python is installed on your machine. You can download it from [Python's official website](https://www.python.org/downloads/).
- **Windows Users:** If you are running this project on Windows, you'll need to install the `windows-curses` package to use the `curses` library.




### Steps to Install

1. **Clone the Repository:**
  ```bash
  git clone https://github.com/AmberForrester/WPM-Typing-Test
  ```

2. **Navigate to the project directory:**
  ```bash
  cd WPM-Typing-Test
  ```

3. **Install Required Dependencies:** 

- For **Windows users:** Run the following command to install the `windows-curses` package:
  ```bash
  pip install windows-curses
  ```
- For **Linux/macOS users:** No additional dependencies are needed, as `curses` is already part of the Python standard library.

4. **Add your own sample text:**
- You can add or modify the `text.txt` file to include your own sample text that users will type during the test. 
- Each line in the `text.txt` file should contain a different sentence or paragraph for the test.

<p align="right">(<a href="#readme-top">top of page</a>)</p>



### How to Run the Application

Once you've cloned the project and installed Python, follow these steps to run the typing test:

1. Open your terminal in the project directory and run the following command: 
   ```bash
   python speedTest.py
   ```

2. You will be greeted with a welcome screen. Press any key to begin the test.

3. Type the displayed text as quickly and accurately as you can.

4. Press any key to start a new test or `Esc` to exit the program.



## How the Test Works

- **Words Per Minute (WPM):** Your typing speed is calculated based on the total number of characters typed (including mistakes). The WPM is updated in real-time as you type. </br>

- **Errors:** Incorrect characters are highlighted in red, and the error count is displayed. </br>

- **Completion:** When you finish typing the entire sentence or paragraph correctly, the test ends and your final WPM and error count are displayed. </br>

# Example Output
```vbnet
    Hello world my name is Amber and I am a full stack developer.
    WPM: 68 | Errors: 3
    You completed the text! Press any key to play again or Esc to quit.
```

<p align="right">(<a href="#readme-top">top of page</a>)</p>



### Contributing

I have learned that contributions are the heart of what makes the open source community such an amazing place! We are constantly able to learn, grow, inspire eachother, and create incredible things. Any contributions you make are **greatly appreciated**, we are so lucky to be here together.

If you have a suggestion that would make this project better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please, don't forget to give the project a :star:! 

I appreciate you!

<p align="right">(<a href="#readme-top">top of page</a>)</p>



### License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">top of page</a>)</p>



### Acknowledgments

Please take some time to check out the links below! I found value in each and every one of them while creating this project, so my hope is that you will to!

* [9 HOURS of Python Projects](https://youtu.be/NpmFbWO6HPU?si=Y0C6tmCBdUZhawBg) - Special thank you to _Tech With Tim_ for the tutorial!
* [Best README Template](https://github.com/othneildrew/Best-README-Template)
* [Basic Syntax: Markdown Guide](https://www.markdownguide.org/basic-syntax/#reference-style-links)
* [Formatting Syntax: GitHub](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md#animal-bug)

<p align="right">(<a href="#readme-top">top of page</a>)</p>