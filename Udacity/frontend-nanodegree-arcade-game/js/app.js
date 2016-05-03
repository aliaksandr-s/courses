function Person(x, y, sprite) {
    this.x = x;
    this.y = y;
    this.sprite = sprite;
};

Person.prototype.render = function () {
    ctx.drawImage(Resources.get(this.sprite), this.x, this.y);
};

function Player(x, y, speed, sprite) {
    this.x = x;
    this.y = y;
    this.speed = speed;
    this.sprite = sprite;
    this.savePrincess = false;
}

Player.prototype = new Person();

Player.prototype.playSound = function () {
    var audio = document.getElementsByTagName("audio")[0];
    audio.volume = 0.6;
    audio.play();
};

Player.prototype.render = function () {
    ctx.drawImage(Resources.get(this.sprite), this.x, this.y);
    displayScoreLevel(gameLevel, lives);
};

Player.prototype.handleInput = function (keyPress) {
    if (keyPress == 'left') {
        player.x -= player.speed;
    }
    if (keyPress == 'up') {
        player.y -= player.speed - 17;
    }
    if (keyPress == 'right') {
        player.x += player.speed;
    }
    if (keyPress == 'down') {
        player.y += player.speed - 17 ;
    }
    // console.log('keyPress is: ' + keyPress);
};

Player.prototype.update = function () {
    if (this.y <= 60){
        this.y = 60;
    }
    if (this.y > 383 ) {
        this.y = 383;
    }
    if (this.x > 602.5) {
        this.x = 602.5;
    }
    if (this.x < 2.5) {
        this.x = 2.5;
    }
    if (lives == 0){
        newGame();
    }
    if (this.x == princess.x && this.y == princess.y) {
        this.savePrincess = true;
        nextLevel();
    }
    // console.log(this.x, this.y);
};

function Enemy() {

};

Enemy.prototype = new Person();

function LeftBug(x, y, speed, sprite) {
    this.x = x;
    this.y = y;
    this.speed = speed;
    this.sprite = sprite;
}

LeftBug.prototype = new Enemy();

LeftBug.prototype.update = function(dt) {
    this.x += this.speed*dt
    if (this.x >= canvasWidth) {
        this.x = -100;
    }
    checkCollision(this);
};

function RightBug(x, y, speed, sprite) {
    this.x = x;
    this.y = y;
    this.speed = speed;
    this.sprite = sprite;
}

RightBug.prototype = new Enemy();

RightBug.prototype.update = function(dt) {
    this.x -= this.speed * dt;
    if (this.x <= -100) {
        this.x = 702;
    }
    checkCollision(this);
};

var checkCollision = function(anEnemy) {
    if (
        player.y + 41 >= anEnemy.y
        && player.x <= anEnemy.x + 63
        && player.y <= anEnemy.y + 63
        && player.x + 63 >= anEnemy.x
       ) {
        player.x = 302.5;
        player.y = 383;
        lives -= 1;
    }
};

var newGame  = function () {
    gameLevel = 1;
    lives = 3;
    increaseDifficulty(0);
};

var nextLevel = function () {
    gameLevel += 1;
    increaseDifficulty(gameLevel - 1);
    princessPositionUpdate();
    playerPositionUpdate();
};

var princessPositionUpdate = function () {
    princess.x = princessAvailablePosition[Math.floor(Math.random() * princessAvailablePosition.length)];
};

var playerPositionUpdate = function () {
    player.x = princessAvailablePosition[Math.floor(Math.random() * princessAvailablePosition.length)];
    player.y = 383;
};

var displayScoreLevel = function(aLevel, aLives) {
    var canvas = document.getElementsByTagName('canvas');
    var firstCanvasTag = canvas[0];

    // add player score and level to div element created
    scoreLevelDiv.innerHTML = 'Lives: ' + aLives + '/' + 'Level: ' + aLevel;
    document.body.insertBefore(scoreLevelDiv, firstCanvasTag[0]);
};

var increaseDifficulty = function(numEnemies) {
    // remove all previous enemies on canvas
    allEnemies.length = 0;

    for (var i = 0; i <= numEnemies; i++) {
        var flip = Math.floor(Math.random() * 2);
        if (flip) {
            var enemy = new RightBug(702,
                            enemyAvailablePosition[Math.floor(Math.random() * enemyAvailablePosition.length)],
                            Math.random() * 300 + 100, 'images/reversed-bug.png');
        } else { enemy =  new LeftBug(-100,
                        enemyAvailablePosition[Math.floor(Math.random() * enemyAvailablePosition.length)],
                        Math.random() * 200 + 50, 'images/enemy-bug.png');
        }
        allEnemies.push(enemy);
    }
};

var princessAvailablePosition = [2.5, 102.5, 202.5, 302.5, 402.5, 502.5, 602.5];
var enemyAvailablePosition = [134, 217, 300];

var allEnemies = [];
var lives = 3;
var gameLevel = 1;
var scoreLevelDiv = document.createElement('div');

var princess = new Person(302.5, 60, 'images/char-princess-girl.png');
var player = new Player(302.5, 383, 100, 'images/char-boy.png');


increaseDifficulty(0);



// This listens for key presses and sends the keys to your
// Player.handleInput() method. You don't need to modify this.
document.addEventListener('keyup', function(e) {
    var allowedKeys = {
        37: 'left',
        38: 'up',
        39: 'right',
        40: 'down'
    };

    player.handleInput(allowedKeys[e.keyCode]);
    player.playSound();
});
