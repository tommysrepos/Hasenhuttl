// how-to-play, stats,  modal
const howToPlayModal = document.querySelector('.how-to-play-modal');
const howToPlayShow = document.querySelector('.how-to-play');
const howToPlayHide = document.querySelector('.how-to-play-hide');

howToPlayShow.addEventListener('click', () =>{
    howToPlayModal.showModal();
});

howToPlayHide.addEventListener('click', () =>{
    howToPlayModal.close();
});

const statsModal = document.querySelector('.stats-modal');
const statsShow = document.querySelector('.stats');
const statsHide = document.querySelector('.stats-hide');

statsShow.addEventListener('click', () =>{
    statsModal.showModal();
});

statsHide.addEventListener('click', () =>{
    statsModal.close();
});

const playerSilhouetteModal = document.querySelector('.player-silhouette-modal');
const playerSilhouetteShow = document.querySelector('.player-silhouette-button');
const playerSilhouetteHide = document.querySelector('.player-silhouette-hide');

playerSilhouetteShow.addEventListener('click', () =>{
    playerSilhouetteModal.showModal();
});

playerSilhouetteHide.addEventListener('click', () =>{
    playerSilhouetteModal.close();
})