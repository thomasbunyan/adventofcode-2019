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

let count0s = (layers) => {
  layerCount = [];
  for (let i = 0; i < layers.length; i++) {
    counter0 = 0;
    counter1 = 0;
    counter2 = 0;
    let joinedLayer = layers[i].join("");
    for (let j = 0; j < joinedLayer.length; j++) {
      if (joinedLayer[j] == "0") counter0++;
      if (joinedLayer[j] == "1") counter1++;
      if (joinedLayer[j] == "2") counter2++;
    }
    layerCount.push({ 0: counter0, 1: counter1, 2: counter2 });
  }
  return layerCount;
};

let main = () => {
  layerCount = count0s(getLayers());
  min = layerCount[0];
  for (let i = 1; i < layerCount.length; i++) {
    if (layerCount[i][0] < min[0]) min = layerCount[i];
  }
  console.log(min);
  console.log(min[1] * min[2]);
};

main();
