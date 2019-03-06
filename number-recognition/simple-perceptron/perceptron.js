// Simple perceptron
class Perceptron {
    /* n is the number of inputs, and c the learning constant */
    constructor(n, c) {
        this.lc = c; // learning constant
        this.weights = new Array(n);
        for (let i = 0; i < n; i++) {
            this.weights[i] = random (-1, 1);
        }
    }

    /* function to train the perceptron */
    train(inputs, desired) {
        let guess = this.feedForward(inputs);
        let error = desired - guess; // Compute the factor for changing the weight based on the error (-2, 0 or 2)
        for (let i = 0; i < this.weights.length; i++) {
            this.weights[i] += error * this.lc * inputs[i]; // Adjust weights based on weightChange * input
        }
    }

    /* guess a answer: -1 or 1 */
    feedForward(inputs) {
    let sum = 0;
    for (let i = 0; i < this.weights.length; i++) {
      sum += inputs[i] * this.weights[i];
    }
    return this.activate(sum); // Result is sign of the sum, -1 or 1
  }

  activate(sum) {
    if (sum > 0) return 1;
    else return -1;
  }

  getWeights() {
    return this.weights;
  }

}