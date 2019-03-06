// population
let training = new Array(1000);
let perceptron;

let count = 0;  // train the perceptron with a point at a time

// Coordinate space
let xMin = -1;
let yMin = -1;
let xMax = 1;
let yMax = 1;

// The function to describe a line
function f(x) {
  return 0.3 * x + 0.2;
}


function setup() {
    createCanvas(400, 400);

    // The perceptron has 3 inputs -- x, y, and bias
    perceptron = new Perceptron(3, 0.001);

     // Create a random set of training points and calculate the "known" answer
    for (let i = 0; i < training.length; i++) {
        let x = random(xMin, xMax);
        let y = random(yMin, yMax);
        let answer = 1;
        if (y < f(x)) answer = -1;
        training[i] = {
          input: [x, y, 1],
          output: answer
        };
    }
}

function draw() {
    background(0);

    // Draw the line
    strokeWeight(1);
    stroke(255);
    let x1 = map(xMin, xMin, xMax, 0, width);
    let y1 = map(f(xMin), yMin, yMax, height, 0);
    let x2 = map(xMax, xMin, xMax, 0, width);
    let y2 = map(f(xMax), yMin, yMax, height, 0);
    line(x1, y1, x2, y2);

    // Draw the line based on the current weights
    // Formula is weights[0]*x + weights[1]*y + weights[2] = 0
    stroke(255);
    let weights = perceptron.getWeights();
    x1 = xMin;
    y1 = (-weights[2] - weights[0] * x1) / weights[1];
    x2 = xMax;
    y2 = (-weights[2] - weights[0] * x2) / weights[1];

    x1 = map(x1, xMin, xMax, 0, width);
    y1 = map(y1, yMin, yMax, height, 0);
    x2 = map(x2, xMin, xMax, 0, width);
    y2 = map(y2, yMin, yMax, height, 0);
    line(x1, y1, x2, y2);

    // Train the Perceptron with one "training" point at a time
    perceptron.train(training[count].input, training[count].output);
    count = (count + 1) % training.length;

    for (let i = 0; i < count; i++) {
        stroke(255);
        strokeWeight(1);
        fill(255);
        let guess = perceptron.feedForward(training[i].input);
        if (guess > 0) noFill();

        let x = map(training[i].input[0], xMin, xMax, 0, width);
        let y = map(training[i].input[1], yMin, yMax, height, 0);
        ellipse(x, y, 8, 8);
  }
}