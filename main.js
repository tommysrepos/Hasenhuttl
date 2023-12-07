// how-to-play, stats, player-silhouette modal
//----------how-to-play----------
const howToPlayModal = document.querySelector('.how-to-play-modal');
const howToPlayShow = document.querySelector('.how-to-play');
const howToPlayHide = document.querySelector('.how-to-play-hide');

howToPlayShow.addEventListener('click', () =>{
    howToPlayModal.showModal();
});

howToPlayHide.addEventListener('click', () =>{
    howToPlayModal.close();
});
//----------stats----------
const statsModal = document.querySelector('.stats-modal');
const statsShow = document.querySelector('.stats');
const statsHide = document.querySelector('.stats-hide');

statsShow.addEventListener('click', () =>{
    statsModal.showModal();
});

statsHide.addEventListener('click', () =>{
    statsModal.close();
});
//----------player-silhouette----------
const playerSilhouetteModal = document.querySelector('.player-silhouette-modal');
const playerSilhouetteShow = document.querySelector('.player-silhouette-button');
const playerSilhouetteHide = document.querySelector('.player-silhouette-hide');

playerSilhouetteShow.addEventListener('click', () =>{
    playerSilhouetteModal.showModal();
});

playerSilhouetteHide.addEventListener('click', () =>{
    playerSilhouetteModal.close();
})

//----------User Input Storage----------
const playerGuess = document.querySelector('input');
let userChoice = ''

playerGuess.addEventListener('change', () =>{
    let userChoice = document.querySelector('input').value
    console.log('User choice: ' + userChoice)
    guessingGame(userChoice);
});


//----------Premier League Player data----------
const playerList = [
    {
        name:'Erling Haaland',
        team: 'MCI',
        nationality:'Norway',
        position: 'FWD',
        age: 23,
        number: 9
    },
    {
        name:'Martin Odegaard',
        nationality:'Norway',
        team: 'ARS',
        position: 'MID',
        age: 24,
        number: 8
    },
    {
        name: 'Ross Barkley',
        nationality: 'England',
        team: 'LUT',
        age: 30,
        number: 6
    }
]

//----------Mystery Player----------
let mysteryPlayer = playerList[Math.floor(Math.random()*playerList.length)];
console.log(mysteryPlayer);
console.log('Mystery Player: ' + mysteryPlayer.name)

//----------Guessing Game----------

function guessingGame(userChoice){
    if (userChoice === mysteryPlayer.name){
        console.log('true')
    }else{
        console.log('false');
    }
    hintGenerator(userChoice);
}

//----------Dynamically Adding Hint Bar----------
const hintContainer = document.querySelector('#hint-container');

function hintGenerator(userChoice){
    const hint = document.createElement('div');
    hint.classList.add('hint-bar');
    hintContainer.appendChild(hint);

    const hintBar = document.getElementsByClassName('hint-bar');
    
    for(let i = 0; i<hintBar.length; i++){
        const clueCard = document.createElement('div');
        clueCard.classList.add('clue-card', 'hint-bar-name');
        hintBar[i].appendChild(clueCard);

        // const clueCard2 = document.createElement('div');
        // clueCard2.classList.add('clue-card', 'hint-bar-team');
        // hintBar[i].appendChild(clueCard2);

        const clueCard3 = document.createElement('div');
        clueCard3.classList.add('clue-card', 'hint-bar-nationality');
        // nationalityChecker(userChoice);
        for(let j = 0; j < playerList.length; j++){
            if(userChoice == playerList[j].name){
                if(playerList[j].nationality == mysteryPlayer.nationality){
                    clueCard3.classList.add('match');
                    clueCard3.textContent = `${playerList[j].nationality}`
                }else{
                    clueCard3.textContent = `${playerList[j].nationality}`
                }
            }
        }
        hintBar[i].appendChild(clueCard3);

        // const clueCard4 = document.createElement('div');
        // clueCard4.classList.add('clue-card', 'hint-bar-pos');
        // hintBar[i].appendChild(clueCard4);

        // const clueCard5 = document.createElement('div');
        // clueCard5.classList.add('clue-card', 'hint-bar-age');
        // hintBar[i].appendChild(clueCard5);

        // const clueCard6 = document.createElement('div');
        // clueCard6.classList.add('clue-card', 'hint-bar-number');
        // hintBar[i].appendChild(clueCard6);
    }
}

// function nationalityChecker(userChoice){
//     for(let i = 0; i < playerList.length; i++){
//         if(userChoice == playerList[i].name){
//             if(playerList[i].nationality == mysteryPlayer.nationality){
//                 clueCard3.classList.add('match');
//             }
//         }
//     }
// }