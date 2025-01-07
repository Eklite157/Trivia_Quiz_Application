# Trivia Application

A Python-based trivia game using Tkinter for the GUI, pandas for question management, and Pillow for image handling.

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
  In case a user clicks the exit button by accident, a confirmation window will show, confirming if they would like to leave. Clicking 'yes' would toggle to a 'Retake Quiz?' window whereas 'no' would resume the quiz from     where they left off.

- **Retake Option**  
  Once the quiz ends, there is an option to retake the quiz. Clicking 'yes' would restart the quiz whereas 'no' would end the quiz and the window will close.

- **Scorekeeping**  
  For every question that is correct, one point would be added to a tally. The final score would show once the user ends the quiz.

- **Hover Animation**  
  The button color would change upon the cursor, to make the user better aware of their action.
