const fs = require("fs");
let input = fs.readFileSync("./input.txt", "utf8");

const width = 25;
const height = 6;

let getLayers = () => {
  rows = [];
  layers = [];
  for (let i = 0; i < input.length; i += width) {
    rows.push(input.slice(i, i + width));
  }
  for (let i = 0; i < rows.length; i += height) {
    layers.push(rows.slice(i, i + height));
  }
  return layers;
};

let getImage = (layers) => {
  image = layers[layers.length - 1];
  for (let layer = layers.length - 2; layer >= 0; layer--) {
    for (let i = 0; i < layers[layer].length; i++) {
      for (let j = 0; j < layers[layer][i].length; j++) {
        if (layers[layer][i][j] == 0) {
          image[i] = image[i].replaceAt(j, "0");
        } else if (layers[layer][i][j] == 1) {
          image[i] = image[i].replaceAt(j, "1");
        }
      }
    }
  }
  return image;
};

let printImage = (image) => {
  for (let i = 0; i < image.length; i++) {
    image[i] = image[i].replace(/0/g, "  ");
    image[i] = image[i].replace(/1/g, "[]");
  }
  console.log(image);
};

String.prototype.replaceAt = function(index, replacement) {
  return this.substr(0, index) + replacement + this.substr(index + replacement.length);
};

printImage(getImage(getLayers()));
