# Trivia Application

A Python-based trivia game using Tkinter for the GUI, pandas for question management, and Pillow for image handling.

## Motivation
During high school, whenever I found myself getting bored in lectures, I would always switch tabs to Jetpunk where I would proceed to simultaneously memorize and learn the countries of the world. Once that became repetitive, I started quizzing myself on world capitals, world flags, and the provinces of various countries. To quote an Instagram reel I saw, perhaps that's why no one knew me in grade 9, but after learning Python, I thought to make use of this inexplicable hobby of mine and build my own Trivia Quiz application that can continue to refresh my knowledge in different categories of interest to me. While I could continue to use Jetpunk, using my own application would provide additional satisfaction and amusement, and I would also learn some of the behind-the-scenes workings of those quizzes I enjoy so much.

## Requirements
- Python 3.x
- pillow
- pandas

## Features
- **Category Selection**  
  User may select from a list of categories, displayed as buttons. Each category would provide a different set of questions.

- **Constant Exit Button**  
  In case the user would like to leave before finishing all the questions, there is always an exit button present in both the category selection and the question windows.

- **Confirmation Section**  
  In case a user clicks the exit button by accident, a confirmation window will show, confirming if they would like to leave. Clicking 'yes' would toggle to a 'Retake Quiz?' window whereas 'no' would resume the quiz from where they left off.

- **Retake Option**  
  Once the quiz ends, there is an option to retake the quiz. Clicking 'yes' would restart the quiz whereas 'no' would end the quiz and the window will close.

- **Scorekeeping**  
  For every question that is correct, one point would be added to a tally. The final score would show once the user ends the quiz.

- **Hover Animation**  
  The button color would change upon the cursor, to make the user better aware of their action.
