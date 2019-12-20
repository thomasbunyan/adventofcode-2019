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
  asteroids = {};
  for (let asteroid of Object.keys(detections)) {
    let { y, x } = getCoords(asteroid);
    compGradients = {};
    for (let asteroidCheck of Object.keys(detections)) {
      if (asteroid == asteroidCheck) continue;
      let { yCheck, xCheck } = { yCheck: getCoords(asteroidCheck).y, xCheck: getCoords(asteroidCheck).x };
      let { yT, xT } = getEqu(y, x, yCheck, xCheck);
      if (compGradients[yT + "," + xT]) {
        compGradients[yT + "," + xT].push(yCheck + "," + xCheck);
      } else {
        compGradients[yT + "," + xT] = [yCheck + "," + xCheck];
      }
    }
    asteroids[y + "," + x] = compGradients;
  }
  return asteroids;
};

let getBest = (asteroids) => {
  let bestPos = "";
  let best = 0;
  Object.entries(asteroids).forEach((a) => {
    let count = Object.keys(a[1]).length;
    if (count > best) {
      bestPos = a[0];
      best = count;
    }
  });
  return { pos: bestPos, count: best };
};

let vaporise = (asteroids) => {
  let best = getBest(asteroids);
  let data = asteroids[best.pos];
  data = sortData(data, best);
  let vaporised = [];

  let index = 0;
  while (vaporised.length < Object.keys(asteroids).length - 1) {
    if (data[index][1].length > 0) vaporised.push(data[index][1].shift());
    if (index == data.length - 1) index = 0;
    else index++;
  }
  return vaporised;
};

let sortData = (data, best) => {
  data = Object.entries(data);
  data.sort((a, b) => {
    let aGrad = getCoords(a[0]);
    let bGrad = getCoords(b[0]);

    if (["1,0"].includes(a[0]) || ["1,0"].includes(b[0])) {
      if (["1,0"].includes(a[0])) return -1;
      else return 1;
    }
    if ((aGrad.y > 0 && aGrad.x < 0) || (bGrad.y > 0 && bGrad.x < 0)) {
      if (aGrad.y > 0 && aGrad.x < 0 && bGrad.y > 0 && bGrad.x < 0) return Math.abs(bGrad.y / bGrad.x) - Math.abs(aGrad.y / aGrad.x);
      else if (aGrad.y > 0 && aGrad.x < 0) return -1;
      else return 1;
    }
    if (["0,-1"].includes(a[0]) || ["0,-1"].includes(b[0])) {
      if (["0,-1"].includes(a[0])) return -1;
      else return 1;
    }
    if ((aGrad.y < 0 && aGrad.x < 0) || (bGrad.y < 0 && bGrad.x < 0)) {
      if (aGrad.y < 0 && aGrad.x < 0 && bGrad.y < 0 && bGrad.x < 0) return Math.abs(aGrad.y / aGrad.x) - Math.abs(bGrad.y / bGrad.x);
      else if (aGrad.y < 0 && aGrad.x < 0) return -1;
      else return 1;
    }
    if (["-1,0"].includes(a[0]) || ["-1,0"].includes(b[0])) {
      if (["-1,0"].includes(a[0])) return -1;
      else return 1;
    }
    if ((aGrad.y < 0 && aGrad.x > 0) || (bGrad.y < 0 && bGrad.x > 0)) {
      if (aGrad.y < 0 && aGrad.x > 0 && bGrad.y < 0 && bGrad.x > 0) return Math.abs(bGrad.y / bGrad.x) - Math.abs(aGrad.y / aGrad.x);
      else if (aGrad.y < 0 && aGrad.x > 0) return -1;
      else return 1;
    }
    if (["0,1"].includes(a[0]) || ["0,1"].includes(b[0])) {
      if (["0,1"].includes(a[0])) return -1;
      else return 1;
    }
    if ((aGrad.y > 0 && aGrad.x > 0) || (bGrad.y > 0 && bGrad.x > 0)) {
      if (aGrad.y > 0 && aGrad.x > 0 && bGrad.y > 0 && bGrad.x > 0) return Math.abs(aGrad.y / aGrad.x) - Math.abs(bGrad.y / bGrad.x);
      else if (aGrad.y > 0 && aGrad.x > 0) return -1;
      else return 1;
    }
  });
  data.forEach((ast) => {
    ast[1].sort((a, b) => {
      let pos = getCoords(best.pos);
      let aPos = getCoords(a);
      let bPos = getCoords(b);
      let aDis = Math.abs(aPos.x - pos.x) + Math.abs(aPos.y - pos.y);
      let bDis = Math.abs(bPos.x - pos.x) + Math.abs(bPos.y - pos.y);
      return aDis - bDis;
    });
  });
  return data;
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
vaporisedList = vaporise(asteroidsDetected);
console.log("200th:", vaporisedList[199]);
