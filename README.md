# Hasenhuttl
Premier League guess-the-player app

Changelog (MM/DD/YY):

12/07/23 - Added styling to the '.match' cards that will display white font colour against the green background. Added styling to all clue cards to increase the font size and center the text content with flex display.

Changed textContent from appending directly to clueCard3 to a p tag which will be appended to clueCard3 (makes styling the text possible).

Create p element and create text content containing format string userChoice and append it to the clue card with '.hint-bar-name' class. This will display the user's guess on every iteration of the hintbar.

12/06/23 - Created logic that will loop through the playerList comparing the userChoice to the property name value of each object in the playerlist. When userChoice matches the current loop iteration's name value, it will compare the current iteration to the mystery player name value. If they are the same, the class '.match' will be added to the clue card changing the background colour to green. If they are not the same, '.match' will not be added. Text content displaying the property value of the current clue card.

12/05/23 - Created div .hint-container that holds the hint bars for each guess. Added overflow scroll on y-axis to keep the hint bars condensed. Created function hintGenerator() which is called when the listener on playerGuess is triggered. This function will create a hintbar and divs for player name, team, nationality, position, age, jersey number. The hintbar will be appended to the hint container. The various divs will be appended to the hintbar.

11/14/23 - Created base of logic for the guessing game. Stored input value inside a variable userChoice. Created array of objects containing two premier league players with relevant keys and values. Created variable that randomly selects one of the player objects and stored it in mysteryPlayer. Created function called guessingGame which checks to see if userChoice === mysteryPlayer. Fixed CSS positioning of sillhouette button and input so that it shrinks with page.

11/10/23 - Created modals for how to play, stats, and show silhouette buttons. Added minimal styling to the modals. Used html element dialog to create the modals. Added event listeners to show and hide buttons to display and close dialog box on click. Added "To-do list"

08/14/23 - Finished styling for all elements. Specifically, adjusted input to a comfortable height and width. Added a slim border to input. Added placeholder text to input.

08/13/23 - Completed flexbox positioning for all elements. Finished styling for header, app title and description, and footer.

08/12/23 - Created html elements for header and guessing game. Began styling and layout for header.

To-do List:

- ~~Take value from input field and store it in a variable.~~
- ~~Create game which displays the hint bar with categories.~~
- ~~Creat functionality for comparing the user's guessed player to the mystery player.~~
- ~~Create player object to test the game.~~
- Repeat same logic used for clueCard3 for all the clue cards on the hint bar.
- Fix issue where player name, team, nationality, position, age, jersey number divs are being appended to EVERY hintbar instead of only the last child of the parent node which is what I understand it should be doing.