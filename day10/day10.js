const fs = require("fs");
let input = fs.readFileSync("./input.txt", "utf8").split(/\r?\n/);

let detections = {};

let scanSpace = () => {
  for (let y = 0; y < input.length; y++) {
    for (let x = 0; x < input[y].length; x++) {
      if (input[y][x] == "#") {
        detections[y + "," + x] = 0;
      }
    }
  }
};

let countAsteroids = (y, x) => {
  counter = [];
  for (let asteroid of Object.keys(detections)) {
    let { y, x } = getCoords(asteroid);
    compGradients = new Set([]);
    for (let asteroidCheck of Object.keys(detections)) {
      if (asteroid == asteroidCheck) continue;
      let { yCheck, xCheck } = { yCheck: getCoords(asteroidCheck).y, xCheck: getCoords(asteroidCheck).x };
      let { yT, xT } = getEqu(y, x, yCheck, xCheck);
      compGradients.add(yT + "," + xT);
    }
    counter.push(compGradients.size);
  }
  return counter;
};

let getEqu = (y, x, yCheck, xCheck) => {
  let yT = y - yCheck;
  let xT = x - xCheck;
  if (yT == 0) {
    return { yT: yT, xT: xT / Math.abs(xT) };
  } else if (xT == 0) {
    return { xT: xT, yT: yT / Math.abs(yT) };
  }
  let hcf = findHCF(Math.abs(yT), Math.abs(xT));
  if (hcf == "err" || hcf == 1) return { yT, xT };
  else {
    return { yT: yT / hcf, xT: xT / hcf };
  }
};

let findHCF = (x, y) => {
  if (x < 1 || y < 1) return "err";
  while (Math.max(x, y) % Math.min(x, y) != 0) {
    if (x > y) x %= y;
    else y %= x;
  }
  return Math.min(x, y);
};

let getCoords = (asteroid) => {
  return { y: asteroid.split(",")[0], x: asteroid.split(",")[1] };
};

scanSpace();
asteroidsDetected = countAsteroids();
console.log(Math.max(...asteroidsDetected));
